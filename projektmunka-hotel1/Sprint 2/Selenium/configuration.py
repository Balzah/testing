"""
A modul célja, hogy ne kelljen minden egyes példánál ismételni a megfelelő Chrome driver létrehozását.
Importálás után elég a get_preconfigured_chrome_driver() függvényt meghívni.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option('detach', True)
    # options.add_argument('--incognito')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Allure certificate error esetén

    return webdriver.Chrome(options=options)
