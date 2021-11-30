import random


opposites = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}
directions = {    # direction: (x, y)
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}


class Maze:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
        self.grid = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                cell = {
                    "up": True,
                    "down": True,
                    "left": True,
                    "right": True
                }
                row.append(cell)
            self.grid.append(row)
            
            self.stack = []
            self.first = True
            self.x = columns // 2
            self.y = rows // 2


    def generate(self):

        if self.first or self.stack:
            self.first = False

            neighbours = {}

            for direction, movement in directions.items():
                next_x = self.x + movement[0]
                next_y = self.y + movement[1]
                if 0 <= next_x < self.columns and 0 <= next_y < self.rows:
                    next = maze[next_y][next_x]
                    if all(next.values()): # Check if all walls are still True
                        neighbours[direction] = next_x, next_y


            if neighbours:
                direction = random.choice(list(neighbours))
                opposite_direction = opposites[direction]

                next_x, next_y = neighbours[direction]
                # remove wall from current cell
                maze[self.y][self.x][direction] = False
                # remove opposite wall from next cell
                maze[next_y][next_x][opposite_direction] = False
                
                self.stack.append((self.x, self.y))

                self.x = next_x
                self.y = next_y
            
            else:
                # Dead end, no possible neighbours
                self.x, self.y = self.stack.pop()



maze = Maze(rows=5, columns=5)
print(maze.grid)