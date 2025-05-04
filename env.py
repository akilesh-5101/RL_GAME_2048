"""
env.py - File that contains the game environment function

Author: Akilesh Venkat (3011akilesh1510@gmail.com)
Date Created: 2025-03-14
Date Modified: 2025-03-14
"""

### ======================
# Imports
### ======================
import argparse
import numpy as np


### ======================
# Environment Agent
### ======================
class Env:
	def __init__(self, dim, seed_val=5):
		self.env_state = np.random.choice([0,0,0,0,1,1,2],size=(4,4))
		self.dim = dim
		np.random.seed(seed_val)
		self.num_possible = [1,1,1,1,1,1,2]
	
	def insert_num (self):
		rand_num_to_insert = np.random.choice(self.num_possible)
		
		#Collecting all zero value indices
		empty_indices = np.where(self.env_state == 0)
		t_val = empty_indices[0].shape[-1]
		#Picking one of the collected indices in random
		rand_ind = np.random.randint(t_val)
		row = empty_indices[0][rand_ind]
		col = empty_indices[1][rand_ind]

		self.env_state[row][col] = rand_num_to_insert
	
	def check_game_outcome (self):
		result = 0
		if not np.isin(0, self.env_state):
			result = -1
		if np.isin(2048, self.env_state): 
			result = 1
		return result

