
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__, template_folder='templates')
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
database = SQLAlchemy(application)

class Pet(database.Model):
  id = database.Column(database.Integer, primary_key = True)
  name = database.Column(database.String(200), nullable = False)
  age = database.Column(database.Integer, nullable = False)

  def __repr__(self):
    return '<Pet %r>' % self.id

@application.route("/")
def main():
  content = render_template('index.html')
  return content 

@application.route("/pets-market/")
def home():
  content = render_template('pets_market.html')
  return content 

@application.route("/pets-market/delete/")
def home():
  content = render_template('delete_pets.html')
  return content 

@application.route("/pets-market/add/")
def home():
  content = render_template('add_pets.html')
  return content 

if __name__ == '__main__':
  application.run(debug=True)
