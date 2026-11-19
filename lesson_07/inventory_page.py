from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name):
        # Преобразуем название товара в формат ID кнопки на saucedemo
        formatted_name = item_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{formatted_name}"
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        add_btn.click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
