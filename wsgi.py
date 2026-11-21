"""Entry point: python -m flask --app wsgi run --port 8181"""
from app import create_app

app = create_app()
