
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
  content = f'hello, again'
  return content

if __name__ == '__main__':
  app.run()
