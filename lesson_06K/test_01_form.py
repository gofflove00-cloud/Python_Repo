from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    driver = webdriver.Edge()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 1. Открываем страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # 2. Заполняем поля формы
    fields_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name_attr, value in fields_data.items():
        field = wait.until(
            EC.visibility_of_element_located((By.NAME, name_attr))
        )
        field.send_keys(value)

    # 3. Нажимаем кнопку Submit
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # 4. Проверяем, что поле Zip code подсвечено красным
    zip_code = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute("class"), (
        "Поле Zip code не подсвечено красным"
    )

    # 5. Проверяем, что остальные поля подсвечены зеленым
    green_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_fields_ids:
        element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class"), (
            f"Поле {field_id} не подсвечено зеленым"
        )

    driver.quit()
