import allure

from src.main.wrappers.base import Base

class MainHeaderBar(Base):

    LOGIN_HEAD_BAR = "//div[@class='head-bar']//div[4]/a/span"
    ENTRY_BUTTON = "//a[text()='Вход']"

    @allure.step("Кликнуть на кнопку \"Логин\" в хедере сайта")
    def click_login_head_bar_button(self):
        self.click_element(self.LOGIN_HEAD_BAR)

    @allure.step("Кликнуть на кнопку \"Вход\"")
    def click_entry_button(self):
        self.click_element(self.ENTRY_BUTTON)

    @allure.step("Получить имя залогиненого пользователя")
    def get_text_head_bar_button(self):
        text_acc = self.get_element_text(self.LOGIN_HEAD_BAR)
        allure.attach("Имя залогиненого пользователя:", text_acc, allure.attachment_type.TEXT)
        return text_acc