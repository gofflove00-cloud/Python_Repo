from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def close_cookie_banner(driver):
    """Закрываем всплывающее окно согласия с cookies, если оно появилось."""
    try:
        wait = WebDriverWait(driver, 5)
        accept_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Принять')]")
            )
        )
        accept_btn.click()
    except TimeoutException:
        pass


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Открываем страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # 2. Устанавливаем cookie пользователя 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "MmE3YzE2MzItMDFkYS00NDhkLTkxMTctZDQ4MjBjZDI2NzQ4",
        "domain": "gitflic.ru",
    })

    # 3. Обновляем страницу
    driver.refresh()

    # 4. Переходим на страницу пользователя 1
    driver.get("https://gitflic.ru/user/1user1")

    # 5. Сохраняем текущий URL
    url_user_1 = driver.current_url

    # 6. Разлогин (очиститка куки)
    driver.delete_all_cookies()

    # 7. Установка cookie пользователя 2
    driver.add_cookie({
        "name": "SESSION",
        "value": "MDJlYzViNWEtZjA0ZS00ODBhLWJiYjYtMzM4ZGI0NDJiNjk4",
        "domain": "gitflic.ru",
    })

    # 8. Обновляем страницу
    driver.refresh()

    # 9. Переходим на страницу пользователя 2
    driver.get("https://gitflic.ru/user/2user2")

    # 10. Сохраняем текущий URL
    url_user_2 = driver.current_url

    # 11. Проверяем, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user_1 != url_user_2, (
        "URL профилей пользователей должны различаться"
    )

    driver.quit()
