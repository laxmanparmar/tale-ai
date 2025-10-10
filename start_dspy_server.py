#!/usr/bin/env python3
"""
Startup script for Tale-AI DSPy API server.
"""

import uvicorn
import os
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open the API documentation in the default browser."""
    time.sleep(2)  # Wait for server to start
    webbrowser.open('http://localhost:8001/docs')

if __name__ == "__main__":
    print("🚀 Starting Tale-AI DSPy Server...")
    print("=" * 50)
    print("Server will be available at: http://localhost:8001")
    print("API Documentation: http://localhost:8001/docs")
    print("Reasoning Methods: http://localhost:8001/reasoning-methods")
    print("=" * 50)
    print("DSPy Features:")
    print("✅ ChainOfThought reasoning")
    print("✅ Structured story analysis")
    print("✅ Story optimization")
    print("✅ Enhanced agent reasoning")
    print("=" * 50)
    
    # Open browser after a delay
    Timer(2.0, open_browser).start()
    
    # Start the server
    uvicorn.run(
        "dspy_api:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )
