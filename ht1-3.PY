
while True:
    password = input("введите пароль: ")

    if (len(password) >= 8) & (any(char.isupper() for char in password)) & any(char.islower() for char in password):
        print("Пароль принят.")
        break
    else:
        print(
            "Неверный пароль. Пароль должен содержать более 8 символов и состоять из заглавных и строчных букв.")





