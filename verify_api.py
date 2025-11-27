import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {bool(api_key)}")
if api_key:
    print(f"Key starts with: {api_key[:10]}...")
    print("✅ API Key configuration successful!")
else:
    print("❌ API Key not found. Please check your .env file.")
