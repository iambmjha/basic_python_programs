def get_sub(num1, num2):
    return num1 - num2

def get_per(num1, num2):
    return num1 % num2

def get_div(num1, num2):
    return num1 / num2

def get_multi(num1, num2):
    return num1 * num2

def main():
    num1 = float(raw_input('Enter 1st number: '))
    num2 = float(raw_input('Enter 2nd number: '))

    print('\nResults:\n------------')
    print('Sub: {}'.format(get_sub(num1, num2)))
    print('Per: {}'.format(get_per(num1, num2)))
    print('Div: {}'.format(get_div(num1, num2)))
    print('Multi: {}'.format(get_multi(num1, num2)))


main()
