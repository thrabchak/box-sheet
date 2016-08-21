"""
This file tests src/layout.py
"""
import unittest

from bs_layout import Layout

class FitTest(unittest.TestCase):

    def testOneBoxFit(self):
        """
        One box fits

        pageSize = pageMargin + (boxBorder + boxSize + boxBorder) + boxMargin + ... + boxMargin + (boxBorder + boxSize + boxBorder) + pageMargin
        
        pageSize = 9
        actualSize = 1 + (1 + 2 + 1) + 1 = 6

        """
        pageSize = 9
        pageMargin = 1
        boxSize = 2
        boxMargin = 2
        boxBorder = 1
        num, size = Layout.getFit(pageSize, pageMargin, boxSize, boxMargin, boxBorder)
        assert num == 1, "Given num: " + str(num)
        assert size == 6, "Given size: " + str(size)

    def testTwoBoxesFit(self):
        """
        Two boxes fit

        pageSize = pageMargin + (boxBorder + boxSize + boxBorder) + boxMargin + ... + boxMargin + (boxBorder + boxSize + boxBorder) + pageMargin
        
        pageSize = 15
        actualSize = 2 + (1 + 2 + 1) + 2 + (1 + 2 + 1)  + 2 = 14

        """
        pageSize = 15
        pageMargin = 2
        boxSize = 2
        boxMargin = 2
        boxBorder = 1
        num, size = Layout.getFit(pageSize, pageMargin, boxSize, boxMargin, boxBorder)
        assert num == 2, "Given num: " + str(num)
        assert size == 14, "Given size: " + str(size)

    def testZeroBoxSize(self):
        """
        Box size of 0
        """
        pageSize = 15
        pageMargin = 2
        boxSize = 0
        boxMargin = 2
        boxBorder = 1
        num, size = Layout.getFit(pageSize, pageMargin, boxSize, boxMargin, boxBorder)
        assert num == 0, "Given num: " + str(num)
        assert size == 0, "Given size: " + str(size)

    def testZeroPageSize(self):
        """
        No page size
        """
        num, size = Layout.getFit(0, 0, 1, 0, 0)
        assert num < 1, "Given num: " + str(num)

    def testPageMarginGreaterThanPageSize(self):
        """
        Page margin greater than page size
        """
        pageSize = 15
        pageMargin = 15
        boxSize = 0
        boxMargin = 2
        boxBorder = 1
        num, size = Layout.getFit(pageSize, pageMargin, boxSize, boxMargin, boxBorder)
        assert num == 0, "Given num: " + str(num)
        assert size == 0, "Given size: " + str(size)

class CreateBoxesTest(unittest.TestCase):

    def testBoxesOnPage(self):
        """
        Boxes on page

        Tests to make sure all boxes created are actually on the page.
        """
        pass

    def testBoxesHonorMargin(self):
        """
        Boxes within margin

        Tests to make sure all boxes created are within the given margin.
        """
        pass

    def testBoxesAtLeastBoxMarginApart(self):
        """
        Boxes spaced by box margin

        Tests to make sure all boxes are at least the box margin apart.
        """
        pass

    def testBoxesCorrectSize(self):
        """
        Box size
        """
        pass

