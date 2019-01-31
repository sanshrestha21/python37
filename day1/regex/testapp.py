f=open ("data.txt","w+")
    

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