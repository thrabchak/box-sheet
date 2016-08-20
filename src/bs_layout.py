"""
This file contains the Layout class which holds all the information for
a planned box sheet export. 
"""
from bs_config import Configuration
from bs_box import Box

class Layout():
    def __init__(self, configuration):
        self.boxes = []

    def getNumRows(self):
        print("getting num rows")

    def getNumColumns(self);
        print("getting num columns")

    def createPdf(self):
        print("Creating layout PDF")
