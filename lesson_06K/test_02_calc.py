from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Открываем страницу калькулятора
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    # 2. Очищаем поле #delay и вводим значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем на кнопки: 7, +, 8, =
    buttons = ["7", "+", "8", "="]
    for btn_text in buttons:
        button = driver.find_element(
            By.XPATH, f"//span[text()='{btn_text}']"
        )
        button.click()

    # 4. Ждём появления результата "15" (таймаут с небольшим запасом — 50 сек)
    wait = WebDriverWait(driver, 50)
    is_result_displayed = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # 5. Проверяем, что результат действительно отобразился
    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert is_result_displayed and result_text == "15", (
        f"Ожидался результат '15', но получили '{result_text}'"
    )

    driver.quit()
