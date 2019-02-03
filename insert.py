from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/raviteja/betbright/betBright.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# See important note below
from model import market

db.create_all()
db.session.commit()

firstrow = market("Real Madrid",385086549360973392)
secondrow = market("Barcelona",385086549360973392)
db.session.add(firstrow)
db.session.add(secondrow)
db.session.commit()
rows = market.query.all()
print rows
