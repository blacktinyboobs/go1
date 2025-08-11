def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def main():
    try:
        n = int(input("Сколько чисел Фибоначчи показать? (не менее 2): "))
        if n < 2:
            print("Введите число не менее 2!")
        else:
            result = fibonacci(n)
            print("Числа Фибоначчи:", result)
            print(f"Сумма чисел: {sum(result)}")
    except ValueError:
        print("Введите корректное число!")


main()
