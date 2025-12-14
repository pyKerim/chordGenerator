import random

from chords import chords
from input_utils import input_normalisation

# Print title
print("Welcome to the Chord Quiz")
input("Press any key")
print("\n" * 25)

# Loop the quiz till all lives are gone
lives = 5
question_number = 1
score = 0

while lives > 0:
    # Randomly select a chord from the dictionary
    chord, chord_tones = random.choice(list(chords.items()))
    # Get the answer as string and split the letters
    print(f"Question #{question_number}: {chord}")
    answer = input(f"What are the tones in {chord}:\n")
    answer = input_normalisation(answer)

    # Check if the lists match
    if set(answer) == set(chords[chord]) and len(answer) == len(chords[chord]):
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was: {', '.join(chords[chord])}")
        lives -= 1
        print(f"You have {lives} lives left.")
    question_number += 1

print(f"You scored {score}")
my_scores = open("scores.txt", "a")
my_scores.write(str(score))
my_scores.close()
