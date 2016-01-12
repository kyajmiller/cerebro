from Classes.GoodCallLeads import GoodCallLeads
from Classes.InsertGoodCallLeadArrayIntoGoodCallLeadsDB import InsertGoodCallLeadArrayIntoGoodCallLeadsDB
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class ProcessGoodCallLeads(object):
    @staticmethod
    def getGoodCallLeadsAndInsertIntoDB():
        goodCallLeadsArrays = GoodCallLeads().getLeads()
        predictedFundingTypes = ProcessGoodCallLeads.classifyFunding(goodCallLeadsArrays)
        for leadArray, fundingClassification in zip(goodCallLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessGoodCallLeads.checkBadScholarship(leadArray, fundingClassification)
            InsertGoodCallLeadArrayIntoGoodCallLeadsDB(leadArray, fundingClassification, badScholarshipClassification)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = [leadArray[4] for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[5]
            infoText = leadArray[4]
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessGoodCallLeads.getGoodCallLeadsAndInsertIntoDB()
