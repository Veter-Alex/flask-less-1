from datetime import datetime

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


@app.route("/personal-page")
def personal_page():
    name = "John"
    return render_template("personal-page.html", name=name)


@app.route("/task")
def task():
    curent_time = datetime.now()
    if curent_time.hour < 12:
        greeting = "Доброе утро"
    elif 12 <= curent_time.hour < 18:
        greeting = "Добрый день"
    else:
        greeting = "Добрый вечер"

    tasks = {
        "Задача 1",
        "Задача 2",
        "Задача 3",
    }
    return render_template(
        "task.html", curent_time=curent_time, greeting=greeting, task=tasks
    )


@app.route("/about")
def about():
    return "About"


@app.route("/contact")
def contact():
    return "Contact"


if __name__ == "__main__":
    app.run(debug=True)
