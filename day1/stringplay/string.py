text="aabbabcabcaabbbcccabcabcabc"
pattern="abc"
counter=0
tlen=len(text)
plen=len(pattern)

for i in range(0,tlen):
    total=0
    for j in range(0,plen):
        if(text[i+j]==pattern[j]):
            total +=1
        else:
                break
    if(total==plen):
        counter +=1

print("total characters: %d" %tlen)
print("total matches: %d" %counter)
