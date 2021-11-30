import arcade


class Display(arcade.Window):
    def __init__(self, maze, cell_width, cell_height, padding):
        width = maze.columns * cell_width + padding * 2
        height = maze.rows * cell_height + padding * 2
        super().__init__(width, height, "Maze")
        arcade.set_background_color(arcade.color.BLACK)

        self.maze = maze
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.padding = padding


        
    def create_shapes(self):
        cell_width = self.cell_width
        cell_height = self.cell_height
        padding = self.padding

        shapes_list = arcade.ShapeElementList()
        for row in range(self.maze.rows):
            for column in range(self.maze.columns):
                x = column * cell_width + padding
                y = self.height - cell_height - row * cell_height - padding
                cell = self.maze[row][column]
                if cell["down"]:
                    shapes_list.append(arcade.create_line(x, y, x+cell_width, y, arcade.color.GREEN))  # down
                if cell["up"]:
                    shapes_list.append(arcade.create_line(x, y+cell_height, x+cell_width, y+cell_height, arcade.color.GREEN)) # top
                if cell["left"]:
                    shapes_list.append(arcade.create_line(x, y, x, y+cell_height, arcade.color.GREEN)) # left
                if cell["right"]:
                    shapes_list.append(arcade.create_line(x+cell_width, y, x+cell_width, y+cell_height, arcade.color.GREEN)) # right
                if (column, row) in self.maze.stack:
                    shapes_list.append(arcade.create_rectangle_filled(
                        x+cell_width/2, y+cell_height/2,
                        cell_width*0.5, cell_height*0.5,
                        arcade.color.YELLOW
                    ))

        return shapes_list
    

    def on_draw(self):
        arcade.start_render()

        self.maze.generate()
        shapes = self.create_shapes()
        shapes.draw()