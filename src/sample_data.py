from langchain_core.documents import Document

def get_sample_resources():
    """Create sample learning resources for the RAG system."""
    resources = [
        Document(
            page_content="FreeCodeCamp: Complete Web Development Bootcamp - Free comprehensive curriculum covering HTML, CSS, JavaScript, and frameworks. Includes hands-on projects.",
            metadata={
                "title": "FreeCodeCamp Web Dev",
                "url": "https://www.freecodecamp.org/learn",
                "difficulty": "beginner",
                "type": "interactive",
                "tags": "web development, html, css, javascript, free"
            }
        ),
        Document(
            page_content="The Odin Project: Full Stack JavaScript - Project-based curriculum teaching full-stack JavaScript development with Node.js and React.",
            metadata={
                "title": "The Odin Project",
                "url": "https://www.theodinproject.com/",
                "difficulty": "beginner",
                "type": "project-based", 
                "tags": "javascript, node.js, react, fullstack, free"
            }
        ),
        Document(
            page_content="MDN Web Docs: JavaScript Guide - Mozilla's official JavaScript documentation and tutorials. Comprehensive reference for all levels.",
            metadata={
                "title": "MDN JavaScript Guide",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
                "difficulty": "all levels",
                "type": "documentation",
                "tags": "javascript, documentation, reference, mozilla"
            }
        )
    ]
    return resources
