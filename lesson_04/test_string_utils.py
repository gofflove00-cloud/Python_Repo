import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
  return StringUtils()


# Тесты для метода capitalize


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("Skypro", "Skypro"),
        ("HELLO", "Hello"),
        ("свет", "Свет"),  # проверка кириллицы
        ("123abc", "123abc"),  # число в начале
        (" a b c ", " a b c "),  # пробелы в начале
    ],
)
def test_capitalize_positive(utils, input_str, expected):
  assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # пустая строка
        ("   ", "   "),  # строка из пробелов
        ("!hello", "!hello"),  # спецсимвол в начале
    ],
)
def test_capitalize_negative(utils, input_str, expected):
  assert utils.capitalize(input_str) == expected


# Тесты для метода trim


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("skypro   ", "skypro   "),  # удаляет только в начале по логике метода
        ("   sky   pro", "sky   pro"),
        ("", ""),
    ],
)
def test_trim_positive(utils, input_str, expected):
  assert utils.trim(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "skypro"),  # без пробелов в начале
        ("   ", ""),  # только пробелы
    ],
)
def test_trim_negative(utils, input_str, expected):
  assert utils.trim(input_str) == expected


# Тесты для метода contains


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "y", True),
        ("SkyPro", "o", True),
        ("Hello world", " ", True),  # поиск пробела
    ],
)
def test_contains_positive(utils, input_str, symbol, expected):
  assert utils.contains(input_str, symbol) is True


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "U", False),
        ("SkyPro", "z", False),
        ("SkyPro", "s", False),  # учет регистра (вдруг 's' != 'S')
        ("", "a", False),  # пустая строка
    ],
)
def test_contains_negative(utils, input_str, symbol, expected):
  assert utils.contains(input_str, symbol) is False


# Тесты для метода delete_symbol


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("banana", "a", "bnn"),  # удаление всех вхождений символа        
    ],
)
def test_delete_symbol_positive(utils, input_str, symbol, expected):
  assert utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "z", "SkyPro"),  # удаляемого символа нет в строке
        ("", "a", ""),  # пустая строка
        ("SkyPro", "", "SkyPro"),  # пустой символ для удаления
    ],
)
def test_delete_symbol_negative(utils, input_str, symbol, expected):
  assert utils.delete_symbol(input_str, symbol) == expected
