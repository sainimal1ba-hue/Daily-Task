n=int(input())
for _ in range(n):
    a=input()
    ans=[]
    if len(a)>10:
        ans.append(a[0])
        ans.append(str(len(a)-2))
        ans.append(a[len(a)-1])
        print("".join(ans))
    else:
        print(a)
