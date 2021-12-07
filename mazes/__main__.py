from maze import Maze
from display import Display
import arcade


maze = Maze(rows=20, columns=20)
Display(maze, 40, 40, 10)

arcade.run()
