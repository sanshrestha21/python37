f= open("data.txt","w+")
#my_list=[1,2,3,4,5]
#range=[1,25]
for item in range(1,25):
    
    for j in range(1,5):
        
        j +=1
        f.write("%d\t" % j)
        if j>5:
            print("\n")
            
           
            break
         
        #j==5
        #break;
        


f.close()

