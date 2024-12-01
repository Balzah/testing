import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from general_page import GeneralPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import http.client
import json
from datetime import datetime
import hashlib
class BeeHotel(GeneralPage):
    def __init__(self, browser: Chrome):
        super().__init__(browser, url='http://localhost:4200/')

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def register_btn(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,'//button/a[@class="nav-link"]')))[1]

    def input_firstname(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'firstName')))

    def input_lastname(self):
        return self.browser.find_element(By.ID, "lastName")

    def input_phone_number(self):
        return self.browser.find_element(By.ID, "phoneNumber")

    def input_email(self):
        return self.browser.find_element(By.ID, "email")

    def input_reg_password(self):
        return self.browser.find_element(By.ID, "password")

    def input_zip_code(self):
        return self.browser.find_element(By.ID, "zipcode")

    def input_city(self):
        return self.browser.find_element(By.ID, "city")

    def input_address(self):
        return self.browser.find_element(By.ID, "address")

    def select_role(self):
        return Select(self.browser.find_element(By.ID, 'role'))

    def input_file_upload(self):
        return self.browser.find_element(By.ID, "featureImageUrl")

    def register_submit_btn(self):
        return WebDriverWait(self.browser, 9).until(EC.element_to_be_clickable((By.XPATH, "//form//button")))

    def login_btn(self):
        return self.browser.find_elements(By.XPATH,'//button[@class="custom-button"]')[2]

    def login_username_input(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, "username")))

    def login_password_input(self):
        return self.browser.find_element(By.ID, "password")

    def login_submit_btn(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH,'//button[@class="btn button"]')))

    def error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//small[@class="text-danger"]')))

    def verify_success_message(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//small')))

    def my_profile_btn(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH,'//button/a[@class="nav-link"]')))[4]

    def input_verify_email(self):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.ID,"emailV")))

    def input_verify_pass_code(self):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.ID,"verificationCode")))

    def verify_registration_btn(self):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH,'//button[@class="btn btn-success custom-verifyreg-button"]')))

    def create_random_email(self):
        conn = http.client.HTTPSConnection("privatix-temp-mail-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "1ec4dbba1emsh3eb8cb9029911aap163da9jsn951786c1d607",
            'X-RapidAPI-Host': "privatix-temp-mail-v1.p.rapidapi.com"
        }

        conn.request("GET", "/request/domains/", headers=headers)

        res = conn.getresponse()
        data = res.read()

        available_domains = (json.loads(data.decode("utf-8")))

        now = datetime.now()

        current_time = now.strftime("%d%m%Y%H%M%S")

        email = f'test{current_time}{available_domains[0]}'

        return email

    # def delete_random_email_btn(self,email):
    #     return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.ID,"click-to-delete")))

    def copy_email_btn(self):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="btn-rds icon-btn bg-theme d-none visable-xs-sm click-to-copy copyIconGreenBtn"]')))

    def verification_code2(self, email):
        hash_email = hashlib.md5(email.encode('utf-8')).hexdigest()
        conn = http.client.HTTPSConnection("privatix-temp-mail-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "1ec4dbba1emsh3eb8cb9029911aap163da9jsn951786c1d607",
            'X-RapidAPI-Host': "privatix-temp-mail-v1.p.rapidapi.com"
        }

        conn.request("GET", f"/request/mail/id/{hash_email}/", headers=headers)

        res = conn.getresponse()
        data = res.read()

        e_mail = json.loads(data.decode("utf-8"))[0]["mail_text"]
        string_to_search = "BEERELAXED-"
        index = e_mail.find(string_to_search)

        return e_mail[index + len(string_to_search):index + len(string_to_search) + 4]

