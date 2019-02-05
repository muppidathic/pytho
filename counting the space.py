input -file=input("Enter File name:")
file -text=open(input-file)
text=file-txt.real()

space,line,charc=0

for i in text:
    if(i==""):
        space+=1
    elif(i=="\n"):
        line+1
    else:
        char+=1
print("space={}\n Lines={}\n characters={}".format(space,line,charc))        
        
        
        
        
        
        
