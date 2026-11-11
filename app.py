import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from Controller.instituicaoEnsinoController import instituicao_bp

load_dotenv()

app = Flask(__name__)

CORS(app)

app.register_blueprint(instituicao_bp)


@app.route("/")
def index():
    return {
        "versao": "0.0.1"
    }, 200


@app.route("/health")
def health():
    return {
        "health": "ok"
    }, 200


def main(arg=[]):
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug)