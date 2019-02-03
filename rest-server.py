#!flask/bin/python
import sqlite3

from flask import Flask, jsonify, make_response, g, render_template
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    entries = query_db('select id,message_type,event from message')
    return render_template('show_results.html', entries=entries)

DATABASE = '/home/raviteja/betbright/betBright.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# See important note below
from model import market

@app.route('/api/match/<match_id>')

def getmatch(match_id):
    qry = market.query.filter_by(id=match_id)
    album = qry.first()
    print album.name
    return '[{"id": %r,"content": %r}]'.format(1, 2)

@app.route('/api/match/?sport=<sport_id>&ordering=<time_now>')
def getevent(sport_id,time_now):
    qry = market.query.filter_by(id=id)
    album = qry.first()
    return '[{"id": %r,"content": %r}]' % album.id % album.name

@app.route('/api/match/?name=<match_name>')
def getmatchbyname(match_name):
    qry = market.query.filter_by(id=id)
    album = qry.first()
    return '[{"id": {0},"content": {1}}]'.format(album.id,album.name)

if __name__ == '__main__':
    app.run(debug=True)