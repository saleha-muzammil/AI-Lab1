
list1=[]
print("Enter the list of words")
for i in range(5):
    list1.append(input())

dict1={}
for i in list1:
    if(i in dict1):
        dict1[i]+=1
    else:   
        dict1[i]=1

print("The frequency of each word is",dict1)
