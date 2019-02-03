from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# See important note below
from model import Market
from model import Selection
from model import Event


s1 = Selection(name="Real Madrid",odds=1.01);
s2 = Selection(name="Barcelona",odds=1.01);
m1 = Market(name="Winner",selections=[s1,s2])

ev1 = Event("Real Madrid vs Barcelona","http://example.com/api/match/994839351740",1,1)

db.session.add(m1)
db.session.add(s1)
db.session.add(s2)
db.session.add(ev1)
db.session.commit()
