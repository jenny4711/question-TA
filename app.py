from flask import Flask,request,render_template,redirect,flash,session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL']='postgresql:///movies_example'

db =SQLAlchemy()
db.app=app
db.init_app(app)

app.config['SECRET_KEY'] = 'chickenzarecod121837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug =DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Show home page"""
    return render_template('home.html')
  

  