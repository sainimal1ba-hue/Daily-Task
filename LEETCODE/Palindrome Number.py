n=int(input())
def isPalindrome(n):
    temp,a=n,0
    if n<0:
        return 0
    while n!=0:
        remainder=x%10
        a=a*10+remainder
        n//=10
    return a==temp
print(isPalindrome(n))
