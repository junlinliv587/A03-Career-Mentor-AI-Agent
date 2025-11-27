import os
import sys

print("=== Debug Environment Check ===")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.executable}")
print(f"Files in current directory: {os.listdir('.')}")

# Check if we're in the right place
if 'src' in os.listdir('.'):
    print("✅ 'src' folder found in current directory")
else:
    print("❌ 'src' folder NOT found - wrong directory?")

print("\n=== Checking Package Imports ===")

try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ dotenv imported successfully")
except Exception as e:
    print(f"❌ dotenv import failed: {e}")

try:
    import langchain
    print("✅ langchain imported successfully")
except Exception as e:
    print(f"❌ langchain import failed: {e}")

try:
    import chromadb
    print("✅ chromadb imported successfully")
except Exception as e:
    print(f"❌ chromadb import failed: {e}")

print("\n=== Checking Config Import ===")

try:
    from config import Config
    print("✅ Config imported successfully")
    api_key_exists = bool(Config.OPENAI_API_KEY)
    print(f"API Key configured: {api_key_exists}")
    if not api_key_exists:
        print("⚠️  WARNING: OPENAI_API_KEY is empty or not set")
except Exception as e:
    print(f"❌ Config import failed: {e}")

print("\n=== Environment Variables Check ===")
env_key = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY from environment: {bool(env_key)}")

print("\n=== Debug Check Complete ===")
