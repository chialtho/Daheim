#! /usr/bin/env python3
from pickle import FALSE
import numpy as np
import random


rows = 10
columns = 10
mines = 6

dim = (rows, columns)
field = np.zeros(dim)
pos_list = []

for i in range(rows):
    for j in range(columns):
        pos_list.append((i,j))
        
mine_pos = random.sample(pos_list, mines)

for pos in mine_pos:
    row, column = pos
    field[row, column] = 1



print(field)


neighbouring_pos_dict = {}

for i in range(0, rows):
    for j in range(0, columns):

        tmp = [(itmp, jtmp) for itmp in range(i-1, i+2) for jtmp in range(j-1, j+2) if not (i == itmp and j == jtmp)]
        tmp =[(itmp, jtmp) for (itmp, jtmp) in tmp if (itmp > 0 and jtmp > 0 and itmp < rows and jtmp < columns)]
        neighbouring_pos_dict[(i, j)] = tmp


player_field = np.zeros(dim)

a = 1
b = 1

move = (a, b)



save_mode = True

if save_mode:
    if field[a, b] != 0.0:
        player_field[a, b] = -1
    else:
        print("Game over")
else:
    if field[a, b] == 1:
        print("Game over")

    pos_list = neighbouring_pos_dict.get(move)

    mine_counter = 0
    for pos in pos_list:
        (r, c) = pos
        val = field[r, c]
        if val == 1:
            mine_counter += 1

    player_field[a, b] = mine_counter    

print(player_field)