"""
This file contains the Box class which holds all the information for
a planned box.
"""
import reportlab

from bs_config import Configuration

class Box():
    """
    Represents a box on a page. 

    In the diagram below, the * represents the (x,y) position of the box. (only helpful with monospace font)
    _______________________________
    |                    page      |
    |    _____________________     |
    |    |    __border___    |     |
    |    |    |* box     |   |     |
    |    |    |__________|   |     |
    |    |___________________|     |
    |                              |
    |                              |
    |                              |
    |______________________________|

    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lines = [Line(), Line, Line(), Line()]

    def draw():
        print("Drawing box")

class SummaryBox(Box):
    def __init__(self):
        print("creating summary box")

class Line():
    def __init__(self):
        pass

    def draw(self):
        pass
