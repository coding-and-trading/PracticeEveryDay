# _*_ coding: utf-8 _*_

def calcNumbers():
    number = int(input('Enter a number'))
    start, end = 0, 6
    ans = calcRoot(number, 3)
    if start < ans and ans <end:
            print('root is ' + str())
    else:
        print('No found.')

def calcRoot(number, height):
    ans = 0
    while ans ** height < abs(number):
        ans = ans + 1
    if ans ** height != abs(number):
        print(number, 'is not a perfect cube')
    else:
        if number < 0:
            ans = -ans
        return ans

def sumOfString(s):
    return sum([float(i) for i in s.split(',')])

if __name__ == '__main__':
    s = '1.23, 2.4, 3.123'
    print(sumOfString(s))