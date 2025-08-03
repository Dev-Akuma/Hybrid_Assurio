from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from .routes.query_router import router as query_router
from .routes.upload_router import router as upload_router

# Create FastAPI app
app = FastAPI(
    title="ClauseMind Cloud - Intelligent Clause Retriever & Decision System",
    description="""
    🧠 **ClauseMind Cloud** - An intelligent system that uses LLM-powered semantic search to retrieve relevant clauses from insurance documents and provide automated decision-making with cloud storage.

    ## Features:
    - Cloud Document Upload (Cloudinary)
    - Auto Indexing (Embeddings + Pinecone)
    - Semantic Search & LLM Reasoning (Gemini)
    - Entity Extraction from Natural Language Queries
    - Cloud Deployment Ready (Render/Vercel)

    ## Pipeline:
    1. PDF Upload → Cloudinary
    2. Text Extraction & Chunking → Local
    3. Query → Entity Extraction
    4. Query Embedding → Pinecone Vector Search
    5. Retrieved Clauses → Gemini LLM
    6. Output → Decision + Justification
    """,
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hybrid-assurio.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(query_router, prefix="/api/v1", tags=["ClauseMind API"])
app.include_router(upload_router, prefix="/api/v1", tags=["Document Upload"])

# API info endpoint
@app.get("/api/v1", response_class=JSONResponse)
async def api_info():
    return {
        "api_name": "ClauseMind Cloud API",
        "version": "2.0.0",
        "architecture": "cloud-native",
        "endpoints": {
            "health": "GET /api/v1/health",
            "upload": "POST /api/v1/upload_pdf",
            "upload_async": "POST /api/v1/upload_pdf_async",
            "query": "POST /api/v1/query",
            "documents": "GET /api/v1/documents",
            "vector_stats": "GET /api/v1/vector_stats"
        },
        "features": [
            "Cloud PDF upload & processing",
            "Semantic clause retrieval (Pinecone)",
            "LLM decision making (Gemini)",
            "Entity extraction",
            "Ready for Vercel/Render"
        ],
        "storage": {
            "files": "Cloudinary",
            "vectors": "Pinecone",
            "embeddings": "SentenceTransformers / Hugging Face API"
        }
    }

# Run locally
if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
