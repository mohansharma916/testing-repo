"""Helpers the remediated code uses: roles, redaction, safe redirects, limits."""
import functools
import time
from urllib.parse import urlparse

from flask import abort, request


def current_role():
    """The demo trusts a header, which is enough to show the role check working."""
    return request.headers.get("X-Demo-Role", "user")


def require_role(role):
    def decorate(view):
        @functools.wraps(view)
        def guard(*args, **kwargs):
            if current_role() != role:
                abort(403)
            return view(*args, **kwargs)
        return guard
    return decorate


def redact(secret):
    text = str(secret or "")
    return text[:4] + "***" if text else "***"


def safe_next(target, fallback):
    """Only same-site paths are safe redirect targets."""
    parsed = urlparse(str(target or ""))
    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
        return fallback
    return parsed.path


class Limiter:
    """A fixed-window counter, per client address and endpoint."""

    def __init__(self):
        self.hits = {}

    def limit(self, count, per_seconds):
        def decorate(view):
            @functools.wraps(view)
            def guard(*args, **kwargs):
                key = (request.remote_addr, view.__name__)
                window = int(time.time() / per_seconds)
                seen, at = self.hits.get(key, (0, window))
                seen = seen + 1 if at == window else 1
                self.hits[key] = (seen, window)
                if seen > count:
                    abort(429)
                return view(*args, **kwargs)
            return guard
        return decorate


limiter = Limiter()
