import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig



class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()


    def test_homepageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\Rahul\PycharmProjects\Ecommerce\Screenshots")
            self.driver.close()
            assert False


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.lp=Login(self.driver)
        self.lp.setUserNmae(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\Rahul\PycharmProjects\Ecommerce\Screenshots")
            self.driver.close()
            assert False
