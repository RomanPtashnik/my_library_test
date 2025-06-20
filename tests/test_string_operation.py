import pytest
import allure # Используем Allure для генерации отчёта тестирования
from my_string_library.string_operation import StringUtils


@allure.feature('Simple reverse') # Обозначает принадлежность теста к feature
@allure.story('reverse')
def test_reverse():
    with allure.step('Testing reverse text in function'): # Добавляем описание в allure
        assert StringUtils.reverse_string("hello") == "olleh"
        assert StringUtils.reverse_string("Привет") == "тевирП"
        assert StringUtils.reverse_string("VK супер") == "репус KV"
        assert StringUtils.reverse_string("") == "Введенна пустая строка!"
        assert StringUtils.reverse_string("   ") == "Введенны пробелы"
        assert StringUtils.reverse_string("   test_test") == "tset_tset"


@allure.feature('Simple count volwels')
@allure.story('vowels')
def test_count_vowels():
    with allure.step('Testing search vowels in function count'):
        assert StringUtils.count_vowels("Python") == 1
        assert StringUtils.count_vowels("%$#%TreeeTy1132+__") == 3
        assert StringUtils.count_vowels("!!!") == 0
        assert StringUtils.count_vowels("EEEEEEEEEE") == 10


@allure.feature('Simple palindrome')
@allure.story('is_palindrome')
def test_is_palindrome():
    with allure.step('Testing palindrome text in function'):
        assert StringUtils.is_palindrome("ShaLaSh") is False
        assert StringUtils.is_palindrome("дод") is True
        assert StringUtils.is_palindrome("шалаш") is True
        assert StringUtils.is_palindrome("Шалаш") is True
        assert StringUtils.is_palindrome("Terra") is False