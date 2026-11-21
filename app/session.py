"""Reads the session blob the browser sends back."""
import base64
import json
import pickle

from flask import Blueprint, request

bp = Blueprint("session", __name__)


@bp.route("/whoami")
def whoami():
    cookie = request.cookies.get("session_blob", "")
    return {"session": str(load_session(cookie))}


def load_session(cookie):
    raw = base64.b64decode(cookie)
    return pickle.loads(raw)
