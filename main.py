import random
from stages import stage
import logo
end_of_game = False

word_list = ["Apple", " Orange", "Peach", "Banana"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo.name)
print(logo.lo)
print(word_list)
lives = 5
#print(f"Solution {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter  ==>").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in  chosen_word:
        lives -= 1
        if lives ==0:
            end_of_game = True
            print("You lose")
    print(f"{"".join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")
    if lives > 0:
        print(stage[lives-1])