"""
This file tests src/bs_config.py
"""
import unittest

from box_sheet import BoxSheet

class jsonParseTest(unittest.TestCase):

    def testDefaultBoxSheet(self):
        """
        Default box sheet
        """
        bs = BoxSheet()
        retval  = bs.main()
        assert retval == 0, "Error creating default box sheet"
