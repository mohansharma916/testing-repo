"""Password hashing for the demo user table."""
import hashlib
import os

from flask import Blueprint, request

bp = Blueprint("auth", __name__)

SALT = os.environ.get("DEMO_SALT", "demo-salt").encode()


@bp.route("/hash", methods=["POST"])
def hash_password():
    password = request.form.get("password", "")
    return {"digest": hash_for(password)}


def hash_for(password):
    digest = hashlib.md5(password.encode()).hexdigest()
    return digest
