from groq_agent import CareerMentorAgent

def run_demo():
    print("🎯 Career Mentor AI Agent - Demo")
    print("=" * 50)
    
    # Test case 1: Beginner Web Developer
    print("\n1. Testing: Beginner → Web Development (6 months)")
    agent = CareerMentorAgent()
    
    test_profile_1 = {
        "current_level": "Beginner",
        "career_goal": "Web Development", 
        "hours_per_week": 15,
        "timeline_months": 6
    }
    
    roadmap_1 = agent.generate_roadmap(test_profile_1)
    print("✅ Roadmap generated successfully!")
    print(f"📝 Length: {len(roadmap_1)} characters")
    
    # Test case 2: Career Switcher to Data Science
    print("\n2. Testing: Experienced → Data Science (12 months)")
    
    test_profile_2 = {
        "current_level": "Some programming experience",
        "career_goal": "Data Science", 
        "hours_per_week": 10,
        "timeline_months": 12
    }
    
    roadmap_2 = agent.generate_roadmap(test_profile_2)
    print("✅ Second roadmap generated successfully!")
    print(f"📝 Length: {len(roadmap_2)} characters")
    
    print("\n🎉 Demo completed! All systems working correctly.")
    print("\nTo run the web interface: streamlit run app.py")

if __name__ == "__main__":
    run_demo()
    