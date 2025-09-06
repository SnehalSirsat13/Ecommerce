import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self):
        self.logger.info("******************Search Customer By Email*******************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserNmae(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************Login Successful************")

        self.logger.info("******************strating search customer by email*************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("*****************Search customer by emailid*****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("Pjffx@gmail.com")
        searchcust.clickSearch()
        time.sleep(3)

        status = searchcust.searchCustomerByEmail("Pjffx@gmail.com")
        assert True == status

        self.logger.info("*************************Test_Search Customer By Email is finished************")










