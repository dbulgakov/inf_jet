# Программа, возвращающая 2-й по величине элемент набора чисел.


def second_max(values_list):
    list_length = len(values_list)
    if list_length <= 1:
        raise ValueError('At least two values are required')
    first, second = values_list[0], values_list[1]
    for number in values_list:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second


def main():
    try:
        input_array = input('Enter input array: ')
        input_array = list(map(int, input_array.split(' ')))

        print('Input: ', input_array)
        print('Second largest: ', second_max(input_array))
    except ValueError as e:
        print('Wrong input! Try again')
        print(e)
    except Exception:
        print('Unknown error')


if __name__ == "__main__":
    main()
