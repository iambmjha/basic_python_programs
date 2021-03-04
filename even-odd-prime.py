import math

def is_even_number(num):
    if(num % 2 == 0): return True
    
    return False

def is_prime_number(num):
    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if(num % i == 0): return False
    
    return True


def print_even_odd_prime(num):
    if (is_even_number(num)): print(str(num) + ' --> Even number')
    if(not is_even_number(num)): print(str(num) + ' --> Odd number')
    if(is_prime_number(num)): print(str(num) + ' --> Prime number')

    print('-------------------\n')


print_even_odd_prime(2)
print_even_odd_prime(3)
print_even_odd_prime(7)
print_even_odd_prime(8)
