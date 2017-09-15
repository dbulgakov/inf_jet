# Программа, возвращающая n-й по величине элемент набора чисел.


def remove_min_value(input_list):
    input_list.remove(min(input_list))
    return input_list


def find_nth_max(array, nth):
    values = []
    if nth > len(array) or nth < 1:
        raise ValueError('Position must be less or equal to array size')
    for item in array:
        if len(values) < nth or item > values[0]:
            if len(values) == nth:
                values = remove_min_value(values)
            values.append(item)
    return min(values)


def main():
    try:
        array = list(map(int, input('Enter input array: ').split(' ')))
        position = int(input('Enter position to find: '))
        print("So, #{0} max is {1}".format(position, find_nth_max(array, position)))
    except ValueError as e:
        print('Wrong input! Try again')
        print(e)
    except Exception:
        print('Unknown error')


if __name__ == "__main__":
    main()