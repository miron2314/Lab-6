if __name__ == '__main__':
    while True:
        input_string = input("Введите строку: ")

        if not input_string:
            print("Ошибка: Строка не может быть пустой.")
            continue

        result_string = ""
        for char in input_string:
            result_string += char
            if char.lower() == 'и':
                result_string += '.'

        print(result_string)
        break