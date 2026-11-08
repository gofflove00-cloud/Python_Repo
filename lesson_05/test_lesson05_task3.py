from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 1. Находим все ссылки на странице по тегу <a>
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # 3. Проверяем, что все ссылки отображаются (видимы) на странице
    for link in links:
        assert link.is_displayed(), (
            f"Ссылка с текстом '{link.text}'не отображается на странице"
            )

    # 4. Проверяем, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, (
            f"Текст первой ссылки ожидал '1', но получили '{first_link_text}'"
            )

    driver.quit()
