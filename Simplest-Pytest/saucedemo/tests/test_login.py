# selenium 4
from selenium.webdriver.common.by import By
import time


def test_login_simple(setup):
    driver = setup


def test_login_check(setup):
    driver = setup
    username = driver.find_element(By.ID, 'user-name').is_displayed()
    assert username == True
    password = driver.find_element(By.ID, 'password').is_displayed()
    assert password == True
    login_button = driver.find_element(By.ID, 'login-button').is_displayed()
    assert login_button == True


