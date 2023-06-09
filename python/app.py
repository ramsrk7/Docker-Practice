from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# 

if __name__ == '__main__':
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']

db = SQLAlchemy(app)

# Model 1
class Items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))

    def __init__(self, title, content):
        self.title = title
        self.content = content

db.create_all()

@app.route("/", methods=['GET'])
def get():
    return "OK! Hello from Python!"

#Create Item

@app.route("/item", methods=['POST'])
def itemadd():
    body = request.get_json()
    title = body['title']
    content = body['content']

    db.session.add(Items(title, content))
    db.session.commit()

    return "All Good"


