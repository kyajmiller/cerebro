import pyodbc
from Classes.SUDBConnect import SUDBConnect
from Classes.Parser import Parser


class DatabaseHelper(SUDBConnect):
    @staticmethod
    def UseOnlyFirstRegex(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegEx

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useOnlyOneRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegExHelper

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useOnlyFirstRegexAndRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        searchCriteriaRegex = ''
        searchCriteriaRegexHelper = ''
        doBothMatch = False
        if len(rows) >= 1:
            searchCriteriaRegex = rows[0].RegEx
            searchCriteriaRegexHelper = rows[0].RegExHelper
        if Parser(stringToScan, searchCriteriaRegex).doesMatchExist() and Parser(stringToScan,
                                                                                 searchCriteriaRegexHelper).doesMatchExist():
            doBothMatch = True

        return doBothMatch

    @staticmethod
    def useAllRegex(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        regExArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
        searchCriteria = '|'.join(list(set(regExArray)))

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useAllRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExHelperArray.append(row.RegExHelper)
        searchCriteria = '|'.join(list(set(regExHelperArray)))

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useAllRegexAndRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regExArray = []
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
                regExHelperArray.append(row.RegExHelper)
        searchCriteriaRegex = '|'.join(regExArray)
        searchCriteriaRegexHelper = '|'.join(regExHelperArray)
        doBothMatch = False

        if Parser(stringToScan, searchCriteriaRegex).doesMatchExist() and Parser(stringToScan,
                                                                                 searchCriteriaRegexHelper).doesMatchExist():
            doBothMatch = True

        return doBothMatch

    @staticmethod
    def useOnlyFirstRegexTrue(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
        return Parser(stringToScan, regEx).doesMatchExist()

    @staticmethod
    def useOnlyFirstRegexHelperTrue(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regExHelper = ''
        if len(rows) >= 1:
            regExHelper = rows[0].RegExHelper
        return Parser(stringToScan, regExHelper).doesMatchExist()

    @staticmethod
    def useOnlyFirstRegexTrueRegexHelperTrue(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        regExHelper = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
            regExHelper = rows[0].RegExHelper
        if Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                           regExHelper).doesMatchExist() == True:
            return True
        elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                             regExHelper).doesMatchExist() == False:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == False:
            return False

    @staticmethod
    def useOnlyFirstRegexTrueRegexHelperFalse(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        regExHelper = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
            regExHelper = rows[0].RegExHelper
        if Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                           regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                             regExHelper).doesMatchExist() == False:
            return True
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == False:
            return False

    @staticmethod
    def useOnlyFirstRegexFalseRegexHelperTrue(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        regExHelper = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
            regExHelper = rows[0].RegExHelper
        if Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                           regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                             regExHelper).doesMatchExist() == False:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == True:
            return True
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == False:
            return False

    @staticmethod
    def useOnlyFirstRegexFalseRegexHelperFalse(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRowsDB(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        regExHelper = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
            regExHelper = rows[0].RegExHelper
        if Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                           regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                             regExHelper).doesMatchExist() == False:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == True:
            return False
        elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                              regExHelper).doesMatchExist() == False:
            return True


