import matplotlib.pyplot as plt
import numpy as np

instructions = [(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]
#instructions = [(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0)]

plt.figure(figsize=(7, 1))

def move(current_position, move):
    current_x, current_y = current_position
    move_x, move_y = move
    return (current_x + move_x, current_y - move_y)

current_position_x, current_position_y = (0,0)
skip = False
for instruction in instructions:
    if instruction == (0,0):
        skip = True
        continue

    new_position_x, new_position_y = move((current_position_x, current_position_y), instruction)
    if not skip:
        xpoints = np.array([current_position_x, new_position_x])
        ypoints = np.array([current_position_y, new_position_y])
        plt.plot(xpoints, ypoints)
    current_position_x, current_position_y = new_position_x, new_position_y
    skip = False

plt.savefig('tortuga-flag.png')
