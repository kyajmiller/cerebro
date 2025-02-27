import re
from Classes.Parser import Parser
from Classes.ScholarshipPackageRequirementFormat import ScholarshipPackageRequirement


class GPA(Parser):
    def __init__(self, stringToScan, scholarshipPackageId='0'):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, '\s[^$\d\.]?[1234]\.\d+')
        self.resultList = []
        self.attributeId = '1'
        self.gpa = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '>='
        self.scholarshipPackageId = scholarshipPackageId

    def checkContext(self, contextRegex):
        contextChecker = Parser(self.stringToScan.lower(), contextRegex)
        return contextChecker.doesMatchExist()

    def getGPA(self):
        if self.checkContext('g\.?p\.?a\.?|grade\spoint\saverage|maintain\sa') and self.doesMatchExist():
            for i in self.getResult():
                i = re.sub('\(', '', i)
                self.resultList.append(i.strip())
        elif self.doesMatchExist():
            if not self.checkContext('million|billion|trillion|version|dollar|pound|euro'):
                for i in self.getResult():
                    i = re.sub('\(', '', i)
                    self.resultList.append(i.strip())

        if self.checkContext('4\.0\sscale') and self.doesMatchExist():
            if '4.0' in self.resultList:
                self.resultList.remove('4.0')

        self.resultList = list(set(self.resultList))

        if len(self.resultList) >= 2:
            self.logicGroup = '1'

        self.gpa = ', '.join(self.resultList)
        return self.gpa

    def getScholarshipPackageRequirementFormat(self):
        self.getGPA()
        if self.getGPA() != '':
            GPA_SPRF = ScholarshipPackageRequirement(self.scholarshipPackageId, self.attributeId,
                                                     self.requirementTypeCode, self.getGPA(), self.logicGroup)

            return GPA_SPRF
