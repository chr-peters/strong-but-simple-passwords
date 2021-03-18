import random

sentences = [
    "My favourite food is ice cream",
    "I love taking long walks at the beach",
    "Watching my favourite movie while eating good food is fun",
    "I love the taste of a pice of chocolate cake",
]


def get_random_sentence():
    return random.choice(sentences)
