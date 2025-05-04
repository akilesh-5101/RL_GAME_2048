"""
game_2048.py - File to simulate the 2048 game using agents and RL

Author: Akilesh Venkat (3011akilesh1510@gmail.com)
Date Created: 2025-03-14
Date Modified: 2025-03-14
"""

### ======================
# Imports
### ======================
import argparse
import numpy as np
from player import Player 
from env import Env


### ======================
# Main Program
### ======================

if __name__ == "__main__":
	player = Player(4)
	env = Env(4, 6)
	print("\nPlayer's turn\n\t")
	print(env.env_state)
	user_entry = input("\nChoose (l/r/u/d): ")
	while user_entry == 'l' or user_entry == 'r' or user_entry == 'u' or user_entry == 'd':
		if user_entry == 'l':
			env.env_state = player.swipe_left(env.env_state)
		elif user_entry == 'r':
			env.env_state = player.swipe_right(env.env_state)
		elif user_entry == 'u':
			env.env_state = player.swipe_up(env.env_state)
		elif user_entry == 'd':
			env.env_state = player.swipe_down(env.env_state)
			
		print("\nOutput:\n\t")
		print(env.env_state)

		env.insert_num()
		out = env.check_game_outcome()
		if out == -1:
			print("\nGame ended in Loss")
			break
		elif out == 1:
			print("\nGame ended in Win")
			break
		print("\nPlayer's turn\n\t")
		print(env.env_state)
		user_entry = input("\nChoose (l/r/u/d): ")

