import allure
import time
from base.base_test import BaseTest
from data.credentials import Credentials


@allure.epic("User")
@allure.feature("Login")
class TestLogin(BaseTest):

    @allure.story("Login in account")
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        time.sleep(5)
        self.login_page.check_mark_button()
        self.login_page.click_submit_button()
        time.sleep(5)
        self.dashboard_page.click_invite_button()
