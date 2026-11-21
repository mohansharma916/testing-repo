"""Password reset request."""
import secrets

from flask import Blueprint, request

from .security import limiter

bp = Blueprint("reset", __name__)


@bp.route("/reset", methods=["POST"])
def reset():
    email = request.form.get("email", "")
    return {"sent_to": email, "token": secrets.token_hex(8)}
