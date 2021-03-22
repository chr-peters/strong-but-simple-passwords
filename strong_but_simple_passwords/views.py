from flask import render_template, request
from .core import (
    get_random_sentence,
    generate_password_from_sentence,
    estimate_password_strength,
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

    response = estimate_password_strength(generated_password)

    # get the time it would take a powerful offline attacker (1e10 hashes per second)
    # to crack this password
    cracking_time = response.get_fast_cracking_time_string()

    return render_template(
        "index.html",
        sentence=user_sentence,
        generated_password=generated_password,
        cracking_time=cracking_time,
    )
