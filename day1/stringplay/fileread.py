content=""
for line in open("data.txt","r",encoding="UTF-8").readlines():
    #print(line)
    content +=line

print(content)