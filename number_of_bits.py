def numberofbits(n):
    count = 0
    while(n):
        count += 1
        n >>=1
    return count

num = int(input('enter your number: '))
print('Total bits : ', numberofbits(num))