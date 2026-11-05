from game_actions import letter_in_position, letter_not_in_word, letter_in_word, setup_game, get_valid_words, \
    get_game_words

if __name__ == '__main__':
    setup_game()

    to_test = ['quads', 'balls', 'mails', 'waves', 'sings', 'bells', 'cells', 'dells', 'hells', 'yells', 'sells',
               'bounds', 'hounds', 'mounds', 'pounds', 'rounds', 'sounds', 'wounds']
    tested = []
    for word in to_test:
        if word in get_valid_words():
            print(f"{word} TRUE")
        else:
            print(f"{word} FALSE")
            tested.append(word)
    print(tested)

    # EXAMPLE OF GAME
    letter_not_in_word('b')
    letter_not_in_word('o')
    letter_not_in_word('w')
    letter_not_in_word('e')
    letter_not_in_word('l')

    letter_not_in_word('d')
    letter_in_word('r', 2)
    letter_in_word('a', 3)
    letter_not_in_word('i')
    letter_not_in_word('n')

    letter_in_word('r', 1)
    letter_in_position('a', 2)
    letter_not_in_word('m')
    letter_in_word('p', 4)
    letter_not_in_word('s')

    letter_in_position('p', 1)
    letter_in_position('a', 2)
    letter_in_position('r', 3)
    letter_not_in_word('k')
    letter_not_in_word('y')
    print(f"After applying the game rules, {len(get_game_words())} valid words remain: {get_game_words()}")
