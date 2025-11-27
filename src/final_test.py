print("=== FINAL ENVIRONMENT TEST ===")

# Test basic imports
try:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ dotenv: OK")
except Exception as e:
    print(f"❌ dotenv: {e}")

# Test config
try:
    from config import Config
    print("✅ config: OK")
    print(f"   API Key: {bool(Config.OPENAI_API_KEY)}")
    print(f"   DB Path: {Config.CHROMA_DB_PATH}")
except Exception as e:
    print(f"❌ config: {e}")

# Test AI packages
try:
    import langchain
    print("✅ langchain: OK")
except Exception as e:
    print(f"❌ langchain: {e}")

print("=== TEST COMPLETE ===")
