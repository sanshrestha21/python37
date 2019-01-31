text="aaaaabcaaccbbabcabcabcabbbcabc"

pattern="abc"

counter=0
i,j,index=0,0,0
tlen=len(text)
plen=len(pattern)

while(i<tlen):
    if(text[i]==pattern[j]):
        i +=1
        j +=1
        if(j==plen):
            counter +=1
            j=0
    else:
            index +=1
            i=index
print("total character : %d" %tlen)
print("total matches : %d" %counter)
