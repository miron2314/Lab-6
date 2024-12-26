import sys

def check_zhi_shi():
    """Проверяет правильность написания 'жи' и 'ши' в последовательности слов."""
    while True:
        s = input("Введите последовательность слов через пробел: ")
        words = s.split()

        if not words:
            print("Ошибка: Введите хотя бы одно слово.", file=sys.stderr)
            continue

        errors_found = False
        for word in words:
            word = word.lower()
            for i in range(len(word) - 1):
                if word[i] == 'ж' and word[i+1] != 'и':
                    print(f"Ошибка в слове '{word}': 'жи' написано неправильно.", file=sys.stderr)
                    errors_found = True
                if word[i] == 'ш' and word[i+1] != 'и':
                    print(f"Ошибка в слове '{word}': 'ши' написано неправильно.", file=sys.stderr)
                    errors_found = True

        if not errors_found:
            print("Все слова написаны правильно с точки зрения 'жи' и 'ши'.")

        break


if __name__ == '__main__':
    check_zhi_shi()