text=""
for line in open("data.txt","r",encoding="UTF-8").readlines():
    text +=line

file=open("data1.txt","w")

for i in range(51):
    file.write(text)
    file.write("\r\n")

file.close()