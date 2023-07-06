import os

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app: Flask = Flask(__name__)


@app.route("/")
def hello_world() -> None:
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.getenv("APP_HOST"), port=os.getenv("APP_PORT"), debug=False)
