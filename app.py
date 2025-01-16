from flask import Flask, render_template, request, jsonify, session, redirect
from src.agent import QuizAgent
import asyncio
import os
from dotenv import load_dotenv
from asgiref.sync import async_to_sync
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key')

# Initialize quiz agent
quiz_agent = QuizAgent()

def run_async(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        return async_to_sync(f)(*args, **kwargs)
    return wrapped

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_domain', methods=['GET'])
def get_domains():
    domains = {
        'Software & Tech': {
            '1': 'Software Development',
            '2': 'Data Science',
            '3': 'Machine Learning',
            '4': 'Cybersecurity',
            '5': 'System Design',
            '6': 'DevOps',
            '7': 'Cloud Computing',
            '8': 'English Communication'
        },
        '3D & Game Development': {
            '9': 'Unity Development',
            '10': 'Unreal Engine',
            '11': 'Blender',
            '12': 'Autodesk Maya',
            '13': '3D Modeling'
        },
        'XR Development': {
            '14': 'Augmented Reality',
            '15': 'Virtual Reality'
        }
    }
    return render_template('select_domain.html', domains=domains)

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    domain_id = request.form.get('domain')
    if not domain_id:
        return jsonify({'error': 'No domain selected'}), 400
        
    # Map domain_id to domain name
    domain_map = {
        '1': 'Software Development', '2': 'Data Science', '3': 'Machine Learning',
        '4': 'Cybersecurity', '5': 'System Design', '6': 'DevOps',
        '7': 'Cloud Computing', '8': 'English Communication', '9': 'Unity Development',
        '10': 'Unreal Engine', '11': 'Blender', '12': 'Autodesk Maya',
        '13': '3D Modeling', '14': 'Augmented Reality', '15': 'Virtual Reality'
    }
    
    domain = domain_map.get(domain_id)
    if not domain:
        return jsonify({'error': 'Invalid domain'}), 400
        
    # Initialize quiz for the selected domain
    quiz_agent.user_profile.domain = domain
    quiz_agent.gemini.set_domain_subjects(domain)
    session['domain'] = domain
    
    return jsonify({'success': True, 'redirect': '/quiz'})

@app.route('/quiz')
def quiz():
    try:
        domain = request.args.get('domain')
        print(f"Quiz route - Received domain: {domain}")
        
        if not domain:
            print("No domain provided, redirecting to domain selection")
            return redirect('/select_domain')
        
        # Initialize quiz for the selected domain
        print(f"Initializing quiz for domain: {domain}")
        try:
            quiz_agent.user_profile.domain = domain
            quiz_agent.gemini.set_domain_subjects(domain)
            session['domain'] = domain
            print(f"Quiz initialization complete. Subjects: {quiz_agent.gemini.subjects}")
        except Exception as e:
            print(f"Error during quiz initialization: {str(e)}")
            return redirect('/select_domain')
        
        return render_template('quiz.html', domain=domain)
        
    except Exception as e:
        print(f"Error in quiz route: {str(e)}")
        return redirect('/select_domain')

@app.route('/get_question', methods=['GET'])
@run_async
async def get_question():
    try:
        if not quiz_agent.gemini.subjects:
            domain = session.get('domain')
            if domain:
                print(f"Reinitializing quiz agent for domain: {domain}")
                quiz_agent.user_profile.domain = domain
                quiz_agent.gemini.set_domain_subjects(domain)
            else:
                return jsonify({'error': 'No domain selected'}), 400
        
        question = await quiz_agent._generate_next_question()
        if not question:
            return jsonify({'error': 'Failed to generate question'}), 500
            
        return jsonify({
            'question': question.content,
            'options': question.options,
            'topic': question.topic,
            'difficulty': question.difficulty,
            'correct_answer': question.correct_answer
        })
    except Exception as e:
        print(f"Error generating question: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/check_answer', methods=['POST'])
@run_async
async def check_answer():
    try:
        data = request.get_json()
        question_text = data.get('question')
        selected_answer = data.get('answer')
        correct_answer = data.get('correct_answer')
        topic = data.get('topic')
        
        is_correct = selected_answer == correct_answer
        
        # Get explanation
        explanation = await quiz_agent.gemini.explain_answer(
            question_text,
            correct_answer,
            topic
        )
        
        return jsonify({
            'correct': is_correct,
            'explanation': explanation
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_hint', methods=['POST'])
@run_async
async def get_hint():
    try:
        data = request.get_json()
        question_text = data.get('question')
        topic = data.get('topic')
        
        hint = await quiz_agent.gemini.generate_hint(question_text, topic)
        return jsonify({'hint': hint})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 