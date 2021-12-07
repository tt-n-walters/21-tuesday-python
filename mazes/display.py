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
    
        self.shapes_list = arcade.ShapeElementList()

        self.shapes_map = [
            [ [] for _ in range(self.maze.columns) ]
            for _ in range(self.maze.rows)
        ]


        
    def create_shapes(self, new_row, new_column):
        self.remove_shapes(new_row, new_column)
        cell_width = self.cell_width
        cell_height = self.cell_height
        padding = self.padding

        for row in range(self.maze.rows):
            for column in range(self.maze.columns):
                if row == new_row and column == new_column:
                    x = column * cell_width + padding
                    y = self.height - cell_height - row * cell_height - padding
                    cell = self.maze[row][column]
                    if cell["down"]:
                        shape = arcade.create_line(x, y, x+cell_width, y, arcade.color.GREEN)  # down
                        self.shapes_list.append(shape)
                        self.shapes_map[row][column].append(shape)
                    if cell["up"]:
                        shape = arcade.create_line(x, y+cell_height, x+cell_width, y+cell_height, arcade.color.GREEN) # top
                        self.shapes_list.append(shape)
                        self.shapes_map[row][column].append(shape)
                    if cell["left"]:
                        shape = arcade.create_line(x, y, x, y+cell_height, arcade.color.GREEN) # left
                        self.shapes_list.append(shape)
                        self.shapes_map[row][column].append(shape)
                    if cell["right"]:
                        shape = arcade.create_line(x+cell_width, y, x+cell_width, y+cell_height, arcade.color.GREEN) # right
                        self.shapes_list.append(shape)
                        self.shapes_map[row][column].append(shape)
                    if (column, row) in self.maze.stack:
                        shape = arcade.create_rectangle_filled(
                            x+cell_width/2, y+cell_height/2,
                            cell_width*0.5, cell_height*0.5,
                            arcade.color.YELLOW
                        )
                        self.shapes_list.append(shape)
                        self.shapes_map[row][column].append(shape)


    def remove_shapes(self, row, column):
        shapes = self.shapes_map[row][column]
        for shape in shapes:
            self.shapes_list.remove(shape)
        self.shapes_map[row][column].clear()
    

    def on_draw(self):
        arcade.start_render()

        self.maze.generate()
        self.create_shapes(self.maze.y, self.maze.x)
        if self.maze.y < self.maze.rows - 1:
            self.create_shapes(self.maze.y + 1, self.maze.x)
        if self.maze.y > 0:
            self.create_shapes(self.maze.y - 1, self.maze.x)
        if self.maze.x < self.maze.columns - 1:
            self.create_shapes(self.maze.y, self.maze.x + 1)
        if self.maze.x > 0:
            self.create_shapes(self.maze.y, self.maze.x - 1)
        self.shapes_list.draw()
    