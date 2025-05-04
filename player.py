"""
player.py - File that containes the player function

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
# Player Agent 
### ======================
class Player:
	def __init__ (self, dim):
		self.dim = dim

	def swipe_left (self, env_state):
		output_state = np.zeros((self.dim,self.dim),dtype=int)

		for i in range(0,self.dim,1):
			#Initial read out zero values 
			non_zero_indices = np.nonzero(env_state[i])
			s = np.size(non_zero_indices)
			output_state[i,0:s] = env_state[i,non_zero_indices]
			
			for j in range(0,self.dim-1,1):
				#Check if any of the adjacent is 0, if yes skip, if no attempt merge operation
				if not output_state[i,j]:
					continue
				elif output_state[i,j] == output_state[i,j+1]:
					output_state[i,j] = 2*output_state[i,j]
					output_state[i,j+1] = 0
			
			#Filter out non-zero values and append corresponding number of zeros
			non_zero_indices = np.nonzero(output_state[i])
			s = np.size(non_zero_indices)
			output_state[i,0:s] = output_state[i,non_zero_indices]
			output_state[i,s:] = 0
		
		#Return
		return output_state
		
	def swipe_right (self, env_state):
		output_state = np.zeros((self.dim,self.dim),dtype=int)

		for i in range(0,self.dim,1):
			#Initial read out zero values 
			non_zero_indices = np.nonzero(env_state[i])
			s = np.size(non_zero_indices)
			output_state[i,0:s] = env_state[i,non_zero_indices]

			for j in range(self.dim-2,-1,-1):
				#Check if any of the adjacent is 0, if yes skip, if no attempt merge operation
				if not output_state[i,j+1]:
					continue
				elif output_state[i,j] == output_state[i,j+1]:
					output_state[i,j+1] = 2*output_state[i,j+1]
					output_state[i,j] = 0
			#Filter out non-zero values and append corresponding number of zeros
			non_zero_indices = np.nonzero(output_state[i])
			s = np.size(non_zero_indices)
			output_state[i,self.dim-s:] = output_state[i,non_zero_indices]
			output_state[i,0:self.dim-s] = 0
	
		#Return
		return output_state

	def swipe_up (self, env_state):
		output_state = np.zeros((self.dim,self.dim),dtype=int)

		for j in range(0,self.dim,1):
			#Initial read out zero values 
			non_zero_indices = np.nonzero(env_state[:,j])
			s = np.size(non_zero_indices)
			output_state[0:s,j] = env_state[non_zero_indices,j]
			
			for i in range(0,self.dim-1,1):
				#Check if any of the adjacent is 0, if yes skip, if no attempt merge operation
				if not output_state[i,j]:
					continue
				elif output_state[i,j] == output_state[i+1,j]:
					output_state[i,j] = 2*output_state[i,j]
					output_state[i+1,j] = 0
			
			#Filter out non-zero values and append corresponding number of zeros
			non_zero_indices = np.nonzero(output_state[:,j])
			s = np.size(non_zero_indices)
			output_state[0:s,j] = output_state[non_zero_indices,j]
			output_state[s:,j] = 0
		
		#Return
		return output_state
		
	def swipe_down (self, env_state):
		output_state = np.zeros((self.dim,self.dim),dtype=int)

		for j in range(0,self.dim,1):
			#Initial read out zero values 
			non_zero_indices = np.nonzero(env_state[:,j])
			s = np.size(non_zero_indices)
			output_state[0:s,j] = env_state[non_zero_indices,j]
			
			for i in range(self.dim-2,-1,-1):
				#Check if any of the adjacent is 0, if yes skip, if no attempt merge operation
				if not output_state[i+1,j]:
					continue
				elif output_state[i,j] == output_state[i+1,j]:
					output_state[i+1,j] = 2*output_state[i+1,j]
					output_state[i,j] = 0
			
			#Filter out non-zero values and append corresponding number of zeros
			non_zero_indices = np.nonzero(output_state[:,j])
			s = np.size(non_zero_indices)
			output_state[self.dim-s:,j] = output_state[non_zero_indices,j]
			output_state[0:self.dim-s,j] = 0
		
		#Return
		return output_state

							
		
				


				
		




