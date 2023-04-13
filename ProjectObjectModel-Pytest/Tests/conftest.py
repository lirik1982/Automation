import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        options = Options()
        options.page_load_strategy = 'normal'
        web_driver = webdriver.Chrome(options=options)
    if request.param == "firefox":
        options = Options()
        options.page_load_strategy = 'normal'
        web_driver = webdriver.Firefox(options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()

