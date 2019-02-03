#!flask/bin/python
import sqlite3

from flask import Flask, jsonify, make_response, g, render_template
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
# See important note below

from model import Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["DEBUG"] = True
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

DATABASE = '/home/raviteja/betbright/betBright.db'


def get_db():
    """
    Establishes database connection

    Connecting to sqlite databse.

    Returns:
    object: db
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    # Call the service to close the connection after db work is completed
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/api/match/<match_id>', methods=['GET'])
def getmatch(match_id):
    """
    Rest Api call for matches.

    provide the match details based on passed match ID.

    Parameters:
    match_id (int): primary key for the match table row

    Returns:
    json object: contains the full details of the match

    """
    try:
        u = Event.query.get(match_id)
        selections = []

        for sel in u.Market.selections:
            item = {"id": sel.id, "name": sel.name, "odds": sel.odds}
            selections.append(item)

        markets = [{"id": u.Market.id, "name": u.Market.name, "selection": selections}]
        sports = [{"id": u.Sport.id, "name": u.Sport.name}]
    except:
        # If the response contains an error, I should get this.
        return jsonify(error="Something went wrong")

    # jsonified response for final result
    return jsonify(id=u.id,
                   name=u.name,
                   url=u.url,
                   start_time=u.start_time,
                   markets=markets,
                   sports=sports)


@app.route('/api/match/sport=<sport_id>/ordering=<time_now>', methods=['GET'])
def getRecentevent(sport_id, time_now):
    """
    Rest Api call for matches.

    provide the match details based on passed sport ID and orders by start time.

    Parameters:
    sport_id (int): primary key for the sports table and using as foreign key in  events table
    time_now (date): date of the event

    Returns:
    json object: contains the full details of the match

    """
    try:
        eventres = query_db('select id,name,url, start_time from event order by ' + time_now)
        events = []
        # iterate whole events as parse as a json string.
        for event in eventres:
            item = {"id": event[0], "name": event[1], "url": event[2], "Start Time": event[3]}
            events.append(item)
    except:
        # If the response contains an error, I should get this.
        return jsonify(error="Something went wrong")

    # jsonified response for final result
    return make_response(jsonify({'results': events}))


@app.route('/api/match/name=<match_name>', methods=['GET'])
def getmatchbyname(match_name):
    """
        Rest Api call for matches.

        provide the match details based on passed name string.

        Parameters:
        match_name (string): name of the match in events table

        Returns:
        json object: contains the full details of the match

        """
    try:
        qry = Event.query.filter_by(name=match_name)
        result = qry.first()
    except:
        # If the response contains an error, I should get this.
        return jsonify(error="Something went wrong")

    # jsonified response for final result
    return jsonify(id=result.id,
                   name=result.name,
                   url=result.url,
                   start_time=result.start_time)


def query_db(query, args=(), one=False):
    # The method is used to interact with the database object
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.errorhandler(400)
def bad_request(error):
    # Call the service handiling bad formation of the url internlly.
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    # Call the service handiling 404 error internlly.
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    # Index page for the flask application
    print "New Application for betBright"


if __name__ == '__main__':
    app.run(debug=True)
