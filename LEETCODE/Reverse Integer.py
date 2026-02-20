import sys
x=int(input())
def reverse(x):
    remainder=x
    a=0
    if x<0:
        x=x*-1
        while x>0:
            remainder=x%10
            a=a*10+remainder
            x//=10
        a=a*-1
    else:
        while x>0:
            remainder=x%10
            a=a*10+remainder
            x//=10
    if a>sys.maxsize or a<(-sys.maxsize-1):
        return 0
    return a
print(reverse(x))
