import os
import sys
import asyncio
from web_server import create_app, start_web_server

# WSGI/ASGI application factory / instance for deployment runners (Render / Gunicorn)
app = create_app()

def get_app():
    """Application factory for cloud runners."""
    return app

if __name__ == "__main__":
    host = os.getenv("WEB_HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 10000))
    try:
        asyncio.run(start_web_server(host=host, port=port))
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
