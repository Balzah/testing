from datetime import datetime

from selenium.webdriver import Chrome


class GeneralPage:

    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def current_url(self):
        return self.browser.current_url

    def save_screenshot(self, path):
        filename = f'{self.browser.title}-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png'
        print(f"Screenshot attempt: {path}\\{filename}")
        if self.browser.save_screenshot(f"{path}\\{filename}"):
            print("Screenshot saved succesfully")
        else:
            print("Screenshot failed")
