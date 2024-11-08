from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    message = "Тестовая страница"
    return render_template("index.html", message=message)


# http://127.0.0.1:5000/user/John
# страница с динамическим параметром
# можно использовать для персонализации страниц
@app.route("/user/<name>")
def user(name):
    return f"User: {name}"


@app.route("/about")
def about():
    return "About"


@app.route("/contact")
def contact():
    return "Contact"


if __name__ == "__main__":
    app.run(debug=True)
