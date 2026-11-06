from english_words import get_english_words_set

VALID_WORDS = []
game_words = []


def setup_game():
    global game_words
    global VALID_WORDS
    words = [w.lower() for w in get_english_words_set(['web2'], lower=True) if
             len(w) == 5 and w.isalpha() and allowed(w)]
    valid_words = words + missing_words()
    print(f"Generated {len(valid_words)} valid 5-letter words from the English words set.")
    VALID_WORDS = valid_words
    game_words = valid_words


def letter_not_in_word(letter):
    global game_words
    filtered_words = [word for word in game_words if letter not in word]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    game_words = filtered_words


def letter_in_word(letter, position):
    global game_words
    filtered_words = [word for word in game_words if letter in word]
    filtered_words = [word for word in filtered_words if not word[position - 1] == letter]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    game_words = filtered_words


def letter_in_position(letter, position):
    global game_words
    filtered_words = [word for word in game_words if word[position - 1] == letter]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    game_words = filtered_words


def allowed(word):
    forbidden_words = ['bruce', 'nelly']
    if word in forbidden_words:
        return False
    else:
        return True


def missing_words():
    return ['dreck', 'balls', 'ramps', 'sails', 'nails', 'mails', 'boils', 'files', 'pails', 'rails', 'fails', 'tails',
            'bails', 'boats', 'hails', 'jails', 'wails', 'quads', 'waves', 'sings', 'bells', 'cells', 'dells', 'hells',
            'yells', 'sells', 'bounds', 'hounds', 'mounds', 'pounds', 'rounds', 'sounds', 'wounds']


def test_words(words):
    tested = []
    for word in words:
        if word in get_valid_words():
            print(f"{word} TRUE")
        else:
            print(f"{word} FALSE")
            tested.append(word)
    print(tested)


def get_valid_words():
    global VALID_WORDS
    return VALID_WORDS


def get_game_words():
    global game_words
    return game_words
