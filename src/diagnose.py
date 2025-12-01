import os
import openai
from dotenv import load_dotenv

load_dotenv()

print("=== AI Agent 诊断 ===")

# 1. 检查API密钥
api_key = os.getenv("OPENAI_API_KEY")
print(f"1. API密钥配置: {bool(api_key)}")
if api_key:
    print(f"   API密钥开头: {api_key[:10]}...")

# 2. 检查包导入
try:
    from langchain_core.prompts import ChatPromptTemplate
    print("2. ✅ LangChain Core 导入成功")
except ImportError as e:
    print(f"2. ❌ LangChain Core 导入失败: {e}")

try:
    from langchain_openai import ChatOpenAI
    print("3. ✅ LangChain OpenAI 导入成功")
except ImportError as e:
    print(f"3. ❌ LangChain OpenAI 导入失败: {e}")

# 3. 测试直接OpenAI调用
try:
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say 'Hello World!'"}],
        max_tokens=10
    )
    print("4. ✅ OpenAI API 调用成功")
    print(f"   响应: {response.choices[0].message.content}")
except Exception as e:
    print(f"4. ❌ OpenAI API 调用失败: {e}")

print("=== 诊断完成 ===")
