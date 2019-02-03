#!flask/bin/python
import sqlite3

from flask import Flask, jsonify, make_response, g, render_template
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
# See important note below
from model import Selection

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["DEBUG"] = True
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

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


@app.route('/api/match/<match_id>', methods=['GET'])
def getmatch(match_id):
    qry = Selection.query.filter_by(id=match_id)
    result = qry.first()

    return jsonify(id=result.id,
            name=result.name,
            odds=result.id)


@app.route('/api/match/?sport=<sport_id>&ordering=<time_now>', methods=['GET'])
def getevent(sport_id,time_now):
    qry = Selection.query.filter_by(id=id)
    album = qry.first()
    #return '[{"id": %r,"content": %r}]' % album.id % album.name
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/match/?name=<match_name>', methods=['GET'])
def getmatchbyname(match_name):
    qry = Selection.query.filter_by(id=id)
    album = qry.first()
    #return '[{"id": {0},"content": {1}}]'.format(album.id,album.name)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


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
    print "New Application"


if __name__ == '__main__':
    app.run(debug=True)