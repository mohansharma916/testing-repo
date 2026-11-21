"""Outbound call to the upstream service."""
import logging

from flask import Blueprint, request

from .security import redact

bp = Blueprint("client", __name__)
log = logging.getLogger(__name__)


@bp.route("/upstream")
def call_upstream():
    token = request.headers.get("Authorization", "")
    log.info("calling upstream with token=%s", token)
    return {"called": True}
