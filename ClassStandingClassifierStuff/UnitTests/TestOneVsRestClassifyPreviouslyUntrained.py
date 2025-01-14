import unittest
from ClassStandingClassifierStuff.OneVsRestClassifyPreviouslyUntrained import \
    OneVsRestClassifyPreviouslyUntrained
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_OVRClassifier(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                            trainingPercentage=0.8)
        testClassify.trainTestAndDisplayResults()

    def test_makeSureTheLabelsListIsAListOfListsOfStrings(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                            trainingPercentage=0.8)

        trainingSet = testClassify.trainingSet
        trainingLabels = [training['label'] for training in trainingSet]
        self.assertEqual(type(trainingLabels), list)
        self.assertEqual(type(trainingLabels[1]), list)
        self.assertEqual(type(trainingLabels[1][0]), str)


if __name__ == '__main__':
    unittest.main()
