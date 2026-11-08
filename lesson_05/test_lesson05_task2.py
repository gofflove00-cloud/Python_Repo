from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # 1. Находим поле для ввода имени по атрибуту name и вводим текст
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Тестовое Имя")

    # 2. Находим кнопку "Submit" с помощью XPath по тексту и кликаем на неё
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    # 3. Проверяем, что URL изменился после отправки формы
    assert driver.current_url == "https://qa-territory.online", \
        f"Ожидался URL /post, но текущий URL: {driver.current_url}"

    driver.quit()
