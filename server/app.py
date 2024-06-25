#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():

    session['page_views'] = session.get('page_views', 0)

@app.route('/articles/<int:id>')
def view_article(id):
    session['page_views'] = session.get('page_views', 0) + 1

    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    article_data = {
        'id': id,
        'author': 'John Doe',
        'title': f'Article {id}',
        'content': 'Content of the article.',
        'preview': 'Preview of the article.',
        'minutes_to_read': 5,
        'date': '2024-06-25'
    }
    return jsonify(article_data)

if __name__ == '__main__':
    app.run(port=5555)
