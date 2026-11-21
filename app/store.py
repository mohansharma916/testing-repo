"""The SQLite table the lookup endpoints read."""
import sqlite3

from . import config


def connect():
    return sqlite3.connect(config.DATABASE)


def init():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, email TEXT, role TEXT)")
        db.executemany("INSERT OR REPLACE INTO users VALUES (?, ?, ?)", [
            ("alice", "alice@example.com", "admin"),
            ("bob", "bob@example.com", "user"),
        ])


def delete(uid):
    with connect() as db:
        db.execute("DELETE FROM users WHERE username = ?", (uid,))
    return {"deleted": uid}
