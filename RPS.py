import random

# Improved player function using history and counter-strategy
def player(prev_play, opponent_history=[]):
    # Append the current play to the opponent's history
    opponent_history.append(prev_play)

    # If it's the first play, pick randomly since we have no history
    if len(opponent_history) == 1:
        return random.choice(["R", "P", "S"])

    # Get the last move made by the opponent
    last_move = opponent_history[-1]
    
    # Predict based on last move - counter strategy:
    # Rock -> Paper (P beats R)
    # Paper -> Scissors (S beats P)
    # Scissors -> Rock (R beats S)
    if last_move == "R":
        return "P"  # Paper beats Rock
    elif last_move == "P":
        return "S"  # Scissors beats Paper
    else:
        return "R"  # Rock beats Scissors

    # If no obvious pattern is detected, pick a random move
    return random.choice(["R", "P", "S"])
