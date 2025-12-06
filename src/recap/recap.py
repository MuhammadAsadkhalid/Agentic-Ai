# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Get API key from .env
# api_key = os.environ.get("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Create model
# model = genai.GenerativeModel(
#     model_name='gemini-2.0-flash',
#     system_instruction="You are a helpful medical assistant. Provide accurate, clear medical information. Always recommend consulting with a real doctor for serious conditions."
# )

# # Ask question
# response = model.generate_content("What is the reason behind fever?")

# print(response.text)

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction="You are a helpful medical assistant. Provide accurate, clear medical information. Always recommend consulting with a real doctor for serious conditions."
)

response = model.generate_content("What is the reason behind fever?")

print(response.text)