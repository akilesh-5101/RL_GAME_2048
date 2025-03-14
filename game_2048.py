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
import numpy
from player import Player 
from env import Env


### ======================
# Main Program
### ======================

if __name__ == "__main__":
	print("This code is being executed directly and not imported from other module")
	env = Env(4)
	env.insert_num()
