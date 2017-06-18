import random
import math

def dice_roll(n):
	for i in range(n):
		roll = random.randint(1, 6)
	return roll

print(dice_roll(1))
