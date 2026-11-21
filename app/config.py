"""Configuration for the demo app."""
import os

DATABASE = os.environ.get("DEMO_DB", "/tmp/staf-sast-demo.db")
UPLOAD_DIR = os.environ.get("DEMO_UPLOADS", "/tmp/staf-sast-demo-uploads")
BASE_DIR = os.path.join(os.path.dirname(__file__), "data")
SECRET_KEY = "dev-secret-123"
ALLOWED_EXT = {"png", "jpg", "pdf"}
ALLOWED_HOSTS = {"hooks.example.com"}
