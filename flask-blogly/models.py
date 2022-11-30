"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

DEFAULT_IMAGE_URL = "https://e7.pngegg.com/pngimages/643/996/png-clipart-leadership-graphics-computer-icons-illustration-organizational-development-learning.png"


def connect_db(app):
  db.app=app
  db.init_app(app)
  
class User(db.Model):
    __tablename__ ='user' 
  
    
  # def __repr__(self):
  #   s=self
  #   return f"<User first_name={s.first_name},last_name={s.last_name}"    
  
  
  
    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
      
    first_name= db.Column(db.Text,
                      nullable=False,
                      unique=True)
      
    last_name= db.Column(db.Text,
                      nullable=False,
                      unique=True)
  
    image_url= db.Column(db.Text,
                      nullable=False,
                      default= DEFAULT_IMAGE_URL)
    

  
