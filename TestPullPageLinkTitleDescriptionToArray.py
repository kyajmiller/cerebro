import unittest
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.RipPage import RipPage

class TestStringMethods(unittest.TestCase):
    def test_PullPageLinkTitleDescriptionToArrayGetTitle(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray(RipPage.getPageSource('https://www.google.com/'))
        self.assertIsNotNone(testPullPageLinkTitleDescriptionToArray.getTitle())
        self.assertEqual('Google', testPullPageLinkTitleDescriptionToArray.getTitle())

    def test_PullPageLinkTitleDescriptionToArrayGetDescription(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('https://www.google.com/'))
        self.assertNotEqual('', testPullPageLinkTitleDescriptionToArray.getDescription())
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getDescription()), 10)

    def test_PullPageLinkTitleDescriptionToArrayGetPageURL(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('http://grandcanyon.com'))
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getPageURL()), 10)

    def test_PullPageLinkTitleDescriptionToArrayGetAllURLsOnPage(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('http://grandcanyon.com'))
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getAllURLsOnPage()), 1)
        print(testPullPageLinkTitleDescriptionToArray.getAllURLsOnPage())

if __name__ == '__main__':
    unittest.main()