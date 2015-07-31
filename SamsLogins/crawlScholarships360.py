# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrawlScholarships360(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://scholarships360.org"
        self.verificationErrors = []
        self.accept_next_alert = True
        ff = self.driver
        ff.get(self.base_url + "/")
        ff.find_element_by_link_text("Discover").click()
        time.sleep(5)
        ff.find_element_by_class_name("CoverPop-close").click()

    def test_crawl_scholarships360(self):
        driver = self.driver
        assert(driver.current_url == "https://scholarships360.org/discover-scholarships/")

        names = []
        inSiteLinks = []
        addedDates = []
        dueDates = []
        amounts = []
        eligibility = []
        websites = []
        emails = []
        scholarshipTypes = []

        while driver.find_elements_by_link_text('Next »') != []:
            nameObjects = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2/a')
            for item in nameObjects:
                names.append(item.text)
                inSiteLinks.append(item.get_attribute('href'))
            driver.find_elements_by_link_text('Next »')[0].click()
            print("clicky")
        else:
            print("no button found")

        print("AOK")
        


        #for each page:
        #-get names, get links
        #for each link:
        #-follow link
        #-get ADDED, DUE, AMOUNT
        #-look in text for "Who is eligible for" in an <h3>, and snatch the next paragraph after it. If it doesn't have it, don't freak out.
        #look for everything formatted like an email, and get the first one.
        #-click the APPLY button and copy link address.
        #use the Scholarship Type <select> to append scholarship types as a list to each. (?????)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
