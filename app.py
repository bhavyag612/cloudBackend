from pathlib import Path

from flask import Flask, jsonify, render_template, request
from random import randint
from database import db
from models import Quote

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


# Route to get a random quote
@app.route("/", methods=["GET"])
def get_quote():
    cursor = Quote.query.all()
    quote=cursor[randint(0,9)]
    return jsonify(quote.to_dict())

if __name__ == '__main__':
    app.run(port=80,host='0.0.0.0')
