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
	def __init__(self, M):
		self.env_state = np.zeros((M, M), dtype=int)
		self.M = M
	
	def insert_num (self):
		empty_indices = np.where(self.env_state == 0)
		t_val = empty_indices[0].shape[-1] 
		rand_ind = np.random.randint(t_val)
		row = empty_indices[0][rand_ind]
		col = empty_indices[1][rand_ind]
		self.env_state[row][col] = 1
		



