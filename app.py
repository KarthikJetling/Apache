from flask import Flask, render_template, url_for
import apache as a

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', res = a.apache())

if __name__ == "__main__":
    app.run(debug = True)
