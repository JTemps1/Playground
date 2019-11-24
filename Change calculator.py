'''
A simple program to calculate what change in COINS ONLY you can get from a specified amount of money.
'''
#Input amount in pounds e.g. for 80p => x = 0.8
def coin_change(x):
    #Start by seeing how many of the largest coin we can get in, and then work our way down:
    two_pound = x // 2
    xn = round(x % 2, 2)

    one_pound = xn // 1
    xn = round(xn % 1, 2)

    fifty_p = xn // 0.5
    xn = round(xn % 0.5, 2)

    twenty_p = xn // 0.2
    xn = round(xn % 0.2, 2)

    ten_p = xn // 0.1
    xn = round(xn % 0.1, 2)

    five_p = xn // 0.05
    xn = round(xn % 0.05, 2)

    two_p = xn // 0.02
    xn = round(xn % 0.02, 2)

    one_p = xn // 0.01
    xn = round(xn % 0.01, 2)

    print("Amount given: {}\n\
            £2: {}\n\
            £1: {}\n\
            50p: {}\n\
            20p: {}\n\
            10p: {}\n\
            5p: {}\n\
            2p: {}\n\
            1p: {}\n\
            ".format(x, int(two_pound), int(one_pound), int(fifty_p), int(twenty_p), int(ten_p), int(five_p), int(two_p), int(one_p)))

coin_change(3.48)
