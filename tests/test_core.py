import random
from decimal import Decimal

import pytest

from strong_but_simple_passwords import core
from strong_but_simple_passwords.core import (
    estimate_password_strength,
    generate_password_from_sentence,
    get_first_letters_from_each_word,
    get_first_letters_from_word,
    get_random_sentence,
    get_random_symbol,
    put_symbol_between_words,
    sentences,
    symbols,
)


def test_get_random_sentence():
    random_sentence = get_random_sentence()

    assert random_sentence in sentences


def test_get_first_letters_from_word():
    word = "Candy"
    assert get_first_letters_from_word(word, 0) == ""
    assert get_first_letters_from_word(word, 1) == "C"
    assert get_first_letters_from_word(word, 2) == "Ca"
    assert get_first_letters_from_word(word, 3) == "Can"
    assert get_first_letters_from_word(word, 10) == "Candy"

    word = ""
    assert get_first_letters_from_word(word, 0) == ""
    assert get_first_letters_from_word(word, 1) == ""
    assert get_first_letters_from_word(word, 10) == ""

    with pytest.raises(ValueError):
        get_first_letters_from_word("oops", -1)


def test_get_first_letters_from_each_word():
    sentence = "I like cute dogs"
    assert get_first_letters_from_each_word(sentence, 1) == ["I", "l", "c", "d"]
    assert get_first_letters_from_each_word(sentence, 2) == ["I", "li", "cu", "do"]
    assert get_first_letters_from_each_word(sentence, 3) == ["I", "lik", "cut", "dog"]
    assert get_first_letters_from_each_word(sentence, 0) == ["", "", "", ""]

    sentence = "Hello"
    assert get_first_letters_from_each_word(sentence, 1) == ["H"]
    assert get_first_letters_from_each_word(sentence, 2) == ["He"]
    assert get_first_letters_from_each_word(sentence, 0) == [""]

    with pytest.raises(ValueError):
        get_first_letters_from_each_word(sentence, -1)


def test_get_random_symbol():
    random_symbol = get_random_symbol()

    assert random_symbol in symbols


def test_put_symbol_between_words():
    words = ["I", "like", "cute", "dogs"]
    symbol = "!"

    assert put_symbol_between_words(words, symbol, 0) == [
        "!",
        "I",
        "like",
        "cute",
        "dogs",
    ]

    assert put_symbol_between_words(words, symbol, 1) == [
        "I",
        "!",
        "like",
        "cute",
        "dogs",
    ]

    assert put_symbol_between_words(words, symbol, 3) == [
        "I",
        "like",
        "cute",
        "!",
        "dogs",
    ]

    assert put_symbol_between_words(words, symbol, 4) == [
        "I",
        "like",
        "cute",
        "dogs",
        "!",
    ]

    with pytest.raises(ValueError):
        put_symbol_between_words(words, symbol, 10)

    with pytest.raises(ValueError):
        put_symbol_between_words(words, symbol, -1)


def test_generate_password_from_sentence(monkeypatch):
    monkeypatch.setattr(core, "get_random_symbol", lambda: "!")
    monkeypatch.setattr(random, "randint", lambda x, y: 1)

    sentence = "I like cute dogs and cats"
    assert generate_password_from_sentence(sentence) == "I!lcdac"

    monkeypatch.setattr(random, "randint", lambda x, y: 0)
    assert generate_password_from_sentence(sentence) == "!Ilcdac"

    monkeypatch.setattr(random, "randint", lambda x, y: 6)
    assert generate_password_from_sentence(sentence) == "Ilcdac!"

    monkeypatch.setattr(random, "randint", lambda x, y: 3)
    assert (
        generate_password_from_sentence(sentence, letters_per_word=3)
        == "Ilikcut!dogandcat"
    )


def test_estimate_password_strength():
    """
    This example is taken from the zxcvbn documentation.
    """
    password = "JohnSmith123"
    response = estimate_password_strength(password)

    assert response.get_fast_cracking_time_string() == "less than a second"
    assert response.get_fast_cracking_time_seconds() == Decimal("0.00025678")
    assert response.get_slow_cracking_time_string() == "4 minutes"
    assert response.get_slow_cracking_time_seconds() == Decimal("256.78")
