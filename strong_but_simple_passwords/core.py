import random
from zxcvbn import zxcvbn


sentences = [
    "My favourite food is lemon ice cream",
    "I love taking long walks at the beach",
    "Watching my favourite movie while eating good food is fun",
    "I love the taste of a pice of chocolate cake",
    "I really enjoy drinking lemonade while watching the sunset",
]

symbols = "!?@#$%^&*"


def get_random_sentence():
    return random.choice(sentences)


def get_first_letters_from_word(word, num_letters):
    if num_letters < 0:
        raise ValueError(
            f"num_letters={num_letters} is invalid. "
            "The number of letters must be positive!"
        )

    new_word_length = min(len(word), num_letters)
    return word[:new_word_length]


def get_first_letters_from_each_word(sentence, num_letters=1):
    words = sentence.split()
    first_letters = [get_first_letters_from_word(word, num_letters) for word in words]
    return first_letters


def get_random_symbol():
    return random.choice(symbols)


def put_symbol_between_words(list_of_words, symbol, position):
    if position > len(list_of_words):
        raise ValueError(
            "Position can't be greater than length! "
            f"length={len(list_of_words)}, position={position}"
        )

    if position < 0:
        raise ValueError("Position can't be negative!")

    copy = list_of_words.copy()
    copy.insert(position, symbol)

    return copy


def generate_password_from_sentence(sentence, letters_per_word=1):
    first_letters = get_first_letters_from_each_word(sentence, letters_per_word)

    symbol = get_random_symbol()
    symbol_position = random.randint(0, len(first_letters))
    words_with_symbol = put_symbol_between_words(first_letters, symbol, symbol_position)

    # convert the list of words with the symbol to a single string
    return "".join(words_with_symbol)


class PasswordStrengthResult:
    """
    A wrapper around the response object returned by zxcvbn.
    """

    def __init__(self, zxcvbn_response):
        self._data = zxcvbn_response

    def get_fast_cracking_time_string(self):
        return self._data["crack_times_display"]["offline_fast_hashing_1e10_per_second"]

    def get_fast_cracking_time_seconds(self):
        return self._data["crack_times_seconds"]["offline_fast_hashing_1e10_per_second"]


def estimate_password_strength(password):
    result = zxcvbn(password)
    return PasswordStrengthResult(result)
