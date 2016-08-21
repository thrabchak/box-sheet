"""
This file tests src/box_sheet.py
"""
import unittest

from box_sheet import BoxSheet

class BoxSheetTest(unittest.TestCase):

    def testDefaultBoxSheet(self):
        """
        Default box sheet
        """
        bs = BoxSheet()
        retval  = bs.main()
        assert retval == 0, "Error creating default box sheet"
