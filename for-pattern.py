import math

def print_for_pattern(num):
    if num < 1: return

    max = num

    for i in range(1, num):
        print(' ' * int(max/2)  + '*'*i)
        max = max - 1


def main():
    num = int(raw_input('Enter number: '))
    print_for_pattern(num)


main()