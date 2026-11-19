from calculator_page import CalculatorPage
from selenium import webdriver


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    calculator = CalculatorPage(driver)

    # 1. Открыть страницу калькулятора
    calculator.open()

    # 2. Ввести значение 45 в поле задержки
    calculator.set_delay(45)

    # 3. Нажать кнопки: 7, +, 8, =
    for button in ["7", "+", "8", "="]:
        calculator.click_button(button)

    # 4. Проверить, что отобразится результат 15 через 45 секунд
    result = calculator.get_result(expected_result="15", timeout=50)
    assert result == "15", f"Ожидался результат '15', но получили '{result}'"

    driver.quit()
