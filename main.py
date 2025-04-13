# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

play(player, quincy, 5)
play(player, abbey, 5)
play(player, kris, 5)
play(player, mrugesh, 5)

# Uncomment line below to play interactively against a bot:
play(human, abbey, 5, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
play(human, random_player, 5, verbose=True)



# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)