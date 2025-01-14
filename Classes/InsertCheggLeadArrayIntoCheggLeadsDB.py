from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertCheggLeadArrayIntoCheggLeadsDB(object):
    def __init__(self, cheggLeadArray, fundingClassification, badScholarshipClassification):
        self.cheggLeadArray = cheggLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.cheggLeadArray[0]
        self.url = self.cheggLeadArray[1]
        self.deadline = self.cheggLeadArray[2]
        self.amount = self.cheggLeadArray[3]
        self.eligibility = self.cheggLeadArray[4]
        self.applicationOverview = self.cheggLeadArray[5]
        self.description = self.cheggLeadArray[6]
        self.sponsor = self.cheggLeadArray[7]
        self.sourceWebsite = self.cheggLeadArray[8]
        self.sourceText = self.cheggLeadArray[9]
        self.date = time.strftime('%Y%m%d')

    def writeFileToDisk(self):
        tableName = 'CheggLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.CheggLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.CheggLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                    "insert into dbo.CheggLeads (Name, Url, Deadline, Amount, Eligibility, ApplicationOverview, Description, Sponsor, SourceWebsite, SourceText, Date, Tag, BadScholarship) values (N'" + self.name + "', N'" + self.url + "', N'" + self.deadline + "', N'" + self.amount + "', N'" + self.eligibility + "', N'" + self.applicationOverview + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.CheggLeads set Deadline=N'" + self.deadline + "', Amount=N'" + self.amount + "', Eligibility=N'" + self.eligibility + "', ApplicationOverview=N'" + self.applicationOverview + "', Description=N'" + self.description + "', Sponsor=N'" + self.sponsor + "', SourceWebsite=N'" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Date='" + self.date + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassificaion + "' where Name='" + self.name + "' and Url='" + self.url + "'")
            self.writeFileToDisk()
            return False
