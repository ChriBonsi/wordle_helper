from game_actions import letter_in_position, letter_not_in_word, letter_in_word, setup_game, get_game_words

if __name__ == '__main__':
    setup_game()

    to_test = ['bruce', 'carly', 'nelly']
    # test_words(to_test)

    # EXAMPLE OF GAME
    letter_not_in_word('g')
    letter_not_in_word('i')
    letter_not_in_word('f')
    letter_not_in_word('t')
    letter_not_in_word('s')

    letter_in_word('c', 1)
    letter_not_in_word('l')
    letter_not_in_word('o')
    letter_not_in_word('w')
    letter_not_in_word('n')

    letter_not_in_word('p')
    letter_in_word('e', 2)
    letter_not_in_word('a')
    letter_in_position('c', 4)
    letter_not_in_word('h')

    letter_in_position('d', 1)
    letter_in_position('r', 2)
    letter_in_position('e', 3)
    letter_not_in_word('a')
    letter_not_in_word('m')

    print(f"After applying the game rules, {len(get_game_words())} valid words remain: {get_game_words()}")
