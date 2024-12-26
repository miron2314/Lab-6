import sys
if __name__ == '__main__':
    s = input("Введите предложение: ")
    n = int(input("Введите длину: "))
    if len(s) >= n:
        print("Заданная длина должна быть больше длины предложения",file=sys.stderr)
        exit(1)

words = s.split(' ')
# Проверить количество слов в предложении.
if len(words) < 2:
print(
"Предложение должно содержать несколько слов",
file=sys.stderr
)
exit(1)
# Количество пробелов для добавления.
delta = n
for word in words:
delta -= len(word)
# Количество пробелов на каждое слово.
w, r = delta // (len(words) - 1), delta % (len(words) - 1)
# Сформировать список для хранения слов и пробелов.
lst = []