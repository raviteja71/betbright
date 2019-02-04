from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sport(db.Model):
    """
    model for table sport

    Fields: id (int),name (string)

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Sport Name %r>' % self.name


class Selection(db.Model):
    """
    model for table selection

    Fields: id (int),name (string),odds(float),market_id(represents table market object)

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    odds = db.Column(db.Float, nullable=False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __repr__(self):
        return '<Selection %r>' % self.name


class Market(db.Model):
    """
    model for table sport

    Fields: id (int),name (string)

    relationships: selections - one-to-many relationship with 'selection' table

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    selections = db.relationship('Selection',  backref='Market', lazy='dynamic')

    def __init__(self, name,selections=[]):
        self.name = name
        self.selections=selections

    def __repr__(self):
        return '{ "name":"%r"}' % self.name


class Event(db.Model):
    """
    model for table event

    Fields: id (int),name (string),url(string),start_time,(date), market_id(represents table market object)

            Market - one-to-one relationship with table 'event'
            Sport - one-to-one relationship with table 'sport'

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=True, nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'))
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)
    market = db.relationship('Market', uselist=False, backref="image")
    Market = db.relationship("Market", backref=db.backref("Event", uselist=False))
    Sport = db.relationship("Sport", backref=db.backref("Event", uselist=False))

    def __init__(self, name, url, sport_id, market_id):
        self.name = name
        self.market_id = market_id
        self.url = url
        self.sport_id = sport_id

    def __repr__(self):
        return '<event %r>' % self.name


class Message(db.Model):
    """
    model for table message

    Fields: id (int),message_type (string (new, update)), event'(TEXT - contains full event info)

    """
    id = db.Column(db.Integer, primary_key=True)
    message_type = db.Column(db.String(250), nullable=False)
    event = db.Column(db.Text, nullable=False)

    def __init__(self, message_type, event):
        self.message_type = message_type
        self.event = event

    def __repr__(self):
        return '<message %r>' % self.id

#db statements to add tables and commit
db.create_all()
db.session.commit()