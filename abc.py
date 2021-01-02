listt=[1,2,3,4,5,6,7,8]
l=len(listt)
for i in range(0,l,1):
    if i%2==0:
        temp=listt[i]
        listt[i]=listt[i+1]
    else:
        listt[i]=temp   

print(listt)

