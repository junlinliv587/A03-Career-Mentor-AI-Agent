# src/models.py
from pydantic import BaseModel

class UserProfile(BaseModel):
    """Data model for user profile information."""
    current_level: str
    career_goal: str  
    hours_per_week: int
    timeline_months: int

class LearningResource(BaseModel):
    """Data model for learning resources."""
    title: str
    url: str
    description: str
    tags: list[str]
    difficulty: str  # beginner, intermediate, advanced