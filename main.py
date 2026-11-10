from game_actions import letter_in_position, letter_not_in_word, setup_game, get_game_words
from utilities import starting_word_ideas, test_words

if __name__ == '__main__':
    setup_game()

    to_test = ['diego']
    test_words(to_test)

    starting_word_ideas(4)

    # EXAMPLE OF GAME
    letter_not_in_word('a')
    letter_not_in_word('n')
    letter_not_in_word('i')
    letter_not_in_word('m')
    letter_in_position('e', 5)

    letter_not_in_word('g')
    letter_in_position('r', 2)
    letter_not_in_word('o')
    letter_not_in_word('p')

    print(f"After applying the game rules, {len(get_game_words())} valid words remain: {get_game_words()}")
