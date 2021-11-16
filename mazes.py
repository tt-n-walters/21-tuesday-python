import arcade
import random


arcade.open_window(420, 420, "Maze")
arcade.set_background_color(arcade.color.BLACK)

opposites = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}


maze = []
for _ in range(10):
    row = []
    for _ in range(10):
        cell = {
            "up": True,
            "down": True,
            "left": True,
            "right": True
        }
        row.append(cell)
    maze.append(row)

x = 0
y = 0

def generate():
    global x, y
    neighbours = {}

    # print("current", x, y)
    # right
    next_x = x + 1
    next_y = y
    # print("next", next_x, next_y)
    if 0 <= next_x < 10 and 0 <= next_y < 10:
        right = maze[next_y][next_x]
        # print(right)
        if all(right.values()): # Check if all walls are still True
            # print("Not visited")
            neighbours["right"] = next_x, next_y
        # else:
            # print("visited")
    # else:
        # print("off edge")

    # up
    next_x = x
    next_y = y - 1
    # print("next", next_x, next_y)
    if 0 <= next_x < 10 and 0 <= next_y < 10:
        up = maze[next_y][next_x]
        # print(up)
        if all(up.values()): # Check if all walls are still True
            # print("Not visited")
            neighbours["up"] = next_x, next_y
        # else:
            # print("visited")
    # else:
        # print("off edge")

    # left
    next_x = x - 1
    next_y = y
    # print("next", next_x, next_y)
    if 0 <= next_x < 10 and 0 <= next_y < 10:
        left = maze[next_y][next_x]
        # print(left)
        if all(left.values()): # Check if all walls are still True
            # print("Not visited")
            neighbours["left"] = next_x, next_y
        # else:
            # print("visited")
    # else:
        # print("off edge")
        
    # down
    next_x = x
    next_y = y + 1
    # print("next", next_x, next_y)
    if 0 <= next_x < 10 and 0 <= next_y < 10:
        down = maze[next_y][next_x]
        # print(down)
        if all(down.values()): # Check if all walls are still True
            # print("Not visited")
            neighbours["down"] = next_x, next_y
        # else:
            # print("visited")
    # else:
        # print("off edge")
    
    # print(neighbours)
    # print("choosing random")

    if neighbours:
        direction = random.choice(list(neighbours))
        opposite_direction = opposites[direction]
        # print("Moving", direction)
        # print("opposite", opposite_direction)

        next_x, next_y = neighbours[direction]
        # print("next cell", next_x, next_y)
        
        # print("removing walls.")
        # remove wall from current cell
        maze[y][x][direction] = False
        # remove opposite wall from next cell
        maze[next_y][next_x][opposite_direction] = False

        x = next_x
        y = next_y


def create_shapes():
    shapes_list = arcade.ShapeElementList()
    for row in range(10):
        for column in range(10):
            x = column * 40 + 10
            y = 420 - 40 - row * 40 - 10
            cell = maze[row][column]
            if cell["down"]:
                shapes_list.append(arcade.create_line(x, y, x+40, y, arcade.color.GREEN))  # down
            if cell["up"]:
                shapes_list.append(arcade.create_line(x, y+40, x+40, y+40, arcade.color.GREEN)) # top
            if cell["left"]:
                shapes_list.append(arcade.create_line(x, y, x, y+40, arcade.color.GREEN)) # left
            if cell["right"]:
                shapes_list.append(arcade.create_line(x+40, y, x+40, y+40, arcade.color.GREEN)) # right
    return shapes_list

def draw(delta):
    arcade.start_render()
    generate()
    create_shapes().draw()


arcade.schedule(draw, 1/60)
arcade.run()
