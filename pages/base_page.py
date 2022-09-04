from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10): #timeout - добавили неявное ожидание
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) #неявное ожидание передали в browser 

    def open(self): 
        self.browser.get(self.url) #добавили метод, открывающий страницу

    def is_element_present(self, how, what): #добавили метод, перехватывающий исключения(как искать(css, id и тд), что искать(строку, селктор))
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
