from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        "title": "Title 1",
        "author": "Autho 1",
        "date": "12-12-2021",
        "content": "Content 1"
    },
    {
        "title": "Title 2",
        "author": "Author 2",
        "date": "12-12-2021",
        "content": "Content 2"
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)

