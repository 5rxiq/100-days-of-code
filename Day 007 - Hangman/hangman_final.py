import random
import hangman_words
import hangman_art
import replit

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
user_guesses = []

print(hangman_art.logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    replit.clear()

    if guess in user_guesses:
        print("You already guessed that letter.")
    else:
        user_guesses.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])