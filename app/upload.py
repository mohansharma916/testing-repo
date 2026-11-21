"""File upload endpoint."""
import os

from flask import Blueprint, abort, request

from .config import ALLOWED_EXT, UPLOAD_DIR

bp = Blueprint("upload", __name__)


@bp.route("/upload", methods=["POST"])
def upload():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ext = request.files["f"].filename.split(".")[-1]
    request.files["f"].save(os.path.join(UPLOAD_DIR, f"upload.{ext}"))
    return {"saved": f"upload.{ext}"}
