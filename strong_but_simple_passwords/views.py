from flask import render_template, request

from .core import (
    estimate_password_strength,
    generate_password_from_sentence,
    get_random_sentence,
)


def index():
    if request.method == "GET":
        random_sentence = get_random_sentence()
        return render_template("index.html", sentence=random_sentence)

    # if no sentence was sent via POST, just display a random sentence
    if "input_sentence" not in request.form.keys():
        random_sentence = get_random_sentence()
        return render_template("index.html", sentence=random_sentence)

    # read user sentence and generate password
    user_sentence = request.form["input_sentence"]
    generated_password = generate_password_from_sentence(
        user_sentence, letters_per_word=3
    )

    password_strength_response = estimate_password_strength(generated_password)

    return render_template(
        "index.html",
        sentence=user_sentence,
        generated_password=generated_password,
        password_strength_response=password_strength_response,
    )
