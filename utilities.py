from game_actions import get_game_words, get_valid_words


def starting_word_ideas(vowel_number, all_diffent_letters=True):
    vowels = ['a', 'e', 'i', 'o', 'u']
    suggestions = []

    for word in get_game_words():
        vocs = 0
        for letter in word:
            if letter in vowels:
                vocs += 1
        if vocs == vowel_number:
            if all_diffent_letters:
                if len(set(word)) == len(word):
                    suggestions.append(word)
            else:
                suggestions.append(word)
    if len(set(suggestions)) > 0:
        print(set(suggestions))


def test_words(words):
    tested = []
    for word in words:
        if word in get_valid_words():
            print(f"{word} TRUE")
        else:
            print(f"{word} FALSE")
            tested.append(word)
    if len(set(tested)) > 0:
        print(set(tested))
