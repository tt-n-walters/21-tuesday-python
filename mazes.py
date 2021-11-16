import arcade
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


rows = 20
columns = 20
cell_width = 40
cell_height = 40
padding = 10


maze = []
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
    maze.append(row)

x = columns // 2
y = rows // 2

width = columns * cell_width + padding * 2
height = rows * cell_height + padding * 2

arcade.open_window(width, height, "Maze")
arcade.set_background_color(arcade.color.BLACK)


def generate():
    global x, y
    neighbours = {}

    for direction, movement in directions.items():
        next_x = x + movement[0]
        next_y = y + movement[1]
        if 0 <= next_x < columns and 0 <= next_y < rows:
            next = maze[next_y][next_x]
            if all(next.values()): # Check if all walls are still True
                neighbours[direction] = next_x, next_y


    if neighbours:
        direction = random.choice(list(neighbours))
        opposite_direction = opposites[direction]

        next_x, next_y = neighbours[direction]
        
        # remove wall from current cell
        maze[y][x][direction] = False
        # remove opposite wall from next cell
        maze[next_y][next_x][opposite_direction] = False

        x = next_x
        y = next_y


def create_shapes():
    shapes_list = arcade.ShapeElementList()
    for row in range(rows):
        for column in range(columns):
            x = column * cell_width + padding
            y = height - cell_height - row * cell_height - padding
            cell = maze[row][column]
            if cell["down"]:
                shapes_list.append(arcade.create_line(x, y, x+cell_width, y, arcade.color.GREEN))  # down
            if cell["up"]:
                shapes_list.append(arcade.create_line(x, y+cell_height, x+cell_width, y+cell_height, arcade.color.GREEN)) # top
            if cell["left"]:
                shapes_list.append(arcade.create_line(x, y, x, y+cell_height, arcade.color.GREEN)) # left
            if cell["right"]:
                shapes_list.append(arcade.create_line(x+cell_width, y, x+cell_width, y+cell_height, arcade.color.GREEN)) # right
    return shapes_list

def draw(delta):
    arcade.start_render()
    generate()
    create_shapes().draw()


arcade.schedule(draw, 1/10)
arcade.run()
