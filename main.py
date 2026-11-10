from game_actions import letter_in_position, letter_not_in_word, letter_in_word, setup_game, get_game_words
from utilities import starting_word_ideas, test_words

if __name__ == '__main__':
    setup_game()

    to_test = ['claus', 'klaus']
    test_words(to_test)

    starting_word_ideas(3)

    # EXAMPLE OF GAME
    letter_not_in_word('t')
    letter_in_position('o', 2)
    letter_not_in_word('g')
    letter_not_in_word('u')
    letter_not_in_word('e')

    letter_not_in_word('p')
    letter_not_in_word('r')
    letter_not_in_word('n')
    letter_not_in_word('s')

    letter_in_position('l', 1)
    letter_not_in_word('c')
    letter_in_word('a', 4)

    print(f"After applying the game rules, {len(get_game_words())} valid words remain: {get_game_words()}")
