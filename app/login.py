"""Login and the post-login redirect."""
from flask import Blueprint, redirect, request

from .security import safe_next

bp = Blueprint("login", __name__)


@bp.route("/login", methods=["POST"])
def login():
    # The demo accepts any credentials; only the redirect matters here.
    return redirect(safe_next(request.args.get("return_to", "/"), "/"))
