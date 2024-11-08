from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # получает name из url
    name = request.args.get("name")
    # если name == None или name == "null" то name = "Guest"
    if name is None or name == "null":
        name = "Guest"
    # текущее время
    curent_time = datetime.now()
    # доброе утро, добрый день, добрый вечер
    if curent_time.hour < 12:
        greeting = "Доброе утро"

    elif 12 <= curent_time.hour < 18:
        greeting = "Добрый день"
    else:
        greeting = "Добрый вечер"

    # задачи
    match greeting:
        case "Доброе утро":
            tasks = ["Подъем 7:00", "Зарядка 7:30-8:00", "Завтрак 8:30"]
        case "Добрый день":
            tasks = ["Обед 13:00", "Дневной сон 14:00-16:00", "Обучение 16:00-18:00"]
        case "Добрый вечер":
            tasks = ["Тренировка 19:00-20:00", "Ужин 20:30", "Чтение книги 21:00"]

    # возвращаем шаблон
    return render_template(
        "index.html",
        name=name,
        curent_time=curent_time.strftime("%H:%M:%S"),
        greeting=greeting,
        task=tasks,
    )


@app.route("/about")
def about():
    return "About"


@app.route("/contact")
def contact():
    return "Contact"


if __name__ == "__main__":
    app.run(debug=True)
