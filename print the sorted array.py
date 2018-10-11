list=[]
num=int(input("how many numbers:")) 
for i in range(num):
    num=int(input("enter a number:"))
    list.append(num)
    print("the sorted array is",sorted(list))
