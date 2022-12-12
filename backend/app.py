from flask import Flask, request
from urllib.parse import urlparse

from api.v1 import loan

app = Flask(__name__)

# APIs
api_prefix = "/api/v1"

app.register_blueprint(loan.blueprint, url_prefix=api_prefix + "/loan")


@app.route("/")
def home():
    return "Hello-World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
