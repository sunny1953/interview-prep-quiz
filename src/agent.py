from typing import Dict, List
from .models.question import Question
from .models.user_profile import UserProfile
from .utils.gemini_helper import GeminiHelper

class QuizAgent:
    def __init__(self):
        self.user_profile = UserProfile()
        self.gemini = GeminiHelper()
        self.current_subject_index = 0
        self.used_questions = set()  # Track used questions by their content
        
    def _select_domain(self):
        """Let user select their interview preparation domain"""
        print("\nWelcome! Let's customize your interview preparation quiz.")
        print("\nAvailable Domains:")
        
        domains = {
            # Software & Tech Domains
            '1': 'Software Development',
            '2': 'Data Science',
            '3': 'Machine Learning',
            '4': 'Cybersecurity',
            '5': 'System Design',
            '6': 'DevOps',
            '7': 'Cloud Computing',
            '8': 'English Communication',
            
            # 3D & Game Development
            '9': 'Unity Development',
            '10': 'Unreal Engine',
            '11': 'Blender',
            '12': 'Autodesk Maya',
            '13': '3D Modeling',
            
            # XR Development
            '14': 'Augmented Reality',
            '15': 'Virtual Reality'
        }
        
        # Print domains in categories
        print("\n=== Software & Tech Domains ===")
        for i in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print(f"{i}. {domains[i]}")
            
        print("\n=== 3D & Game Development ===")
        for i in ['9', '10', '11', '12', '13']:
            print(f"{i}. {domains[i]}")
            
        print("\n=== XR Development ===")
        for i in ['14', '15']:
            print(f"{i}. {domains[i]}")
            
        while True:
            choice = input("\nSelect your interview preparation domain (1-15): ")
            if choice in domains:
                selected_domain = domains[choice]
                self.user_profile.domain = selected_domain
                print(f"\nSelected domain: {selected_domain}")
                
                # Update subjects based on domain
                self.gemini.set_domain_subjects(selected_domain)
                return
            print("Invalid choice. Please try again.")

    async def start_quiz(self):
        """Start the quiz session"""
        print("Welcome to the Domain-Specific Interview Preparation Quiz!")
        
        # Select domain first
        self._select_domain()

        while True:
            question = await self._generate_next_question()
            if not question:
                print("Error generating question. Ending quiz.")
                break

            is_correct = await self._ask_question(question)
            self._evaluate_performance(question, is_correct)
            
            # Ask if user wants to continue
            if not self._should_continue():
                break

    async def _generate_next_question(self) -> Question:
        """Generate the next question based on user's profile and progress"""
        try:
            # Debug logging
            print(f"Current domain: {self.user_profile.domain}")
            print(f"Available subjects: {self.gemini.subjects}")
            print(f"Current subject index: {self.current_subject_index}")
            
            if not self.user_profile.domain:
                print("Error: No domain selected")
                return None
                
            if not self.gemini.subjects:
                print("Error: No subjects available. Attempting to reinitialize...")
                try:
                    self.gemini.set_domain_subjects(self.user_profile.domain)
                    print(f"Reinitialized subjects: {self.gemini.subjects}")
                except Exception as e:
                    print(f"Failed to reinitialize subjects: {str(e)}")
                    return None
                
            # Reset subject index if it's out of bounds
            if self.current_subject_index >= len(self.gemini.subjects):
                self.current_subject_index = 0
                
            # Rotate through subjects
            subject = self.gemini.subjects[self.current_subject_index]
            self.current_subject_index = (self.current_subject_index + 1) % len(self.gemini.subjects)

            print(f"Selected subject: {subject}")
            print(f"Difficulty level: {self.user_profile.difficulty_level}")

            # Generate question with current parameters
            question = await self.gemini.generate_question(
                subject=subject,
                difficulty=self.user_profile.difficulty_level or 'medium'  # Default to medium if not set
            )

            # Ensure question is unique
            attempts = 0
            while question and question.content in self.used_questions and attempts < 3:
                question = await self.gemini.generate_question(
                    subject=subject,
                    difficulty=self.user_profile.difficulty_level or 'medium'
                )
                attempts += 1

            if question:
                self.used_questions.add(question.content)
                print("Successfully generated question")
            else:
                print("Failed to generate question")
                
            return question
            
        except Exception as e:
            print(f"Error in _generate_next_question: {str(e)}")
            return None

    def _should_continue(self):
        """Ask user if they want to continue the quiz"""
        while True:
            response = input("\nWould you like another question? (y/n): ").lower()
            if response in ['y', 'n']:
                return response == 'y'
            print("Please enter 'y' for yes or 'n' for no.")

    async def _ask_question(self, question: Question) -> bool:
        """Present the question to the user and return whether the answer was correct"""
        print(f"\n{question.content}")
        
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                # Add hint option
                print("\nEnter 'h' for a hint or a number for your answer")
                answer = input("\nEnter your answer (1-{}, h for hint): ".format(len(question.options)))
                
                if answer.lower() == 'h':
                    # Get hint from Gemini
                    hint = await self.gemini.generate_hint(question.content, question.topic)
                    print(f"\nHint: {hint}")
                    continue
                
                answer_idx = int(answer) - 1
                if 0 <= answer_idx < len(question.options):
                    user_answer = question.options[answer_idx]
                    is_correct = user_answer == question.correct_answer
                    
                    print("Correct!" if is_correct else f"Wrong. The correct answer was: {question.correct_answer}")
                    
                    # Get explanation from Gemini
                    explanation = await self.gemini.explain_answer(
                        question.content, 
                        question.correct_answer,
                        question.topic
                    )
                    print(f"\nExplanation: {explanation}")
                    
                    return is_correct
            except ValueError:
                pass
            print("Invalid input. Please try again.")

    def _evaluate_performance(self, question: Question, is_correct: bool):
        """Enhanced performance evaluation"""
        question.times_asked += 1
        if is_correct:
            question.times_correct += 1
        
        # Update user profile
        self.user_profile.update_performance(question, is_correct)
        
        # Calculate success rate
        success_rate = question.times_correct / question.times_asked
        
        # Update difficulty level based on recent performance
        recent_results = self.user_profile.performance_history[-5:]  # Last 5 questions
        if len(recent_results) >= 5:
            correct_count = sum(1 for result in recent_results if result['correct'])
            success_percentage = (correct_count / len(recent_results)) * 100
            
            if success_percentage >= 80 and self.user_profile.difficulty_level != 'hard':
                self.user_profile.difficulty_level = 'hard'
                print("\nExcellent progress! Difficulty increased to: hard")
            elif success_percentage <= 40 and self.user_profile.difficulty_level != 'easy':
                self.user_profile.difficulty_level = 'easy'
                print("\nDifficulty adjusted to: easy. Keep practicing!")
            elif 40 < success_percentage < 80 and self.user_profile.difficulty_level != 'medium':
                self.user_profile.difficulty_level = 'medium'
                print("\nDifficulty adjusted to: medium")
