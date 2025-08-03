#!/usr/bin/env python3
"""
Enhanced ClauseMind - Startup Script
Run this script to start the enhanced ClauseMind application with PDF upload functionality
"""

import os
import sys
import subprocess
from pathlib import Path

def check_env_file():
    """Check if .env file exists and has required variables"""
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file not found. Creating default...")
        env_content = """# ClauseMind Configuration
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_NAME=gemini-pro
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RETRIEVAL=5
"""
        env_file.write_text(env_content)
        print("✅ .env created. Please update GEMINI_API_KEY before deploying.")
        return False

    content = env_file.read_text()
    if 'your_gemini_api_key_here' in content:
        print("⚠️  Please update GEMINI_API_KEY in your .env file.")
        return False

    print("✅ Environment configuration OK.")
    return True

def create_directories():
    """Create necessary directories"""
    for d in ['data', 'data/uploads']:
        Path(d).mkdir(parents=True, exist_ok=True)
    print("✅ Required directories created.")

def start_server():
    """Start FastAPI server via Uvicorn"""
    print("🚀 Starting Enhanced ClauseMind backend server...")
    subprocess.run([
        sys.executable, "-m", "uvicorn",
        "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])

def main():
    print("🧠 Enhanced ClauseMind - Startup Sequence")
    if not check_env_file():
        return
    create_directories()
    start_server()

if __name__ == "__main__":
    main()
