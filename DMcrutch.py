from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/stats")
def stats():
    return "<p>Hello, stats!</p>"

@app.route("/notes")
def notes():
    return "<p>Hello, notes!</p>"

@app.route("/combat")
def combat():
    return "<p>Hello, combat!</p>"

@app.route("/dictionary")
def dictionary():
    return "<p>Hello, dictionary!</p>"

@app.route("/about")
def about():
    return "<p>Hello, about!</p>"

if __name__ == '__main__':
    app.run(debug=True)