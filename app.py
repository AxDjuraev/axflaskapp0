
from flask import Flask

app = Flask(__main__)
@app.route('/')
def home():
  content = f'hello, again'
  return content

if __name__ == '__main__':
  app.run()
