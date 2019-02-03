from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Sport Name %r>' % self.name


class Selection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    odds = db.Column(db.Float, unique=True, nullable=False)

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __repr__(self):
        return '<Selection %r>' % self.name


class market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    selection = db.Column(db.Integer, db.ForeignKey('rel_market_selection.market_id'), nullable=False)

    def __init__(self, name, selection):
        self.name = name
        self.selection = selection

    def __repr__(self):
        return '{ "name":"%r"}' % self.name

class rel_market_selection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    market_id = db.Column(db.Integer,  nullable=False)
    selection_id = db.Column(db.Integer, nullable=False)
    def __init__(self, name, selection):
        self.name = name
        self.selection = selection
    def __repr__(self):
        return '{ "name":"%r"}' % self.name

class event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    markets = db.Column(db.Integer, db.ForeignKey('market.id'), nullable=False)
    def __init__(self, name, markets):
        self.name = name
        self.markets = markets
    def __repr__(self):
        return '<event %r>' % self.name
class message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_type = db.Column(db.String(250), unique=True, nullable=False)
    event = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    def __init__(self, message_type, event):
        self.message_type = message_type
        self.event = event
    def __repr__(self):
        return '{ "name":"%r", "age":%r, "city":"%r"}' % self.name, self.message_type, self.event

db.create_all()
db.session.commit()


