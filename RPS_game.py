import random
from tabulate import tabulate

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}
    game_history = []  # Store the moves of each game

    for game_num in range(1, num_games + 1):
        print(f"--> Starting Game {game_num}")
        print(f"   --> Player 1's previous move: {p1_prev_play}, Player 2's previous move: {p2_prev_play}")
        
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        print(f"   --> Player 1 plays: {p1_play}, Player 2 plays: {p2_play}")

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
            print(f"   --> It's a tie!")
        elif (p1_play == "P" and p2_play == "R") or (p1_play == "R" and p2_play == "S") or (p1_play == "S" and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
            print(f"   --> Player 1 wins this round!")
        elif (p2_play == "P" and p1_play == "R") or (p2_play == "R" and p1_play == "S") or (p2_play == "S" and p1_play == "P"):
            results["p2"] += 1
            winner = "Player 2 wins."
            print(f"   --> Player 2 wins this round!")

        # Store the game results (both players' moves and the outcome)
        game_history.append({
            "Game Number": game_num,
            "Player 1 Move": p1_play,
            "Player 2 Move": p2_play,
            "Winner": winner,
            "Score P1": results["p1"],
            "Score P2": results["p2"],
            "Ties": results["tie"]
        })

        # Display the flow in terminal if verbose is True
        if verbose:
            print(f"\n--> Game {game_num}:")
            print(f"   --> Player 1 played {p1_play}, Player 2 played {p2_play}")
            print(f"   --> {winner}")
            print(f"   --> Current Score: {results}")
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    # Convert the list of dictionaries into a list of lists for tabulate
    game_history_table = [list(game.values()) for game in game_history]
    
    # Print the game history table after all games are done
    print("\nGame History:")
    headers = ["Game Number", "Player 1 Move", "Player 2 Move", "Winner", "Score P1", "Score P2", "Ties"]
    print(tabulate(game_history_table, headers=headers, tablefmt="pretty"))
    
    games_won = results['p2'] + results['p1']
    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print(f"\n--> Final results: {results}")
    print(f"--> Player 1 win rate: {win_rate:.2f}%")

    return win_rate

# Example of usage:
# play(player, quincy, 10, verbose=True)  # Call with verbosity enabled to track flow

def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    print(f"--> Quincy chooses: {choices[counter[0] % len(choices)]}")
    return choices[counter[0] % len(choices)]

def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    print(f"--> Mrugesh predicts the opponent's next move based on history: {most_frequent}")
    return ideal_response[most_frequent]

def kris(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    print(f"--> Kris responds with: {ideal_response[prev_opponent_play]}")
    return ideal_response[prev_opponent_play]

def abbey(prev_opponent_play, opponent_history=[], play_order=[{
    "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0,
}]):
    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    print(f"--> Abbey predicts the next move based on last two plays: {prediction}")
    return ideal_response[prediction]

def human(prev_opponent_play):
    play = ""
    while play not in ['R', 'P', 'S']:
        play = input("[R]ock, [P]aper, [S]cissors? Please only Type Capital Letters R,P or S: ")
        print(play)
    print(f"--> Human plays: {play}")
    return play

def random_player(prev_opponent_play):
    choice = random.choice(['R', 'P', 'S'])
    print(f"--> Random player plays: {choice}")
    return choice

def player(prev_play, opponent_history=[]):
    # Append the current play to the opponent's history
    opponent_history.append(prev_play)

    # If it's the first play, pick randomly since we have no history
    if len(opponent_history) == 1:
        choice = random.choice(["R", "P", "S"])
        print(f"--> Player plays randomly: {choice}")
        return choice

    # Get the last move made by the opponent
    last_move = opponent_history[-1]
    
    # Predict based on last move - counter strategy:
    if last_move == "R":
        choice = "P"  # Paper beats Rock
    elif last_move == "P":
        choice = "S"  # Scissors beats Paper
    else:
        choice = "R"  # Rock beats Scissors

    print(f"--> Player counters opponent's move: {choice}")
    return choice
