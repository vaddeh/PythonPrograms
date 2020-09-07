A=[3,1,2,4,3]

b = len(A)
print(b)
sum = 0
sub = 0
z= []


for x in range(1,len(A)):
    for c in range(x,b,1):
        sum+=A[c]
    for y in range(0,x,1):
        sub+=A[y]
    total = sum-sub
    if(total < 0):
        total = abs(total)
    print("total",total)
    z.append(total)
    print(z)
    print("sum",sum)
    sum = 0
    print("sub",sub)
    sub = 0
print("least",min(z))


