from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class GrantForwardLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.grantforward.com/'

        self.arrayOfTitles = []
        self.arrayOfResultsPagesLinks = []
        self.arrayOfDescriptionsDiv = []
        self.arrayOfDescriptionsText = []
        self.arrayOfWebsiteLinks = []
        self.arrayOfGrantForwardLeads = []
        self.arrayOfResultsPageArrays = []

        self.driver.get(self.base_url + '/index')
        self.driver.find_element_by_id('keyword').clear()
        self.driver.find_element_by_id('keyword').send_keys(self.searchTerm)
        self.driver.find_element_by_xpath('//div[2]/button').click()
        self.driver.implicitly_wait(2)

    def processSearchResultsAndMakeLeadArray(self):
        self.getTitlesAndLinksFromSearchResults()
        '''
        isThereNextPage = self.checkIfNextPage()
        pageCount = 2
        while isThereNextPage == True and pageCount <= 10:
            self.goToNextPage()
            self.getTitlesAndLinksFromSearchResults()
            isThereNextPage = self.checkIfNextPage()
            pageCount += 1
        '''
        for singleArray in self.arrayOfResultsPageArrays:
            self.makeLeadArrayAndAddToGrantForwardLeads(singleArray)

        self.driver.quit()

        return self.arrayOfGrantForwardLeads

    def getTitlesAndLinksFromSearchResults(self):
        self.arrayOfTitles = self.driver.find_elements_by_xpath("//a[@class = 'grant-url']")
        self.arrayOfResultsPagesLinks = []
        for i in self.arrayOfTitles:
            self.arrayOfResultsPagesLinks.append(i.get_attribute('href'))

        for i in range(len(self.arrayOfTitles)):
            title = self.arrayOfTitles[i].text
            resultPageLink = self.arrayOfResultsPagesLinks[i]
            singleResultArray = [title, resultPageLink]
            self.arrayOfResultsPageArrays.append(singleResultArray)

    def makeLeadArrayAndAddToGrantForwardLeads(self, singleArray):
        name = singleArray[0]
        url = singleArray[1]
        resultPageInfo = self.goToResultPageAndPullInformation(url)

        keyword = self.searchTerm
        description = CleanText.cleanALLtheText(resultPageInfo[0])
        sponsor = CleanText.cleanALLtheText(resultPageInfo[1])
        amount = resultPageInfo[2]
        eligibility = CleanText.cleanALLtheText(resultPageInfo[3])
        submissionInfo = CleanText.cleanALLtheText(resultPageInfo[4])
        categories = CleanText.cleanALLtheText(resultPageInfo[5])
        opportunitySourceLink = resultPageInfo[6]
        # opportunitysourceText = CleanText.cleanALLtheText(RipPage.getPageSource(opportunitySourceLink))

        singleLeadArray = [keyword, url, name, description, sponsor, amount, eligibility, submissionInfo, categories,
                           opportunitySourceLink]

        self.arrayOfGrantForwardLeads.append(singleLeadArray)

    def goToResultPageAndPullInformation(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)
        description = ''
        sponsor = ''
        amount = ''
        eligibility = ''
        submissionInfo = ''
        categories = ''
        opportunitySourceLink = ''

        if self.checkIfElementExists("//div[@id = 'field-description']/div[@class = 'content-collapsed']"):
            descriptionDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-description']/div[@class = 'content-collapsed']")
            description = descriptionDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'sponsor-content']/div/a"):
            sponsorDiv = self.driver.find_element_by_xpath("//div[@class = 'sponsor-content']/div/a")
            sponsor = sponsorDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']"):
            amountDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']")
            amount = amountDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']"):
            eligibilityDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']")
            eligibility = eligibilityDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']"):
            submissionInfoDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']")
            submissionInfo = submissionInfoDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@id = 'field-subjects']/ul"):
            categoriesDiv = self.driver.find_element_by_xpath("//div[@id = 'field-subjects']/ul")
            categories = categoriesDiv.get_attribute('textContent')

        if self.checkIfElementExists("//a[@class = 'source-link btn btn-warning']"):
            opportunitySourceLinkDiv = self.driver.find_element_by_xpath("//a[@class = 'source-link btn btn-warning']")
            opportunitySourceLink = opportunitySourceLinkDiv.get_attribute('href')

        resultPageInfo = [description, sponsor, amount, eligibility, submissionInfo, categories, opportunitySourceLink]
        return resultPageInfo

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_xpath("(//a[contains(text(), 'Next')])[1]")
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPage(self):
        self.driver.find_element_by_xpath("(//a[contains(text(), 'Next')])[1]").click()
        self.driver.implicitly_wait(2)

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False


test = GrantForwardLeads('engineering').processSearchResultsAndMakeLeadArray()
for i in test[0]:
    print(i)