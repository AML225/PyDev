import random

def dice():
    return random.randint(1,6)

class Roll:

    def __init__(self, num_die: int):
        self.num_die = num_die
    
    def roll(self):
        roll = []
        for i in range(self.num_die):
            roll.append(dice())
        return roll

roll_1 = tuple(Roll(5).roll())
print(f'Roll 1 is: {roll_1}')

keep_dice = [1, 2]
keep_roll = []

for i in range(len(keep_dice)):
    keep_roll.append(roll_1[keep_dice[i]-1])

print(f'Keeping dice numbers: {keep_dice}, with values {keep_roll}')

roll_2 = tuple(Roll(5 - len(keep_roll)).roll())
print(f'Roll 2 is: {roll_2}')

keep_dice = [1]

for i in range(len(keep_dice)):
    keep_roll.append(roll_2[keep_dice[i]-1])

print(f'Keeping dice numbers: {keep_dice}, banked dice values are now {keep_roll}')

roll_3 = tuple(Roll(5 - len(keep_roll)).roll())
print(f'Roll 3 is: {roll_3}')

keep_roll.extend(roll_3)

print(f'Your final 5 dice values are: {keep_roll}')
    

