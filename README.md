# Interview Prep Quiz

An AI-powered adaptive learning platform for interview preparation across multiple technical domains and English communication skills.

## Features

- 15+ specialized technical domains
- AI-powered question generation
- Real-time answer validation
- Adaptive difficulty levels
- English grammar and communication focus
- Interactive hints and explanations
- Progress tracking

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3.x, Flask
- **AI**: Google Gemini AI
- **Dependencies**: Requirements listed in `requirements.txt`

## Prerequisites

1. Python 3.8 or higher
2. Google Gemini API key
3. pip (Python package manager)

## Step-by-Step Setup

### 1. Create Project Directory
```bash
mkdir interview-prep-quiz
cd interview-prep-quiz
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Create a requirements.txt file with:
```txt
Flask==2.0.1
python-dotenv==1.0.0
google-generativeai==0.3.0
asgiref==3.7.2
pytest==7.4.0
pytest-asyncio==0.21.1
```

Then install:
```bash
pip install -r requirements.txt
```

### 4. Project Structure Setup
Create the following directory structure:
```
interview-prep-quiz/
├── app.py
├── requirements.txt
├── .env
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── select_domain.html
└── src/
    ├── agent.py
    ├── models/
    │   ├── question.py
    │   └── user_profile.py
    └── utils/
        ├── gemini_helper.py
        └── gemini_config.py
```

### 5. Environment Configuration
Create a `.env` file:
```env
FLASK_SECRET_KEY=your_secret_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
FLASK_ENV=development
```

### 6. Running the Application
```bash
python app.py
```
The application will be available at `http://localhost:5000`

## Usage Guide

### 1. Starting the Quiz
- Visit `http://localhost:5000`
- Click "Start Quiz" or "Select Domain"
- Choose your preferred domain:
  - Software Development
  - Data Science
  - English Communication
  - And more...

### 2. Taking the Quiz
- Questions are generated based on selected domain
- Choose from multiple choice options
- Get immediate feedback
- Use hints when needed
- View detailed explanations

### 3. Difficulty Levels
- Easy: Basic concepts
- Medium: Practical applications
- Hard: Advanced scenarios
- Adapts based on performance

### 4. English Communication Mode
- Grammar focus
- Business communication
- Writing skills
- Professional vocabulary
- Real-world scenarios

## Available Domains

### Software & Tech
- Software Development
- Data Science
- Machine Learning
- Cybersecurity
- System Design
- DevOps
- Cloud Computing

### 3D & Game Development
- Unity Development
- Unreal Engine
- Blender
- Autodesk Maya
- 3D Modeling

### XR Development
- Augmented Reality
- Virtual Reality

## Troubleshooting

### Common Issues

1. Question Generation Fails
   - Verify API key in .env
   - Check internet connection
   - Ensure valid domain selection

2. Session Errors
   - Clear browser cache
   - Restart Flask server
   - Check secret key configuration

3. Dependencies Issues
   - Verify Python version
   - Reinstall requirements
   - Check virtual environment activation

## Development Notes

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Testing
```bash
# Run tests
pytest tests/
```

### Security
- Never commit .env file
- Keep API keys secure
- Validate all user inputs
- Handle errors gracefully

## Support

For support:
1. Check documentation
2. Review error logs
3. Verify configurations
4. Check console for errors

## Future Enhancements

- User authentication
- Progress persistence
- Performance analytics
- Mobile application
- Additional domains
- Custom question sets

---
Created for interview preparation and skill enhancement. 