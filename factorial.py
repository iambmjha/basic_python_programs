def fact(num):
    if(num < 0): return 'Negative number not allowed'
    if(num == 0): return 1

    f = 1
    for i in range(1, num):
        f = f * i
    
    return  f


print(fact(10))
print(fact(3))
print(fact(5))
print(fact(0))
print(fact(1))
print(fact(-67))