a=int(input("please enter first number of an A.p serise::"))
n=int(input("please enter the total numbers in this A.p serise::"))
total=(n*(2*a+(n-1)*d))/2
tn=a+(n-1)*d
i=a
print("\n the tn Term of Arithmatic progreesion series=",tn)
print("the sum of Arithmatic progression series:")
while(i<=tn):
    if(i!=tn):
        print("%d+%d"%i,end="")
    else:
        print("%d=%d"%(i,total))
        i=i+d
