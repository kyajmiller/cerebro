from Classes.SUDBConnect import SUDBConnect


class CollegeGreenLightLeadsGetDatabaseInfo(object):
    def __init__(self):
        self.db = SUDBConnect()

    def getDescriptions(self):
        descriptions = []

        rows = self.db.getRowsDB("select Description from dbo.CollegeGreenLightLeads")
        for row in rows:
            descriptions.append(row.Description)

        return descriptions

    def getSourceTexts(self):
        sourceTexts = []

        rows = self.db.getRowsDB("select SourceText from dbo.CollegeGreenLightLeads")
        for row in rows:
            sourceTexts.append(row.SourceText)

        return sourceTexts

    def getCollegeGreenLightLeadsIds(self):
        collegeGreenLightLeadIds = []

        rows = self.db.getRowsDB("select CollegeGreenLightLeadId from dbo.CollegeGreenLightLeads")
        for row in rows:
            collegeGreenLightLeadIds.append(str(row.CollegeGreenLightLeadId))

        return collegeGreenLightLeadIds

    def getSponsors(self):
        sponsors = []

        rows = self.db.getRowsDB("select * from dbo.CollegeGreenLightLeads")
        for row in rows:
            sponsors.append(row.Sponsor)

        return sponsors

    def getConcatenatedDescriptionSourceText(self):
        listConcatenatedItems = []

        descriptions = self.getDescriptions()
        sourceTexts = self.getSourceTexts()

        for i in range(len(descriptions)):
            description = descriptions[i]
            sourceText = sourceTexts[i]

            concatenatedItem = '%s %s' % (description, sourceText)
            listConcatenatedItems.append(concatenatedItem)

        return listConcatenatedItems
