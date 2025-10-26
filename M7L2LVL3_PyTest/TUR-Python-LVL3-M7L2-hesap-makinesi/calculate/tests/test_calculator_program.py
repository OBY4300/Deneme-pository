import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Bilinmeyen işlem."

def test_sifirla_bolme():
    assert calculate(2, 0, "/") == "Hata: Sıfıra bölme"

def test_eksi_rakam_topla():
    assert calculate(-1, -2, "+") < 0

def test_hepsi_eksi_bol():
    assert calculate(-6, -3, "/") > 0 

def test_birinci_eksi_bol():
    assert calculate(-6, 3, "/") < 0

def test_ikinci_eksi_bol():
    assert calculate(6, -3, "/") < 0

def test_hepsi_eksi_carp():
    assert calculate(-6, -3, "*") > 0 

def test_birinci_eksi_carp():
    assert calculate(-6, 3, "*") < 0

def test_ikinci_eksi_carp():
    assert calculate(6, -3, "*") < 0

def safdsfdsfdgfggdfhfghxxfznfzfngfbzdvvvfesbsfbdsfdfbndfjzvjdfhvıfsdhuvhuıfdhbduıhvdıubjdfıubhdfıubhfıbhfıbhıbhfdubhdfıubhfıbhfbhfıbhfdıubhfdıubhfıubfhıubhfdıubhfdıbhfdıubhuıbhd():
    abc = 23
    skfod = 21213 - abc
    assert abc + skfod == 21213

'''
Görev: Şu anda, 3 adet birim test uygulanmıştır:
Toplama ve bölme işlemlerinin doğruluğu ile bilinmeyen işlem test edilmektedir.
Göreviniz, aşağıdaki işlemler için en az iki test eklemektir:
1. Çıkarma
2. Çarpma
Ek olarak, farklı senaryolar için ek testler geliştirip yazarsanız harika olur!
'''

safdsfdsfdgfggdfhfghxxfznfzfngfbzdvvvfesbsfbdsfdfbndfjzvjdfhvıfsdhuvhuıfdhbduıhvdıubjdfıubhdfıubhfıbhfıbhıbhfdubhdfıubhfıbhfbhfıbhfdıubhfdıubhfıubfhıubhfdıubhfdıbhfdıubhuıbhd()