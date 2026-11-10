# wordle_helper

Simple helper for the game Wordle.

It takes the list of possible words (English 5-letter words) and filters them by iteratively removing words that
don't match the conditions after each guess. The conditions are based on the feedback from the game:

- Green letter: the letter is in the correct position;
- Yellow letter: the letter is in the word but not in the correct position;
- Gray letter: the letter is not in the word.

So, every time the user takes a guess, they simply add a line of code in the main
to:

- Remove all words that don't have the green letters in the correct positions;
- Remove all words that don't have the yellow letters in the word;
- Remove all words that have the gray letters in the word.