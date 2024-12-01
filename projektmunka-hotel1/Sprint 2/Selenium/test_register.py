import time
from selenium import webdriver
import configuration as config
from page_model import BeeHotel
import allure
import os

class TestBeeHotel:

    def setup_method(self):
        self.driver = config.get_preconfigured_chrome_driver()
        self.page = BeeHotel(self.driver)
        self.page.open()

    def teardown_method(self):
       self.page.close()

    @allure.id("TC1")
    @allure.title("Regisztráció valid adatokkal.")
    def test_registration_VALID(self):
        email = self.page.create_random_email()

        self.page.register_btn().click()
        self.page.input_firstname().send_keys("Niumka")
        self.page.input_lastname().send_keys("Sele")
        self.page.input_email().send_keys(email)
        self.page.input_phone_number().send_keys("061234567")
        self.page.input_reg_password().send_keys("Selenium1")
        self.page.input_zip_code().send_keys(1234)
        self.page.input_city().send_keys("Buda")
        self.page.input_address().send_keys("Kalocs u. 1")
        self.page.select_role().select_by_value("ROLE_BEEKEEPER")
        time.sleep(1)
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "rak.PNG"))
        self.page.input_file_upload().send_keys(upload_file)
        time.sleep(2)

        self.page.register_submit_btn().click()


        time.sleep(5)
        code = self.page.verification_code2(email)

        self.page.input_verify_email().send_keys(email)
        self.page.input_verify_pass_code().send_keys(code)
        self.page.verify_registration_btn().click()

        assert self.page.verify_success_message().is_displayed()

    @allure.id("TC2")
    @allure.title("Regisztráció invalid jelszóval.")
    def test_registration_INVALID_password(self):
        self.page.register_btn().click()
        self.page.input_firstname().send_keys("Niu")
        self.page.input_lastname().send_keys("Sel")
        self.page.input_phone_number().send_keys("061234567")
        self.page.input_email().send_keys("ritad19776@glaslack.com")
        self.page.input_reg_password().send_keys("S1")
        self.page.input_zip_code().send_keys(1234)
        self.page.input_city().send_keys("Buda")
        self.page.input_address().send_keys("Kalocs u. 1")
        self.page.select_role().select_by_value("ROLE_BEEKEEPER")
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "rak.PNG"))
        self.page.input_file_upload().send_keys(upload_file)

        assert self.page.error_message().is_displayed()
        assert self.page.error_message().text == "Your password must contain at least 8 letters and have a capital letter plus a number!"

#allure
#python -m pytest --alluredir=./allure-result
#allure serve ./allure-result