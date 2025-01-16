import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=api_key)

def get_gemini_model():
    """Initialize and return the Gemini model"""
    return genai.GenerativeModel('gemini-pro') 