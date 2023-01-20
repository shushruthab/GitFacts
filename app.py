from flask import Flask, render_template, request
from gitfacts import git_facts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        git_repo = request.form["git_repo"]
        items = git_facts(git_repo)
        print(items)
        return render_template("index.html", items=items)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
