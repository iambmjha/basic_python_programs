def is_even_number(num):
    if(num % 2 == 0): return True
    
    return False


def main():
    nums = [1,2,3,4,5,4,3,6,7,8,80,60,67]

    for i in nums:
        if(is_even_number(i)): print(str(i) + ' -- even')
        else: print(str(i) + ' -- odd')

main()