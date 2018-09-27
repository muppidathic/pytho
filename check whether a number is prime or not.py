N=int(input("N="))
k=0
for x in range(1,N+1):
    if(N%x==0):
        k=k+1
if(k==2):
    print("Yes")
else:
    print("No")
