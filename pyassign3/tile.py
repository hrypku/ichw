"""
empty is the list of uncovered wall blocks,
filled is the list of covered list.
"""

import turtle


class Tile:
    """Define the tiles."""

    def __init__(self, a, b):
        self.length = a
        self.width = b

    def covered(self, m, n, c):
        """
        Return that covered by the tile on position c.
        Return False if the operation is n/a.
        """
        x = c % m
        y = c // m
        if x + self.length > m:
            return False
        if y + self.width > n:
            return False

        covered = []
        for p in range(y, y+self.width):
            for q in range(x, x+self.length):
                covered.append(m*p+q)
        return tuple(covered)

    def whether_uncovered(self, m, n, c, Filled):
        """Return whether the position that the tile will cover has been covered."""
        for i in self.covered(m, n, c):
            if i in Filled:
                return False
        return True

    def new_Empty(self, empty, m, n, c):
        """Return a new list of empty wall blocks."""
        if not self.covered(m, n, c):
            return False

        new_empty = [i for i in empty]
        for i in self.covered(m, n, c):
            new_empty.remove(i)
        return new_empty

    def new_Filled(self, filled, m, n, c):
        """Return a new list of filled wall blocks."""
        if not self.covered(m, n, c):
            return False

        new_filled = [i for i in filled]
        for i in self.covered(m, n, c):
            new_filled.append(i)
        return new_filled


def solute(empty, filled, tiles, m, n):
    """Return all the solutions."""
    if empty ==[]:
        return [[]]

    solutions = []
    for tile in tiles:
        if tile.covered(m, n,empty[0]) and tile.whether_uncovered(m, n, empty[0], filled):
            parts = solute(tile.new_Empty(empty, m, n, empty[0]), tile.new_Filled(filled, m, n, empty[0]), tiles, m, n)
            for part in parts:
                part.append(tile.covered(m, n, empty[0]))
            solutions.extend(parts)
    return solutions


class Grid(turtle.Turtle):
    """Draw the grid(which is actually the wall blocks)."""

    def __init__(self, m, n):
        turtle.Turtle.__init__(self)
        self.length = m
        self.height = n
        self.shape('circle')

    def plot(self):
        # Horizontal lines
        for i in range(self.height+1):
            self.goto(0, i*50)
            self.pd()
            self.goto(self.length*50, i*50)
            self.pu()

        # Vertical lines
        for i in range(self.length+1):
            self.goto(i*50, 0)
            self.pd()
            self.goto(i*50, self.height*50)
            self.pu()

        self.ht()


class Brick(turtle.Turtle):
    """
    coor means coordinate.
    Brick has four Attributes:
        1.left bottom coordinate
        2.right top coordinate
        3.right bottom coordinate
        4.left top coordinate
    """

    def __init__(self, position, m):
        turtle.Turtle.__init__(self)
        self.lbcoor = (position[0] % m, position[0] // m)
        self.rtcoor = ((position[-1] % m) + 1, (position[-1] // m) + 1)
        self.rbcoor = ((position[-1] % m) + 1, position[0] // m)
        self.ltcoor = (position[0] % m, (position[-1] // m) + 1)
        self.shape('blank')

    def plot(self):
        self.ht()
        self.pu()
        self.goto(i*50 for i in self.lbcoor)
        self.pensize(7)
        self.st()
        self.pd()
        self.goto(i*50 for i in self.rbcoor)
        self.goto(i*50 for i in self.rtcoor)
        self.goto(i*50 for i in self.ltcoor)
        self.goto(i*50 for i in self.lbcoor)
        self.ht()


class Serial(turtle.Turtle):
    def __init__(self, c, m):
        turtle.Turtle.__init__(self)
        x = c % m
        y = c // m
        self.coordinate = (x*50+25,y*50+25)
        self.value = str(c)
        self.shape('blank')

    def plot(self):
        self.pu()
        self.goto(self.coordinate)
        self.write(self.value, align="center", font=("Arial", 20, "normal"))


def visualize(solutions, m, n):
    """Visualize the solution using turtle."""
    # Locate the O point on the left bottom of the canvas.
    ref = max(m, n)
    turtle.setworldcoordinates(-10, -10, (ref*50)+10, (ref*50)+10)
    # Draw the grid
    grid = Grid(m, n)
    grid.plot()
    # numbers
    for c in [i for i in range(m*n)]:
        number = Serial(c, m)
        number.plot()
    # User input which solution to plot
    s = turtle.Screen().numinput('Select Plan', 'Input number of {0} - {1}'.format(0, len(solutions)-1),
                                 default=0, minval=0, maxval=len(solutions)-1)
    # Draw the tiles(bricks).
    for brick in solutions[int(s)]:
        sorted_brick = [i for i in brick]
        sorted_brick.sort()         # sort the list to ensure the maximum element has the index -1.
        Brick(sorted_brick, m).plot()
    
    turtle.Screen().mainloop()


def main():
    # User Input
    m = int(input('Please input the length of the wall:'))
    n = int(input('Please input the height of the wall:'))
    a = int(input('Please input the length of the tile:'))
    b = int(input('Please input the height of the tile:'))

    # Initialize
    initial_empty = [i for i in range(m*n)]
    initial_filled = []
    tile1 = Tile(a, b)
    tile2 = Tile(b, a)
    tiles = [tile1, tile2]

    # Solute and Print
    all_solutions = solute(initial_empty, initial_filled, tiles, m, n)
    for solution in all_solutions:
        solution.sort()
        print(solution)

    # Finish the process if there is no solution.
    if not all_solutions:
        print('No solution!')
        return 0

    # Visualize
    visualize(all_solutions, m, n)


main()
