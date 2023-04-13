import pytest
from Config.config import TestData
from Tests.test_Base import BaseTest
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_signup_link(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)





