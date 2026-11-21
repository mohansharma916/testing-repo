"""Reachability check used by the status page."""
import os
import subprocess

from flask import Blueprint, request

bp = Blueprint("net_tools", __name__)


@bp.route("/ping")
def ping_host():
    host = request.args.get("host", "127.0.0.1")
    os.system(f"ping -c 1 {host}")
    return {"pinged": host}
