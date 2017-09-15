# Программа, выполняющая проверку строки на то, что она является палиндромом


def palindrome(input_string):
    if len(input_string) < 2:
        return False
    return input_string == input_string[::-1]


def main():
    string_to_check = input('Enter string to check: ')
    print('Input string is palindrome: ', palindrome(string_to_check))


if __name__ == "__main__":
    main()