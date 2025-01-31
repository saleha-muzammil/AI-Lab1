def Square(oldlist):
    newlist=[]
    for i in range(len(oldlist)):
        newlist.append(oldlist[i]*oldlist[i])
    return newlist

oldlist=[1,2,3,4,5]
print("printing the list after squaring the elements:")
final_list=Square(oldlist)
print(final_list)



    
