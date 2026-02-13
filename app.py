from flask import Flask, render_template, request
from main_logic import analyze_poem

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    output = None

    if request.method == "POST":
        poem = request.form["poem"]
        output = analyze_poem(poem)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
