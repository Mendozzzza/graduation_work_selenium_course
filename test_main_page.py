from selenium import webdriver
from .pages.main_page import MainPage #импортируем класс описывающий главную стр
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    # browser.get(link)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()
    page.open() #открываем страницу, используя метод open
    page.go_to_login_page() #выполняем метод стр - переходим на стр логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
