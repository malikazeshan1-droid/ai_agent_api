import sys
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Add backend to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from app.services.gemini_service import gemini_service
from app.config import settings

def test_gemini():
    print(f"Testing Gemini with key: {settings.GEMINI_API_KEY[:10]}...")
    try:
        print("Available models:")
        for m in genai.list_models():
            print(f" - {m.name}")
        
        response = gemini_service.generate_response("Say 'Gemini is active'")
        print(f"Response: {response}")
    except Exception as e:
        print(f"❌ Gemini Error: {e}")

if __name__ == "__main__":
    test_gemini()
