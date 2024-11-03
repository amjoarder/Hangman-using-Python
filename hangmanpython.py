import random

words = ["UMBRELLA", "COMPUTER", "TELESCOPE", "SMARTPHONE", "LAPTOP", "PERFUME"]

word = random.choice(words)
total_chances = 7
guessed_word = "-" * len(word)
guessed_letters = set()

while total_chances > 0 and guessed_word != word:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()

    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(letter)

    if letter in word:
        # Update guessed_word with the correctly guessed letter in all the correct positions
        new_guessed_word = ""
        for index in range(len(word)):
            if word[index] == letter:
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[index]
        guessed_word = new_guessed_word
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print("Remaining Chances:", total_chances)

    if guessed_word == word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    if guessed_word != word:
        print("Game Over")
        print("All the chances are exhausted")
        print("The correct word is:", word)
