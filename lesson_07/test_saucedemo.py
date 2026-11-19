from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from selenium import webdriver


def test_saucedemo_checkout():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт магазина
    login_page.open()

    # 2. Авторизоваться как пользователь standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить в корзину товары
    items_to_buy = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    for item in items_to_buy:
        inventory_page.add_item_to_cart(item)

    # 4. Перейти в корзину и проверить содержимое
    inventory_page.go_to_cart()
    assert cart_page.get_cart_items() == items_to_buy, (
        "Список товаров в корзине не совпадает с добавленными"
    )

    # 5. Нажать кнопку Checkout
    cart_page.click_checkout()

    # 6. Заполнить форму своими данными
    checkout_page.fill_shipping_info("Иван", "Петров", "123456")

    # 7. Прочитать со страницы итоговую стоимость (Total)
    total_price = checkout_page.get_total_price()

    # 8. Закрыть браузер
    driver.quit()

    # 9. Проверить (assert), что итоговая сумма равна $58.29
    assert total_price == "$58.29", (
        f"Ожидалась сумма '$58.29', но получили '{total_price}'"
    )
