'''
This is a binary converter which takes it's input as 3 numbers: a lower limit, an upper limit, and a step.
The program will then return this range of numbers with the given step as binary numbers.
'''

#Function to convert an integer into binary:
def int_bin(x):
    
    a = x
    num = []
    
    if x == 0:
        num = [0]
    else:
    
        while a > 1:
            
            n = a % 2
            num.append(int(n))
        
            if n == 1:
                a = a/2 - 0.5
            
            else:
                a = a/2
        num.append(1)                     
    return num[::-1]

#Request input of range parameters:
xmin = int(input('Lower limit: \n'))
xmax = int(input('Upper Limit: \n'))
step = int(input('Step: \n'))

#Convert input into binary:

for x in range(xmin, xmax, step):
    print('{}: {}'.format(x, int_bin(x)))

