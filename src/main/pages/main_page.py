from src.main.wrappers.base import Base

class MainHeaderBar(Base):

    LOGIN_HEAD_BAR = "//div[@class='head-bar']//div[4]/a/span"
    ENTRY_BUTTON = "//a[text()='Вход']"

    def click_login_head_bar_button(self):
        self.click_element(self.LOGIN_HEAD_BAR)

    def click_entry_button(self):
        self.click_element(self.ENTRY_BUTTON)

    def get_text_head_bar_button(self):
        text_acc = self.get_element_text(self.LOGIN_HEAD_BAR)
        return text_acc