from .base_page import BasePage #импорт базового класса BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): #делаем класс MainPage наследником класса BasePage. Предок в скобках()
    def go_to_login_page(self): #указываем аргумент self, чтобы иметь доступ к атриб и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
