if __name__ == '__main__':
    word = input("Введите слово: ")
    idx = len(word) // 2
    if len(word) % 2 == 1:
        r = word[:idx] + word[idx+1:]
    else:
        r = word[:idx-1] + word[idx+1:]
    print(r)