from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer():
    lnkCustomer_menu_xpath ="//body/div[@class='wrapper']/aside[@class='main-sidebar sidebar-dark-primary elevation-4']/div[@class='sidebar']/nav[@class='mt-2']/ul[@role='menu']/li[@class='nav-item has-treeview menu-is-opening menu-open']/a[1]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']"
    lstitemAminstrator_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuest_xpath = "//list[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//list[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment'}"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=='female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrator':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAminstrator_xpath)
        elif role=='Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        time.sleep(3)

        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(content)

    def clickOnsave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()







