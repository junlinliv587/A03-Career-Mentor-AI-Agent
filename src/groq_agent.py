from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from config import Config
from rag_core import RAGSystem

class CareerMentorAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model=Config.LLM_MODEL,
            groq_api_key=Config.GROQ_API_KEY,
            temperature=0.7
        )
        self.rag_system = RAGSystem()
        
        self.roadmap_prompt = ChatPromptTemplate.from_template("""
You are an experienced software engineering career mentor. Create a personalized learning roadmap.

## Student Background:
- Current Level: {current_level}
- Target Career: {career_goal}
- Study Time: {hours_per_week} hours/week
- Timeline: {timeline_months} months

## Recommended Learning Resources:
{resources}

Create a clear, structured 4-phase learning plan with:
1. Phase titles and durations
2. Key learning objectives  
3. Recommended resources from the list above
4. Practical projects
5. Progress checkpoints

Be encouraging and realistic!
""")
    
    def generate_roadmap(self, user_profile):
        # Retrieve relevant resources
        query = f"{user_profile['career_goal']} {user_profile['current_level']}"
        resources = self.rag_system.retrieve_resources(query)
        resources_text = "\n".join([f"- {doc.page_content}" for doc in resources])
        
        roadmap_chain = (
            {
                "current_level": RunnablePassthrough(),
                "career_goal": RunnablePassthrough(), 
                "hours_per_week": RunnablePassthrough(),
                "timeline_months": RunnablePassthrough(),
                "resources": RunnablePassthrough()
            }
            | self.roadmap_prompt
            | self.llm
        )
        
        response = roadmap_chain.invoke({
            **user_profile,
            "resources": resources_text
        })
        return response.content
    
