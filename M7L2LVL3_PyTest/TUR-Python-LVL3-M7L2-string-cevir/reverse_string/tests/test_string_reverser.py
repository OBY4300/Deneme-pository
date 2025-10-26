# test_string_reverser.py

import pytest
from reverse_string.string_reverser import reverse_string

# reverse_string fonksiyonunun normal bir metinle doğru çalışıp çalışmadığını test eder.
def test_reverse_string_normal():
    print(reverse_string("hello"))
    assert reverse_string("hello") == "olleh", "Beklenen sonuç: 'hello' metninin 'olleh' olarak ters çevrilmesi"
# reverse_string fonksiyonunun boşluk içeren metinlerde doğru çalışıp çalışmadığını kontrol eder.
def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh", "Beklenen sonuç: 'hello world' metninin 'dlrow olleh' olarak ters çevrilmesi"

# reverse_string fonksiyonunun boş bir metni hatasız şekilde işleyip işlemediğini kontrol eder.
def test_reverse_string_empty():
    assert reverse_string("") == "", "Beklenen sonuç: Boş bir metnin ters çevrildiğinde yine boş olması"

test_reverse_string_normal()