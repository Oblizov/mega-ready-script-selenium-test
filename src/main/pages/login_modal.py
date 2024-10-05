import allure

from src.main.wrappers.base import Base

class LoginModalWindow(Base):

    LOGIN_INPUT = "//input[@name='login']"
    PASSWORD_INPUT = "//input[@name='pass']"
    LOGIN_BUTTON = "//div[@class='modal-content']//button[@type='submit']"

    @allure.step("Очистить поле в окне логина")
    def clean_creds(self):
        self.clear_input(self.LOGIN_INPUT)
        self.clear_input(self.PASSWORD_INPUT)

    @allure.step("Ввести логин и пароль")
    def input_creds(self, username, password):
        self.clean_creds()
        self.input_text(self.LOGIN_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)

    @allure.step("Залогинить пользователя")
    def login(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Подождать исчезновения окна логина")
    def check_login_modal_invisibility(self):
        self.check_element_invisibility(self.LOGIN_INPUT)