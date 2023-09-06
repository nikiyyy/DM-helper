from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/stats")
def stats():
    return render_template('stats.html')

@app.route("/notes")
def notes():
    return render_template('notes.html')

@app.route("/combat")
def combat():
    return render_template('combat.html')

@app.route("/dictionary")
def dictionary():
    return render_template('dictionary.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)