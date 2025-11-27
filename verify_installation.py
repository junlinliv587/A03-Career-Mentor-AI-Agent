def check_package(package_name, description):
    try:
        __import__(package_name)
        return True, f"✅ {package_name:20} - {description}"
    except ImportError as e:
        return False, f"❌ {package_name:20} - {description} - Error: {e}"

print("=== Career Mentor AI Agent - Environment Verification ===\n")

# Core packages to check
packages_to_check = [
    ("langchain", "AI Agent Framework"),
    ("langchain_community", "Community Integrations"),
    ("chromadb", "Vector Database"),
    ("streamlit", "Web Interface"),
    ("fastapi", "API Backend"),
    ("openai", "AI Models"),
    ("pydantic", "Data Validation"),
    ("uvicorn", "ASGI Server"),
]

print("Checking core package installation:")
all_success = True

for package, description in packages_to_check:
    success, message = check_package(package, description)
    print(message)
    if not success:
        all_success = False

print("\n" + "="*50)
if all_success:
    print("🎉 SUCCESS: All core packages installed correctly!")
    print("🚀 You are ready to start coding your AI Agent!")
else:
    print("⚠️  Some packages failed to import. Please check the errors above.")

print("="*50)
