from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                self.SCREEN, str(expected_result)
            )
        )
        return self.driver.find_element(*self.SCREEN).text
