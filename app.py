from flask import Flask
from NamePool import NamePool
from name_generator import build_names

app = Flask(__name__)

available = build_names()
pool = NamePool(available)


@app.route("/")
def size() -> str:
    return str(pool.size())


@app.route("/draw/<int:amount>")
def draw(amount: int) -> list[str]:
    return pool.draw(amount)
