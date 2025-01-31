n=50
for i in range(n):
    print((i+1))

for i in range(n):
    if(((i+1)%15)==0):
        print("fizzbuzz")
    elif(((i+1)%3)==0):
        print("fizz")
    elif(((i+1)%5)==0):
        print("buzz")
    
    else:
        print(i+1)
         