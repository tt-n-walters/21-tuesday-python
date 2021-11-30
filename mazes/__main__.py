from maze import Maze
from display import Display
import arcade


maze = Maze(rows=30, columns=30)
Display(maze, 20, 20, 10)
arcade.run()
