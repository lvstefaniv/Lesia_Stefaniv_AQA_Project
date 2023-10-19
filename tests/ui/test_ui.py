import pytest

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    #Creating object for browser control
    driver = webdriver.Chrome(
        service = Service(r'/home/empeek/Стільниця/Lesia_Stefaniv_AQA_Project' + r'chromedriver')
        )
    
    #Open the page https://github.com/login
    driver.get("https://github.com/login")

    #Find a textfield for incorrect login
    login_elem = driver.find_element(By.ID, "login_field")

    #Enter incorrect username or email
    login_elem.send_keys("lesia_stefaniv@mistakeinmail.com")

    #Find a textfield for incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    #Enter incorrect password
    pass_elem.send_keys("wrong password")

    #Find a 'Sign in' button
    btn_elem = driver.find_element(By.NAME, "commit")
    
    #Click with the left mouse button
    btn_elem.click()

    #Check the expected page title
    assert driver.title == "Sign in to GitHub · GitHub"

    #Close the browser
    driver.close()