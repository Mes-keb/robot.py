
class Robot:
    """Stories the virtual robot's position and direction"""

    def __init__(self, grid_size=9):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        self.x = self.grid_size // 2
        self.y = self.grid_size // 2
        self.direction = "N"
        self.moves = 0

    def turn_left(self):
        directions = ["N", "W", "S", "E"]
        current = directions.index(self.direction)
        self.direction = directions[(current + 1) % 4]
        self.moves += 1

    def turn_right(self): 
        directions = ["N", "E", "S", "W"]
        current = directions.index(self.direction)
        self.direction = directions[(current + 1) % 4]
        self.moves += 1

    def move_forward(self):
        return self._move(1)
    
    def move_backward(self):
        return self._move(-1)

    def _move(self, step):
        dx, dy = {
            "N": (0, -1),
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0),
        }[self.direction]

        new_x = self.x + dx * step
        new_y = self.y + dy * step

        if not (0 <= new_x < self.grid_size
                and 0 <= new_y < self.grid_size):
            return False
        
        self.x = new_x
        self.y = new_y
        self.moves += 1
        return True
        