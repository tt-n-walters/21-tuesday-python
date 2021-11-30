

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


maze = Maze(rows=5, columns=5)
print(maze.grid)