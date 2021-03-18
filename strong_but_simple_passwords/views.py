from flask import render_template, request
from .core import get_random_sentence


def index():
    if request.method == "GET":
        random_sentence = get_random_sentence()
        return render_template("index.html", sentence=random_sentence)

    # if no sentence was sent via POST, just display a random sentence
    if "input_sentence" not in request.form.keys():
        random_sentence = get_random_sentence()
        return render_template("index.html", sentence=random_sentence)

    user_sentence = request.form["input_sentence"]
    return render_template("index.html", sentence=user_sentence)
