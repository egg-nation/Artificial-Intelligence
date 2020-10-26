from collections import deque
import random


def get_maze():
    maze = list()
    fd = open('maze.txt', 'r')
    row = fd.readline()

    # creating a list from the given maze
    while row:
        row = row.strip('[]\n').split(', ')
        int_row = list()

        for i in row:
            int_row.append(int(i))

        maze.append(int_row)
        row = fd.readline()

    return maze


labyrinth = get_maze()

# from where to where / change for multiple examples
x_s, y_s = 0, 1
x_f, y_f = 3, 2  #10, 5

# the height of the maze
n = len(labyrinth)

# the width of the maze
m = len(labyrinth)

# directions to move
dirs = {'up': (1, 0), 'right': (0, 1), 'left': (0, -1), 'down': (-1, 0)}
ways = ['up', 'right', 'left', 'down']


# find initial state to start
def get_initial_state():
    # using list as data structure
    progress = list()
    progress.append((x_s, y_s))

    # position on line and column axis x and y in the maze
    return (x_s, y_s), progress


# we reached the defined final state
def final_state(state):
    return state[0] == (x_f, y_f)


# checking the validity of the transition from a state using a certain direction from the list
def valid_transition(state, dir):
    # checking so that it doesn't go outside the predefined maze
    if state[0][0] + dir[0] < 0:
        return False

    if state[0][1] + dir[1] < 0:
        return False

    if state[0][0] + dir[0] >= n:
        return False

    if state[0][1] + dir[1] >= m:
        return False

    if labyrinth[state[0][0] + dir[0]][state[0][1] + dir[1]] == 1:
        return False

    return True


def transition(state, dir):
    # trying a direction of movement onto a given state

    # if the transition is valid (previous function)
    if valid_transition(state, dir):
        # create new state to add to the list
        new_state = (state[0][0] + dir[0], state[0][1] + dir[1])
        new_list = state[1].copy()
        new_list.append(new_state)
        return new_state, new_list

    return state


# BFS
def bfs(state):
    # starting with no visited positions
    visited = set()
    order = deque([])
    order.append(state)
    visited.add(state[0])

    while order:
        current_state = order.popleft()
        for i in ways:
            new_state = transition(current_state, dirs[i])
            if new_state[0] not in visited:
                if not final_state(new_state):
                    visited.add(new_state[0])
                    order.append(new_state)
                else:
                    print(new_state[1])


# bkt
def bkt(state, visited):
    # checking the status
    if final_state(state):
        print(state[1])
        return

    # trying all the possible combinations for the given ways (classic bkt)
    for i in ways:
        if valid_transition(state, dirs[i]):
            new_state = transition(state, dirs[i])
            if new_state[0] not in visited:
                visited.add(state[0])
                bkt(new_state, visited)
                visited.remove(state[0])


# HILLCLIMBING
def stochastic_HC(state):
    # starting with no visited positions
    visited = set()
    search = True

    while search:
        visited.add(state[0])
        search = False

        # creating a list of possible neighbours
        neighs = list()

        # adding all the possible neighbours by checking if the direction leads to a valid state
        for i in ways:
            if valid_transition(state, dirs[i]):
                new_state = transition(state, dirs[i])
                if new_state[0] not in visited:
                    neighs.append(new_state)

        if neighs:
            rand_index = random.randint(0, len(neighs) - 1)
            rand_neigh = neighs[rand_index]

            # checking if it s a final state
            if final_state(rand_neigh):
                print(rand_neigh[1])
            else:
                # continue if not
                search = True
                state = rand_neigh


if __name__ == '__main__':
    # bkt(get_initial_state(), set())
    # bfs(get_initial_state())
    for i in range(30):
        stochastic_HC(get_initial_state())
