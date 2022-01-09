"""This is a deliberately vulnerable class for testing."""
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/xss")
def xss():
    """Reflect the request query parameter without sanitization."""
    username = request.args.get("username")
    return make_response(f"Hello {username}")
