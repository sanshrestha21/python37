text=""
#content=""
for line in open("data.txt","r",encoding="UTF-8").readlines():
    #print(line)
    #content +=line
    text +=line

#print(content)
pattern="python"
counter=0
tlen=len(text)
plen=len(pattern)
text=text.lower()
pattern=pattern.lower()

for i in range(0,tlen-plen):
    total=0
    for j in range(0,plen):
        if(text[i+j]==pattern[j]):
            total +=1
    if(total==plen):
        counter +=1

print("total characters: %d" %tlen)
print("total many matches: %d" %counter)
