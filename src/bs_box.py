"""
This file contains the Box class which holds all the information for
a planned box.
"""
import reportlab

from bs_config import Configuration

class Box():
    def __init__(self):
        print("Hello from Box")
        self.lines = [Line(), Line, Line(), Line()]

    def draw():
        print("Drawing box")

class Line():
    def __init__(self):
        print("Hello from Line")

    def draw(self):
        print("Drawing line")
