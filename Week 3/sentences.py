########################
# Generating Sentences #
########################
import random

def get_determiner(quantity):
    """Return a randomly chosen determiner.

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = [
            "bird", "boy", "car","cat", "child", 
            "dog", "girl", "man", "rabbit", "woman"
        ]
    else:
        words = [
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"
        ]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb.

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    tense = tense.lower()

    if tense == "past":
        words = [
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        ]
    if tense == "present" and quantity == 1:
        words = [
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        ]
    if tense == "present" and quantity != 1:
        words = [
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        ]

    if tense == "future":
        words = [
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"
        ]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    if quantity == "single":
        quantity = 1
    else:
        quantity = 2

    determiner = get_determiner(quantity).capitalize()
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase1 = get_prepositional_phrase(quantity)
    prep_phrase2 = get_prepositional_phrase(quantity)
    sentence = [determiner] + [adjective] + [noun] + [verb] + [*prep_phrase1] + [*prep_phrase2]
    print(*sentence, end=".\n")


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
        ]
    word = random.choice(prepositions)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    sentence = [preposition] + [determiner] + [noun]
    return sentence

def get_adjective():
    adjectives = [
        "tall", "short", "big", "small", "tiny", "huge", "wide", "narrow",
        "rough", "smooth", "shiny", "wrinkled", "clean", "dirty", "kind", 
        "rude", "intelligent", "lazy", "honest", "brave", "shy", "loyal", 
        "creative", "selfish", "chubby", "thin", "muscular", "graceful", 
        "awkward", "elegant", "plain", "handsome", "beautiful", "ugly", 
        "cute", "stylish", "messy", "neat"
    ]

    word = random.choice(adjectives)
    return word


def main():
    """Starts the program.
    """
    make_sentence("single", "past")
    make_sentence("single", "present")
    make_sentence("single", "future")
    make_sentence("plural", "past")
    make_sentence("plural", "present")
    make_sentence("plural", "future")

# Start program
main()