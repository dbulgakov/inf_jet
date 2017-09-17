#!/usr/bin/python3
import sys
import os
import math


def f_fib(data):
    a = 0
    b = 1
    for __ in range(int(data[0])):
        a, b = b, a + b
    return a


def f_factorial(data):
    return math.factorial(int(data[0]))


def f_ack_list(data):
    data = list(map(int, data))
    return f_ack(data[0], data[1])


def f_ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return f_ack(m - 1, 1)
    if m > 0 and n > 0:
        return f_ack(m - 1, f_ack(m, n - 1))


solution_dict = {
    'ACK': f_ack_list,
    'F': f_factorial,
    'FIB': f_fib
}


def get_solution(line):
    splited_line = line.split()
    method, data = splited_line[0], splited_line[1:]
    return solution_dict[method](data)


def save_ans(dict_to_save):
    try:
        f = open('output.txt', 'w')
        for key in dict_to_save.keys():
            f.write(str(key) + ' ' + str(dict_to_save[key]) + '\n')
        f.close()
    except IOError:
        print('Grant permissions to write to file!')
    except Exception as e:
        print('Check input data!')
        print(e)


def main(argv):
    try:
        output_dict = {}
        f = open(os.getcwd() + '/' + argv[1])
        for index, line in enumerate(f):
            output_dict[index + 1] = get_solution(line)
        f.close()
        save_ans(output_dict)
    except FileNotFoundError:
        print('File not found! Try again.')
    except Exception as e:
        print('Unknown exception!')
        print(e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print('Pass filename!')
