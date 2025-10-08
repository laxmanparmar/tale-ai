#!/usr/bin/env python3
"""
Startup script for Tale-AI FastAPI server.
"""

import uvicorn
import os
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open the client HTML file in the default browser."""
    time.sleep(2)  # Wait for server to start
    webbrowser.open('file://' + os.path.realpath('client.html'))

if __name__ == "__main__":
    print("🚀 Starting Tale-AI Server...")
    print("=" * 50)
    print("Server will be available at: http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("Client Interface: client.html")
    print("=" * 50)
    
    # Open browser after a delay
    Timer(2.0, open_browser).start()
    
    # Start the server
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
