import time
from base.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login("hotdogg@gmail.com")
        self.login_page.enter_password("Qwerty")
        self.login_page.check_mark_button()
        self.login_page.click_submit_button()
        time.sleep(15)
        self.dashboard_page.click_invite_button()
        time.sleep(15)
