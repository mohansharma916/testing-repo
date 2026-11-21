"""Serves the bundled data files."""
import os

from flask import Blueprint, abort, request

from .config import BASE_DIR

bp = Blueprint("files", __name__)


@bp.route("/read")
def read_file():
    name = request.args.get("name", "notes.txt")
    with open(os.path.join(BASE_DIR, name)) as fh:
        return fh.read()
