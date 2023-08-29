# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=""
    for i in range(len(c)):
        if b-c[i]>=0:
            d=d+'1'
            b=b-c[i]
        else:
            d=d+'0'
            
    print(d)
        
