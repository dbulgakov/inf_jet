# Программа выполняющая Run-length encoding декодирование строки (3a1b2c2d->aaabccdd).


def rnl_decode(string):
    string_length = len(string)
    if string_length == 0:
        raise ValueError('Input string must not be empty!')

    if string_length % 2 != 0:
        raise ValueError('Wrong input format!')

    output_string = ""
    for i in range(0, string_length - 1):
        if i % 2 == 0:
            if not string[i].isdigit():
                raise ValueError('Wrong input format!')
            else:
                output_string += string[i + 1] * int(string[i])
    return output_string


def main():
    try:
        input_string = input("Enter string to decode: ")
        print(rnl_decode(input_string))
    except ValueError as e:
        print(e)
    except Exception:
        print('Unknown error')


if __name__ == "__main__":
    main()
