from english_words import get_english_words_set
from turn_actions import letter_in_position, letter_not_in_word

if __name__ == '__main__':
    valid_words = {w.lower() for w in get_english_words_set(['web2'], lower=True) if len(w) == 5 and w.isalpha()}
    print(f"Generated {len(valid_words)} valid 5-letter words from the English words set.")

    # EXAMPLE OF GAME
    valid_words = letter_not_in_word('t', valid_words)
    valid_words = letter_in_position('o', 2, valid_words)
    valid_words = letter_not_in_word('k', valid_words)
    valid_words = letter_not_in_word('e', valid_words)
    valid_words = letter_not_in_word('n', valid_words)

    valid_words = letter_not_in_word('b', valid_words)
    valid_words = letter_not_in_word('i', valid_words)
    valid_words = letter_not_in_word('l', valid_words)
    valid_words = letter_not_in_word('s', valid_words)

    valid_words = letter_not_in_word('g', valid_words)
    valid_words = letter_in_position('u', 3, valid_words)
    valid_words = letter_not_in_word('r', valid_words)
    valid_words = letter_not_in_word('d', valid_words)

    valid_words = letter_not_in_word('m', valid_words)
    valid_words = letter_in_position('c', 4, valid_words)
    valid_words = letter_in_position('h', 5, valid_words)
    print(valid_words)
    valid_words = letter_in_position('p', 1, valid_words)
    print(valid_words)
