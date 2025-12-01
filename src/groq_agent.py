from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from config import Config

class CareerMentorAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model=Config.GROQ_MODEL,
            groq_api_key=Config.GROQ_API_KEY,
            temperature=0.7
        )
        
        self.roadmap_prompt = ChatPromptTemplate.from_template("""
You are an experienced software engineering career mentor. Create a personalized learning roadmap.

Student Background:
- Current Level: {current_level}
- Target Career: {career_goal}
- Study Time: {hours_per_week} hours/week
- Timeline: {timeline_months} months

Create a clear, structured learning plan with phases and practical projects.
Be encouraging and realistic!
""")
    
    def generate_roadmap(self, user_profile):
        roadmap_chain = (
            {
                "current_level": RunnablePassthrough(),
                "career_goal": RunnablePassthrough(), 
                "hours_per_week": RunnablePassthrough(),
                "timeline_months": RunnablePassthrough(),
            }
            | self.roadmap_prompt
            | self.llm
        )
        
        response = roadmap_chain.invoke(user_profile)
        return response.content

def test_agent():
    agent = CareerMentorAgent()
    test_profile = {
        "current_level": "beginner",
        "career_goal": "web development", 
        "hours_per_week": 15,
        "timeline_months": 6
    }
    
    print("🤖 Testing Career Mentor Agent with Groq...")
    roadmap = agent.generate_roadmap(test_profile)
    print("✅ Agent test completed!")
    print("\n" + "="*50)
    print(roadmap)

if __name__ == "__main__":
    test_agent()