def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0

    my_string = 'This is my string. Do you like?'

    for c in my_string:
        if(c in vowels): count = count + 1

    print('Number of vowels: {}'.format(count))


main()