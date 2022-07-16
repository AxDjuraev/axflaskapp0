
from flask import Flask, render_template, url_for, request, redirect
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
def pets_market():
  pets = Pet.query.order_by(Pet.name).all()
  content = render_template('pets_market.html', pets = pets)
  return content 

@application.route("/pets-market/delete/", methods=['GET', 'POST'])
def pets_market_delete():
  content = render_template('delete_pets.html')
  return content 

@application.route("/pets-market/add/", methods=['GET', 'POST'])
def pets_market_add():
  if request.method == 'POST':
    try:
      pet_name = request.form['pet_name']
      pet_age = request.form['pet_age']
      pet = Pet(name = pet_name, age = pet_age)
      
      database.session.add(pet)
      database.session.commit()
      return redirect('/pets-market/')
    except Exception as exception:
      return f'Error: {str(exception)}'
  content = render_template('add_pets.html')
  return content 

if __name__ == '__main__':
  application.run(debug=True)
