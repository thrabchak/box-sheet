"""
This file contains the Configuration class which can be queried for config info. 
"""
class Configuration():
    def __init__(self, args):
        # Defaults config values
        self.boxWidth = 3
        self.boxHeight = 5
        self.pageWidth = 100
	self.pageHeight = 250
	self.pageMargin = 5
        self.boxMargin = 2
        self.border = 1
        self.isLandscape = False
        self.jsonConfig = None

        # Parse json
        if self.jsonConfig != None:
            self.parseJson()

        # Parse args
        self.parseArgs(args)

    def parseArgs(self, args):
        print("Parsing args")

    def parseJson(self):
        print("Parsing json config file")

