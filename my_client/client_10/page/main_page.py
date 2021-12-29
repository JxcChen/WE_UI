from selenium.webdriver.common.by import By

from page.base_page import BasePage
from selenium.webdriver import Chrome


class MainPage(BasePage):
    @staticmethod
    def init_driver():
        return Chrome()

    def start(self):
        driver = self.init_driver()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return MainPage(driver)

    def search_kw(self, value):
        self.send_key((By.ID, 'kw'), value).click_ele((By.ID, 'su'))

    def quit(self):
        self.driver.quit()
