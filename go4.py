def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def main():
    text = input("Введите строку для проверки: ")
    if is_palindrome(text):
        print(f'"{text}" — это палиндром!')
    else:
        print(f'"{text}" — не палиндром.')

    print("Примеры палиндромов: радар, level, 12321")
    print("Хотите проверить ещё? Введите новую строку или 'выход' для завершения.")
    while (text := input("Ваша строка: ")) != "выход":
        if is_palindrome(text):
            print(f'"{text}" — это палиндром!')
        else:
            print(f'"{text}" — не палиндром.')


main()
