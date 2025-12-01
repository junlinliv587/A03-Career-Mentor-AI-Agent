import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from groq_agent import CareerMentorAgent

def main():
    st.set_page_config(
        page_title="Career Mentor AI Agent",
        page_icon="🚀",
        layout="wide"
    )
    
    st.title("🚀 Career Mentor AI Agent")
    st.markdown("### Get your personalized learning roadmap for tech careers!")
    
    with st.form("user_input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            current_level = st.selectbox(
                "What's your current level?",
                ["Beginner", "Some programming experience", "Career switcher with other experience"]
            )
            career_goal = st.selectbox(
                "What's your target career?",
                ["Web Development", "Data Science", "Mobile Development", "DevOps", "Full-Stack Development"]
            )
        
        with col2:
            hours_per_week = st.slider(
                "Weekly study hours",
                min_value=5,
                max_value=40,
                value=15,
                help="How many hours can you study per week?"
            )
            timeline_months = st.slider(
                "Target timeline (months)",
                min_value=3,
                max_value=24,
                value=6,
                help="When do you want to be job-ready?"
            )
        
        submitted = st.form_submit_button("Generate My Learning Roadmap! 🎯")
    
    if submitted:
        with st.spinner("🤖 AI is creating your personalized learning roadmap..."):
            agent = CareerMentorAgent()
            
            user_profile = {
                "current_level": current_level,
                "career_goal": career_goal,
                "hours_per_week": hours_per_week,
                "timeline_months": timeline_months
            }
            
            roadmap = agent.generate_roadmap(user_profile)
            
            st.success("✅ Your personalized learning roadmap is ready!")
            st.markdown("---")
            st.markdown(roadmap)
            
            # Download button
            st.download_button(
                label="📥 Download Roadmap",
                data=roadmap,
                file_name=f"learning_roadmap_{career_goal.replace(' ', '_')}.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
    