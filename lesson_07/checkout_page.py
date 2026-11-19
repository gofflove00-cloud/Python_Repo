from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_shipping_info(self, first_name, last_name, postal_code):
        first_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_field.send_keys(first_name)

        last_field = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_field.send_keys(last_name)

        zip_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        zip_field.send_keys(postal_code)

        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self):
        total_el = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        # Извлекаем значение вида "$58.29" из строки "Total: $58.29"
        return total_el.text.replace("Total: ", "")
