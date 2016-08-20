"""
This is the main file for creating a box sheet.
"""
import argparse

from bs_config import Configuration 
from bs_layout import Layout

class BoxSheet():
    def __init__(self, args):
        self.args = args

    def main(self):
        self.configuration = Configuration(args)
        self.layout = Layout(self.configuration)
        self.layout.createPdf()

if __name__== "__main__":
    # Handle arguments
    parser = argparse.ArgumentParser(description='Create a PDF filled with boxes of a chosen size.')
    parser.add_argument('output', help='output path of the box sheet PDF')
    parser.add_argument('-c', '--config', help='configuration json file for inputing all parameters at once')
    args = parser.parse_args()
    
    # Create BoxSheet given args
    bs = BoxSheet(args)
    bs.main()
