import uvicorn
import os
import sys

# Ensure backend directory is in python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # We can't import settings at module level if we want to support running from root or backend
    # but since this is inside backend, let's try to be robust.
    try:
        from app.config import settings
        uvicorn.run(
            "app.main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG
        )
    except ImportError as e:
        print(f"Error importing app: {e}")
        print("Make sure you are running from the correct directory or have dependencies installed.")
