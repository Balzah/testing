import time

import configuration as config
from page_model import BeeHotel
import allure
import os
#allure
#python -m pytest --alluredir=./allure-result
#allure serve ./allure-result

class TestBeeHotel:

    def setup_method(self):
        self.page = BeeHotel(config.get_preconfigured_chrome_driver())
        self.page.open()

    def teardown_method(self):
        self.page.close()

    @allure.id("TC1")
    @allure.title("Bejelentkezés BeeKeeper adatokkal.")
    def test_login_BeeKeeper(self):
        self.page.login_btn().click()
        self.page.login_username_input().send_keys("blaisevagyblue1@hotmail.com")
        self.page.login_password_input().send_keys("123Bazsi")
        time.sleep(1)
        self.page.login_submit_btn().click()
        time.sleep(1)
        assert self.page.my_profile_btn().is_displayed()

    @allure.id("TC2")
    @allure.title("Bejelentkezés BeeFamily adatokkal.")
    def test_login_BeeFamily(self):
        self.page.login_btn().click()
        self.page.login_username_input().send_keys("blaisevagyblue@hotmail.com")
        self.page.login_password_input().send_keys("123Bazsi")
        time.sleep(1)
        self.page.login_submit_btn().click()
        time.sleep(1)
        assert self.page.my_profile_btn().is_displayed()