import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_001_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self):
        self.logger.info("**********************Test_001_AddCustomer**********************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserNmae(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************Login successful*****************")

        self.logger.info("********************Starting Add Customer********************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("*******************Providing customer info****************")

        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("John")
        self.addcust.setLastname("Richard")
        self.addcust.setCompanyName("Deloitte")
        self.addcust.setAdminContent("This is for testing..............")
        self.addcust.clickOnsave()

        self.logger.info("****************Saving customerv info********************")
        self.logger.info("*********************Add customer validation started***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added sucessfully.' in self.msg:
            assert True == True
            self.logger.info("*****************Add customer test passed*************")
        else:
            self.driver.save_screenshot("C:\Users\Rahul\PycharmProjects\Ecommerce\Screenshots")
            self.logger.error("*****************Add Customer Test Failed**************")
            assert True == False

            self.driver.close()
            self.logger.info("****************Ending Home Page Title Tset************")

    def random_generator(size=8,char=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(char) for x in range(size))