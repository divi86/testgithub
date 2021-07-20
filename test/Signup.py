
from selenium.webdriver.common.by import By
from test import Locators

class SignUpPage:
    def __init__(self, driver):
        self.txt_fn = driver.find_element(By.NAME, Locators.firstname_name)
        self.txt_ln = driver.find_element(By.NAME, Locators.lastname_name)


    def getTxtfn(self):
        return self.txt_fn

    def getTxtln(self):
        return self.txt_ln