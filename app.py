
from flask import Flask

application = Flask(__name__, template_folder='templates')
@application.route("/")
def home():
  content = f'hello, again'
  return content

if __name__ == '__main__':
  application.run()
