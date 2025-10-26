def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Hata: Sıfıra bölme"
    else:
        return "Bilinmeyen işlem."


def main():
    print("Basit Hesap Makinesi. İki sayı girin ve bir işlem seçin.")
    num1 = float(input("İlk sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))
    operation = input("Bir işlem seçin (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"Sonuç: {result}")


if __name__ == "__main__":
    main()
