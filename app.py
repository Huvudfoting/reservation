from flask import Flask, jsonify, Response
from dataclasses import asdict

from NamePool import NamePool
from name_generator import build_names

app = Flask(__name__)

available = build_names()
pool = NamePool(available)


@app.route("/", methods=['GET'])
def size() -> str:
    return str(pool.size())


@app.route("/draw/<int:amount>", methods=['GET'])
def draw(amount: int) -> list[str]:
    return pool.draw(amount)


@app.route("/reserve/<name>", methods=['GET'])
def reserve(name: str) -> Response:
    reservation = pool.reserve(name)
    return jsonify(asdict(reservation))


@app.route("/reserve/undo/<name>/<secret>", methods=['GET'])
def undo_reserve(name: str, secret: str) -> Response:
    pool.undo_reserve(name, secret)
    return Response(status=204)


@app.route("/reserve/confirm/<name>/<secret>", methods=['GET'])
def confirm_reserve(name: str, secret: str) -> Response:
    reservation = pool.confirm_reserve(name, secret)
    return jsonify(asdict(reservation))


@app.route("/list-reserved", methods=['GET'])
def list_reserved() -> Response:
    return jsonify(list(pool.reserved.keys()))
