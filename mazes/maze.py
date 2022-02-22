import random
from vector import Vector


opposites = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}
directions = {    # direction: (x, y)
    "up": Vector(0, -1),
    "down": Vector(0, 1),
    "left": Vector(-1, 0),
    "right": Vector(1, 0)
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
        
        self.current = Vector(columns // 2, rows // 2)


    def generate(self):

        if self.first or self.stack:
            self.first = False

            neighbours = {}

            for direction, movement in directions.items():
                next = self.current + movement
                if 0 <= next.x < self.columns and 0 <= next.y < self.rows:
                    next_pos = self.grid[next.y][next.x]
                    if all(next_pos.values()): # Check if all walls are still True
                        neighbours[direction] = next


            if neighbours:
                direction = random.choice(list(neighbours))
                opposite_direction = opposites[direction]

                next = neighbours[direction]
                print(neighbours)
                print(next)
                # remove wall from current cell
                self.grid[self.current.y][self.current.x][direction] = False
                # remove opposite wall from next cell
                self.grid[next.y][next.x][opposite_direction] = False
                
                self.stack.append(self.current)

                self.current = next
            
            else:
                # Dead end, no possible neighbours
                self.current = self.stack.pop()


    def __repr__(self):
        return "Maze with " + str(self.rows) + " rows and " + str(self.columns) + " columns."
    

    def __getitem__(self, index):
        return self.grid[index]



if __name__ == "__main__":
    maze = Maze(rows=5, columns=5)
    print(maze.grid)
