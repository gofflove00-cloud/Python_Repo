from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу dynamic_loading/2
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        wait = WebDriverWait(driver, 10)

        # 2. Ищем и нажимаем на кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Ждем появления текста "Hello World!"
        finish_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Делаем скриншот страницы
        driver.save_screenshot("lesson_06/screenshots/hello_world.png")

        # 5. Проверяем, что появившийся текст равен "Hello World!"
        assert finish_text.text == "Hello World!", (
            "Текст 'Hello World!' не появился"
        )
    finally:
        driver.quit()
