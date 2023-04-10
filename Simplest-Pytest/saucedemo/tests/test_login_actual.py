# selenium 4
from selenium.webdriver.common.by import By
import time


def test_login_actual(setup):
    driver = setup
    time.sleep(2)
    username = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    title = driver.find_element(By.CLASS_NAME, 'title').text
    assert title == 'Products'
