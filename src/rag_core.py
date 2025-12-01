from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from config import Config
from sample_data import get_sample_resources

class RAGSystem:
    """RAG system for retrieving learning resources."""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
        
        # Initialize vector database with sample data
        self.vector_db = Chroma(
            persist_directory=Config.CHROMA_DB_PATH,
            embedding_function=self.embeddings
        )
        
        # Add sample resources if database is empty
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize the vector database with sample learning resources."""
        try:
            # Check if database already has data
            existing_count = self.vector_db._collection.count()
            if existing_count == 0:
                sample_docs = get_sample_resources()
                self.vector_db.add_documents(sample_docs)
                print(f"✅ Initialized database with {len(sample_docs)} sample resources")
            else:
                print(f"✅ Database already has {existing_count} resources")
        except Exception as e:
            print(f"⚠️ Database initialization note: {e}")
    
    def retrieve_resources(self, query: str, k: int = Config.RETRIEVE_COUNT):
        """Retrieve relevant learning resources based on query."""
        try:
            retriever = self.vector_db.as_retriever(search_kwargs={"k": k})
            relevant_docs = retriever.get_relevant_documents(query)
            return relevant_docs
        except Exception as e:
            print(f"❌ Error retrieving resources: {e}")
            # Fallback to sample resources
            return get_sample_resources()[:k]

