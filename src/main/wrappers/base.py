from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class Base:

    TIME_OUT = 3
    URL = "https://mega.readyscript.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.TIME_OUT)

    def open_page(self, url = URL):
        self.driver.get(url)

    def find_element(self, element, by = By.XPATH):
        try:
            return WebDriverWait(self.driver, self.TIME_OUT).until(ec.visibility_of_element_located((by, element)))
        except TimeoutException:
            print(f"Error: Element with locator {element} not found!!!")
            return None
        except Exception as e:
            print(f"Unknown error: {e}")

    def click_element(self, element):
        self.find_element(element).click()

    def get_element_text(self, element, by = By.XPATH):
        return self.find_element(element, by).text

    def clear_input(self, element, by = By.XPATH):
        self.find_element(element, by).clear()

    def input_text(self, element, text, by = By.XPATH):
        self.find_element(element, by).send_keys(text)

    def check_element_invisibility(self, element, by = By.XPATH):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(ec.invisibility_of_element_located((by, element)))
            return True
        except TimeoutException:
            print(f"Error: Element with locator {element} did not disappear!!!")
            return False
        except Exception as e:
            print(f"Unknown error: {e}")
            return False