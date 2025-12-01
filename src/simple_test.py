print("=== Simple Python Test ===")
print("If you see this, Python is working!")

try:
    import sys
    print(f"Python path: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    import langchain
    print("✅ LangChain imported successfully")
except Exception as e:
    print(f"❌ Error: {e}")
