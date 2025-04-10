import sys
import os

# Add the parent directory (task_app) to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import create_app from the app module
from app import create_app

# Create and run the app
app = create_app()
app.run(debug=True)
