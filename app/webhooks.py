"""Relays an event to a caller-supplied callback."""
import json
import urllib.request
from urllib.parse import urlparse

from flask import Blueprint, abort, request

from .config import ALLOWED_HOSTS

bp = Blueprint("webhooks", __name__)


@bp.route("/relay", methods=["POST"])
def relay():
    payload = request.get_json(force=True, silent=True) or {}
    body = {"event": payload.get("event", "ping")}
    target = payload["callback_url"]
    post = urllib.request.Request(target, data=json.dumps(body).encode(), method="POST")
    with urllib.request.urlopen(post, timeout=5) as response:
        return {"status": response.status}
