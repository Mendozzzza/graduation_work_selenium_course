from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") 
    #создали внешнюю переменную, чтобы использ в тестах
    #теперь каждый селектор пара "что искать" и "как искать"

class LoginPageLocators():
    current_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#ltrytrey") #login_form
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#regirteyretyorm") #register_form