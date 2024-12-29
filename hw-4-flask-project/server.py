from flask import Flask
from flask import jsonify
from dotenv import dotenv_values
from flask import request
from controllers import operation

app = Flask(__name__)


@app.route("/")
def server_info():
    return "My server"


@app.route("/author")
def author():
    author = {
        "name": "Mushkat Ilya",
        "course": 2,
        "age": 19,
    }
    return jsonify(author)


# @app.route("/sum")
# def runner():
#     a = request.args.get('a', type=int)
#     b = request.args.get('b', type=int)
#     return jsonify({'sum': a + b})


@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
