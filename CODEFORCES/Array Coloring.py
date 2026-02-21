n=int(input())
def check(b):
    for i in range(1,len(b)):
        if b[i]%2==b[i-1]%2:
            return False
    return True

for _ in range(n):
    k=int(input())
    b=list(map(int,input().split()))
    if check(b):
        print("YES")
    else:
        print("NO")
    
