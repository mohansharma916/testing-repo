"""User lookup and search endpoints."""
from flask import Blueprint, render_template, request

from . import store

bp = Blueprint("data", __name__)


@bp.route("/user")
def get_user():
    username = request.args.get("username", "")
    cursor = store.connect().cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return {"rows": cursor.fetchall()}


@bp.route("/search")
def search():
    return render_template("search.html", term=request.args.get("term", ""))
