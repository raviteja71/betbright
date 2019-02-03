from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# See important note below
from model import Market
from model import Selection
from model import Event
from model import Message
from model import Sport

s1 = Selection(name="Poland",odds=3.01)
s2 = Selection(name="Irland",odds=7.01);
m1 = Market(name="Winner",selections=[s1,s2])

ev1 = Event("Poland vs Irland","http://example.com/api/match/2",2,1)


db.session.add(m1)
db.session.add(s1)
db.session.add(s2)
db.session.add(ev1)
db.session.commit()
