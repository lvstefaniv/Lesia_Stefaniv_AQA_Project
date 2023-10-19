from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #Find a textfield for incorrect login
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Enter incorrect username or email
        login_elem.send_keys(username)

        #Find a textfield for incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")

        #Enter incorrect password
        pass_elem.send_keys(password)

        #Find a 'Sign in' button
        btn_elem = self.driver.find_element(By.NAME, "commit")
    
        #Click with the left mouse button
        btn_elem.click()

    def check_title(self, expexted_title):
        return self.driver.title == expexted_title