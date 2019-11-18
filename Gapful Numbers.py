'''
A gapful number is divisible by its first and last integers e.g. 105 is divisible by 15.
This program will return all the gapful numbers in a user defined range.
'''
num1 = input('Beginning of range:')
num2 = input('End of range:')

for x in range(int(num1),int(num2)):

    num = str(x)

    if len(num) < 2:
        print('{} is too small to be gapful.'.format(num))
    

    elif int(num) % int(num[0]+num[-1]) == 0:

        print('{} is a gapful number!'.format(num))

    else:

        pass
