
from flask import Flask, render_template, url_for

application = Flask(__name__, template_folder='templates')
@application.route("/")
def home():
  content = render_template('index.html')
  return content 

if __name__ == '__main__':
  application.run(debug=True)
