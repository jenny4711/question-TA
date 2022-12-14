"""Blogly application."""

from flask import Flask,request,render_template,redirect,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecod121837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug =DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def home():
  
  return render_template('home.html')



 
