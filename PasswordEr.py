users = {}

while True:
    print("\n1 - Регистрация")
    print("2 - Вход")
    print("3 - Выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        login = input("Придумай логин: ")

        if login in users:
            print("Такой логин уже существует.")
        else:
            password = input("Придумай пароль: ")
            users[login] = password
            print("Регистрация успешна.")

    elif choice == "2":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in users and users[login] == password:
            print("Вход выполнен.")
        else:
            print("Неверный логин или пароль.")

    elif choice == "3":
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор.")
