# Программа выполняющая Run-length encoding кодирование строки (aaabccdd -> 3a1b2c2d)


def rnl_encode(string):
    if len(string) == 0:
        raise ValueError('Input string must not be empty!')

    previous = string[0]
    counter = 0
    output_string = ""
    for char in string:
        if char == previous:
            counter += 1
        else:
            output_string += "{0}{1}".format(counter, previous)
            previous = char
            counter = 1
    output_string += "{0}{1}".format(counter, previous)
    return output_string


def main():
    try:
        input_string = input("Enter string to encode: ")
        print(rnl_encode(input_string))
    except ValueError as e:
        print(e)
    except Exception:
        print('Unknown error')


if __name__ == "__main__":
    main()
