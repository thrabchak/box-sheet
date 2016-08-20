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
	
	rows = self.getNumFit(config.pageHeight, config.pageMargin, config.boxHeight, config.boxMargin, config.border)
	cols = self.getNumFit(config.pageWidth, config.pageMargin, config.boxWidth, config.boxMargin, config.border)

	if(rows < 1 or cols < 1):
            print("Cannot fit any boxes on the page.")
	    return None

	# determine boxMarginPadding	
	rowPads = self.getNumPads(rows)
	rowPadSize = self.getPadSize(config.pageHeight, config.pageMargin, config.boxHeight, config.boxMargin, config.border, rows)
	colPads = self.getNumPads(cols)
	colPadSize = self.getPadSize(config.pageWidth, config.pageMargin, config.boxWidth, config.boxMargin, config.border, cols)

    def getNumFit(self, pageSize, pageMargin, boxSize, boxMargin, boxBorder):
	"""
	Returns the number of boxes that can fit in a given page size. This calculation
	can be used both for the width and the height. If a value of <1 is returned then
	no boxes can be created and we are in an error state. This would happen if the
	page size is too small for the requested box size and margin combination.

	This will return the maximum full boxes that can be placed in the given area. In
	order to center the boxes, we will add to the boxMargin.

	Calculation:

	pageSize = pageMargin + (boxBorder + boxSize + boxBorder) + boxMargin + ... + boxMargin + (boxBorder + boxSize + boxBorder) + pageMargin
		 = (2 * pageMargin) + (2 * boxBorder + boxSize) + n * (2 * boxBorder + boxSize + boxMargin) 
	"""

	boxArea = boxSize + 2 * boxBorder
	return 1 + (pageSize - 2 * pageMargin - boxArea) // (boxArea + boxMargin)
    
    def getNumPads(self, numBoxes):
	"""
	Returns the number of pads to be used in order to center the boxes.
	"""

	if numBoxes == 1:
	    return 2
	else:
	    return numBoxes - 1
    def getPadSize(self, pageSize, pageMargin, boxSize, boxMargin, boxBorder, numBoxes):
	return 0

    def createPdf(self):
	if(self.boxes == None):
	    print("Cannot create boxes.")
	    return None
        
	print("Creating layout PDF")

