from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB(object):
    def __init__(self, scholarsiteLeadArray, fundingClassification, badScholarshipClassification):
        self.scholarsiteLeadArray = scholarsiteLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.scholarsiteLeadArray[0]
        self.amount = self.scholarsiteLeadArray[1]
        self.deadline = self.scholarsiteLeadArray[2]
        self.requirements = self.scholarsiteLeadArray[3]
        self.annualAwards = self.scholarsiteLeadArray[4]
        self.major = self.scholarsiteLeadArray[5]
        self.academicLevel = self.scholarsiteLeadArray[6]
        self.qualifiedMinorities = self.scholarsiteLeadArray[7]
        self.eligibleInstitution = self.scholarsiteLeadArray[8]
        self.eligibleRegion = self.scholarsiteLeadArray[9]
        self.usCitizen = self.scholarsiteLeadArray[10]
        self.usResident = self.scholarsiteLeadArray[11]
        self.foreignNational = self.scholarsiteLeadArray[12]
        self.minimumAge = self.scholarsiteLeadArray[13]
        self.maximumAge = self.scholarsiteLeadArray[14]
        self.classRank = self.scholarsiteLeadArray[15]
        self.minimumGPA = self.scholarsiteLeadArray[16]
        self.minimumACT = self.scholarsiteLeadArray[17]
        self.minimumSAT = self.scholarsiteLeadArray[18]
        self.date = time.strftime('%Y%m%d')

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.ScholarsiteLeads where Name='" + self.name + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def writeFileToDisk(self):
        tableName = 'ScholarsiteLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.ScholarsiteLeads where Name='" + self.name + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, '', self.date)

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDeleteDB(
                    "insert into dbo.ScholarsiteLeads (Name, Amount, Deadline, Requirements, AnnualAwards, Major, AcademicLevel, QualifiedMinorities, EligibleInstitution, EligibleRegion, USCitizen, USResident, ForeignNational, MinimumAge, MaximumAge, ClassRank, MinimumGPA, MinimumACT, MinimumSAT, Tag, BadScholarship, Date) values (N'" + self.name + "', N'" + self.amount + "', '" + self.deadline + "', N'" + self.requirements + "', N'" + self.annualAwards + "', N'" + self.major + "', N'" + self.academicLevel + "', N'" + self.qualifiedMinorities + "', N'" + self.eligibleInstitution + "', N'" + self.eligibleRegion + "', N'" + self.usCitizen + "', N'" + self.usResident + "', N'" + self.foreignNational + "', '" + self.minimumAge + "', '" + self.maximumAge + "', N'" + self.classRank + "', N'" + self.minimumGPA + "', N'" + self.minimumACT + "', N'" + self.minimumSAT + "', N'" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.ScholarsiteLeads set Amount=N'" + self.amount + "', Deadline=N'" + self.deadline + "', Requirements=N'" + self.requirements + "', AnnualAwards='" + self.annualAwards + "', Major='" + self.major + "', AcademicLevel=N'" + self.academicLevel + "', QualifiedMinorities=N'" + self.qualifiedMinorities + "', EligibleInstitution=N'" + self.eligibleInstitution + "', EligibleRegion=N'" + self.eligibleRegion + "', USCitizen='" + self.usCitizen + "', USResident='" + self.usResident + "', ForeignNational='" + self.foreignNational + "', MinimumAge='" + self.minimumAge + "', MaximumAge='" + self.maximumAge + "', ClassRank='" + self.classRank + "', MinimumGPA='" + self.minimumGPA + "', MinimumACT='" + self.minimumACT + "', MinimumSAT='" + self.minimumSAT + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassificaion + "', Date='" + self.date + "' where Name='" + self.name + "'")
            self.insertUpdateLead()
            return False
