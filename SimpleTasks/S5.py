# Программа, выполняющая поиск подстроки в строке.


def main():
    string_to_check = input('Enter string to check: ')
    substring_to_find = input('Enter substring to find: ')
    print('Input string contains substring: ', substring_to_find in string_to_check)


if __name__ == "__main__":
    main()
