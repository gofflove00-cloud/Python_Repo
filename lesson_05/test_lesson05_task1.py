from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываем страницу
    driver.get("https://httpbin.qa-territory.online")

    # 2. Находим и кликаем на ссылку HTML Form
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    # 3. Проверяем, что URL изменился на /forms/post
    assert driver.current_url == "https://qa-territory.online", \
        f"Ожидался URL /forms/post, но получили {driver.current_url}"

    # 4. Возвращаемся назад на главную страницу
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://qa-territory.online", \
        f"Ожидался исходный URL, но получили {driver.current_url}"

    driver.quit()
