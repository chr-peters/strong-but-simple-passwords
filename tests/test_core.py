from strong_but_simple_passwords.core import get_random_sentence, sentences


def test_get_random_sentence():
    random_sentence = get_random_sentence()

    assert random_sentence in sentences
