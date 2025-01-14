import nltk.data
from SUDBConnect import SUDBConnect
from PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from GPA import GPA
from DueDate import DueDate


class PopulatePivotLeadRequirements(object):
    def __init__(self, listOfMajors):
        self.listOfMajors = listOfMajors
        self.db = SUDBConnect()
        self.tag = 'Scholarship'
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        self.loopThroughListOfMajorsAndDoStuff()

    def loopThroughListOfMajorsAndDoStuff(self):
        for major in self.listOfMajors:
            pivotLeadsDatabaseInfo = PivotLeadsGetDatabaseInfo(major, self.tag)
            listOfPivotLeadsIds = pivotLeadsDatabaseInfo.getPivotLeadId()
            listOfConcatenatedAbstractEligibilities = pivotLeadsDatabaseInfo.getListStringConcatendatedAbstractEligibility()
            listOfSourceTexts = pivotLeadsDatabaseInfo.getSourceText()

            for i in range(len(listOfPivotLeadsIds)):
                pivotLeadId = str(listOfPivotLeadsIds[i])

                abstractEligibility = listOfConcatenatedAbstractEligibilities[i].strip()
                abstractEligibilitySentences = self.tokenizeAbstractEligibilityIntoSentences(abstractEligibility)

                sourceText = listOfSourceTexts[i]
                sourceTextSentences = self.tokenizeAbstractEligibilityIntoSentences(sourceText)

                gpa = self.getGPAFromAbstractEligibility(abstractEligibilitySentences)
                dueDate = self.getDueDateFromSourceText(sourceTextSentences)

                self.populatePivotLeadRequirements(pivotLeadId, major, gpa, dueDate)

    def getGPAFromAbstractEligibility(self, abstractEligibilitySentences):
        gpa = []
        for sentence in abstractEligibilitySentences:
            maybeGPA = GPA(sentence).getGPA()
            if maybeGPA != '':
                gpa.append(maybeGPA)

        gpa = list(set(gpa))
        gpa = ', '.join(gpa)

        return gpa

    def getDueDateFromSourceText(self, sourceTextSentences):
        dueDate = ''

        for sentence in sourceTextSentences:
            if len(sentence) <= 1000:
                maybeDueDate = DueDate(sentence).getDueDate()
                if maybeDueDate != '':
                    dueDate = maybeDueDate

        return dueDate

    def tokenizeAbstractEligibilityIntoSentences(self, abstractEligibility):
        sentences = self.sentenceTokenizer.tokenize(abstractEligibility)
        return sentences

    def populatePivotLeadRequirements(self, pivotLeadId, major, gpa, dueDate):
        self.insertMajorIntoPivotLeadsRequirements(pivotLeadId, major)

        if gpa != '':
            self.insertGPAIntoPivotLeadsRequirements(pivotLeadId, gpa)

        if dueDate != '':
            self.insertDueDateIntoPivotLeads(pivotLeadId, dueDate)

    def insertMajorIntoPivotLeadsRequirements(self, pivotLeadId, major):
        attributeId = '417'
        attributeValue = major

        self.db.insertUpdateOrDeleteDB(
            "insert into dbo.PivotLeadRequirements (PivotLeadId, AttributeId, AttributeValue) values ('" + pivotLeadId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertGPAIntoPivotLeadsRequirements(self, pivotLeadId, gpa):
        attributeId = '1'
        attributeValue = gpa

        self.db.insertUpdateOrDeleteDB(
            "insert into dbo.PivotLeadRequirements (PivotLeadId, AttributeId, AttributeValue) values ('" + pivotLeadId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertDueDateIntoPivotLeads(self, pivotLeadId, dueDate):
        self.db.insertUpdateOrDeleteDB(
            "update dbo.PivotLeads set DueDate='" + dueDate + "' where PivotLeadId='" + pivotLeadId + "'")
