"""
This file contains the Layout class which holds all the information for
a planned box sheet export. 
"""
from bs_config import Configuration
from bs_box import Box

class Layout():
    def __init__(self, configuration):
            self.config = configuration
            self.boxes = self.createBoxes()

    def createBoxes(self):
            config = self.config

            rows, rowSize = self.getFit(config.pageHeight, config.pageMargin, config.boxHeight, config.boxMargin, config.border)
            cols, colSize = self.getFit(config.pageWidth, config.pageMargin, config.boxWidth, config.boxMargin, config.border)

            if(rows < 1 or cols < 1):
                print("Cannot fit any boxes on the page.")
                return None

            # determine boxMarginPadding    
            rowPads = self.getNumPads(rows)
            rowPadSize = self.getPadSize(config.pageHeight, rowSize, rowPads)
            colPads = self.getNumPads(cols)
            colPadSize = self.getPadSize(config.pageWidth, colSize, colPads)

            # create Box objects
            boxes = []
            for row in range(rows):
                boxRow = []
                rowValue = self.getRowValue(row)
                for col in range(cols):
                    colValue = self.getColValue(col)
                    boxRow.append(Box(colValue, rowValue, config.boxWidth, config.boxHeight))

            return boxes

    def getRowValue(self, row):
        return 0

    def getColValue(self, col):
        return 0

    def createPdf(self):
            """
            Creates a PDF of this box layout.
            """
            if(self.boxes == None):
                print("Cannot create boxes.")
                return 1

            print("Creating layout PDF")
            return 0

    @staticmethod
    def getFit(pageSize, pageMargin, boxSize, boxMargin, boxBorder):
            """
            Returns the number of boxes that can fit in a given page size and the actual size it takes up.
            This calculation can be used both for the width and the height. If a num value of <1 is returned
            then no boxes can be created and we are in an error state. This would happen if the
            page size is too small for the requested box size and margin combination.

            This will return the maximum full boxes that can be placed in the given area. In
            order to center the boxes, we will add to the boxMargin.

            Calculation:

            pageSize = pageMargin + (boxBorder + boxSize + boxBorder) + boxMargin + ... + boxMargin + (boxBorder + boxSize + boxBorder) + pageMargin
                     = (2 * pageMargin) + (2 * boxBorder + boxSize) + n * (2 * boxBorder + boxSize + boxMargin) 
            """
            #Error Cases
            if(pageSize <= 0):
                print("Page must be greater than zero.")
                return 0, 0
            elif(pageMargin > pageSize):
                print("Page margin must be greater than page size.")
                return 0, 0
            elif(boxSize > pageSize):
                print("Box size must be smaller than page size.")
                return 0, 0
            elif(boxSize <= 0):
                print("Box size must be greater than zero.")
                return 0, 0

            boxArea = boxSize + 2 * boxBorder
            num =  1 + (pageSize - 2 * pageMargin - boxArea) // (boxArea + boxMargin)
            size = 2 * pageMargin + (num - 1) * (boxArea + boxMargin) + boxArea

            return num, size
    
    @staticmethod
    def getNumPads(numBoxes):
            """
            Returns the number of pads to be used in order to center the boxes.
            """

            if numBoxes == 1:
                return 2
            else:
                return numBoxes - 1

    @staticmethod
    def getPadSize(pageSize, actualSize, numPads):
            return (pageSize - actualSize) / numPads
