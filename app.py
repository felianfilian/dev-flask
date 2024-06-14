from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://db.db'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
db = SQLAlchemy(app)

class MEssage(db.model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def hello():
    return "Super Mario"

if __name__ == '__main__':
    app.run(debug=True)
