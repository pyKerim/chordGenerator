import random
import chords
import input_utils

from input_utils import input_normalisation
from chords import chords_list
chords = chords_list

def clean_input(user_input):
    return user_input

# Print title
print("Welcome to the Chord Quiz")
print("\n")

# Loop the quiz for 5 questions
question_number = 1
score = 0
while question_number <= 5:
    # Randomly select a chord from the dictionary
    chord, chord_tones = random.choice(list(chords.items()))

    # Get the answer as string and split the letters
    answer = input(f"What are the tones in {chord}:\n")

    answer = input_normalisation(answer)
    # Check if the lists match
    if set(answer) == set(chords[chord]):
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question_number += 1
print(f"You scored {score}/5!")