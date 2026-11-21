"""Administrative endpoints."""
from flask import Blueprint

from . import store
from .security import require_role

bp = Blueprint("admin", __name__)


@bp.route("/admin/users/<uid>", methods=["DELETE"])
def delete_user(uid):
    return store.delete(uid)
