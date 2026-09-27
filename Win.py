def main():
    phonebook = []

    while True:
        print("\nТелефонная Книга")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            if not phonebook:
                print("Телефонная книга пуста.")
            else:
                print("--- Список контактов ---")
                for name, phone in phonebook:
                    print(f"Имя: {name} | Телефон: {phone}")
                print("------------------------")

        elif choice == "2":
            name = input("Введите имя контакта: ").strip()
            phone = input("Введите номер телефона: ").strip()

            if not name or not phone:
                print("Имя и телефон не могут быть пустыми")
                continue

            if any(c[0].lower() == name.lower() for c in phonebook):
                print(f"Контакт с именем '{name}' уже существует в списке")
            else:
                phonebook.append([name, phone])
                print(f"Контакт '{name}' успешно добавлен!")

        elif choice == "3":
            search_name = input("Введите имя для поиска: ").strip().lower()
            for contact in phonebook:
                if contact[0].lower() == search_name:
                    print(f"Найдено -> Имя: {contact[0]} | Телефон: {contact[1]}")
                    break
            else:
                print(f"Контакт с именем '{search_name}' не найден")

        elif choice == "4":
            delete_name = input("Введите имя контакта для удаления: ").strip().lower()
            for contact in phonebook:
                if contact[0].lower() == delete_name:
                    phonebook.remove(contact)
                    print(f"Контакт '{contact[0]}' успешно удален")
                    break
            else:
                print(f"Контакт с именем '{delete_name}' не найден")

        elif choice == "5":
            print("Программа завершена")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5")


if __name__ == "__main__":
    main()


 