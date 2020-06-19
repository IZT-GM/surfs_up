# Import flask
from flask import Flask

# Create instance
app = Flask(__name__)

# Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/index')
def index():
    return 'This should be the index'

@app.route('/part_1')
def part_1():
    return 'This is Part I'

if __name__ == "__main__":
    app.run(debug=True)