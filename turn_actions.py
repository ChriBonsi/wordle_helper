def letter_not_in_word(letter, words):
    filtered_words = [word for word in words if letter not in word]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    return filtered_words

def letter_in_word(letter, position, words):
    filtered_words = [word for word in words if letter in word]
    filtered_words = [word for word in filtered_words if not word[position - 1] == letter]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    return filtered_words

def letter_in_position(letter, position, words):
    filtered_words = [word for word in words if word[position-1] == letter]
    print(f"Generated {len(filtered_words)} valid 5-letter words from the English words set.")
    return filtered_words