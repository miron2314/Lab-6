import sys


def process_sentence():
    """Обрабатывает ввод предложения и выводит буквы 'м' и 'н'."""
    while True:
        s = input("Введите предложение: ")

        # Ищем 'м' и 'н'
        s = s.lower()
        found_letters = ""
        for char in s:
            if char == 'м' or char == 'н':
                found_letters += char + " "

        if found_letters:
            print("Буквы 'м' и 'н' в предложении:")
            print(found_letters)
        else:
            print("В предложении не найдены буквы 'м' и 'н'.")

        break


if __name__ == '__main__':
    process_sentence()