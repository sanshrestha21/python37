from __future__ import print_function
def writefile():

    f= open("data.txt","w+")
    

    line=""
    for n in range(1,26):
        if(line==""):
            line=str(n)
        else:
            line = line + " " + str(n)
        if(n%5==0):
            print(line)
            f.write(line+"\n")
            line=""
    
    f.close()

def readfile():
    dataset=[]
    f=open("data.txt","r")


    for line in f.readlines():
        data=line.split(" ")
        for i in range(0,len(data)):
            data[i]=int(data[i])
        dataset.append(data)
    f.close()
    return dataset


dataset=readfile()

sum=0
for i in range(0,len(dataset)):
    output=""
    for j in range(0,len(dataset[i])):
        output +=" "
        if(i==j):
            sum +=dataset[i][j]
            output +=str(dataset[i][j])
            print(output,end=" ")
    print("")
print(sum)

