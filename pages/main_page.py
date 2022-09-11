from .base_page import BasePage #импорт базового класса BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators #импортируем из файла класс

class MainPage(BasePage): #делаем класс MainPage наследником класса BasePage. Предок в скобках()
    def go_to_login_page(self): #указываем аргумент self, чтобы иметь доступ к атриб и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self): #делаем метод проверки наличия ссылки
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #сообщение после селектора передается как ошибка в консоль
