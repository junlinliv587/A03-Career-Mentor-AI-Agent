from cache import ResponseCache

class CareerMentorAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model=Config.LLM_MODEL,
            groq_api_key=Config.GROQ_API_KEY,
            temperature=0.7
        )
        self.rag_system = RAGSystem()
        self.cache = ResponseCache()
        
    def generate_roadmap(self, user_profile):
        # Check cache first
        cached_response = self.cache.get(user_profile)
        if cached_response:
            print("✅ Serving from cache")
            return cached_response
        
        # Generate new response if not cached
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
        
        # Cache the response
        self.cache.set(user_profile, response.content)
        return response.content
    
