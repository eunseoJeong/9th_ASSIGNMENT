N = int(input(">> "))

if ((N<=0) or (N>=10)):
    exit

li = []

for i in range (N+1) : 
    li.append(i)

for j in range (N) :
    print(li[2:N:2])
    print(li[1:N+1:2])