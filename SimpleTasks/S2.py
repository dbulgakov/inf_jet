# Программа, выполняющая разложение числа на набор простых множителей

import math


def factorization(input_number):
    dividers = []
    for number in range(2, int(math.sqrt(input_number)) + 1):
        while input_number % number == 0:
            dividers.append(number)
            input_number //= number
    if input_number != 1:
        dividers.append(input_number)
    return dividers


def main():
    try:
        number = int(input('Enter number to factorize: '))
        if number <= 1:
            raise ValueError('Input number must be >= 1!')
        print('Dividers: ', *factorization(number))
    except ValueError as e:
        print('Wrong input! Try again')
        print(e)


if __name__ == "__main__":
    main()