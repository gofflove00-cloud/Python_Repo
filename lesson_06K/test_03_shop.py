from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop_checkout():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 1. Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся как standard_user
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_input.send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем в корзину нужные товары по их ID кнопок
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for item_id in items_to_add:
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, item_id)))
        add_btn.click()

    # 4. Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажимаем Checkout
    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_btn.click()

    # 6. Заполняем форму своими данными
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажимаем кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Читаем со страницы итоговую стоимость (Total)
    total_locator = (By.CLASS_NAME, "summary_total_label")
    total_element = wait.until(
        EC.visibility_of_element_located(total_locator)
    )
    total_text = total_element.text

    # 9. Закрываем браузер (до assert, согласно условию задачи)
    driver.quit()

    # 10. Проверяем, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", (
        f"Ожидалась сумма 'Total: $58.29', но получили '{total_text}'"
    )
