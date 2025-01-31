def FindPalindrome(string:str):
    i=0
    j=len(string)
    while(j>=i):
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True
string=input('Enter a string ').strip().replace(' ','').lower()
print(string)
if FindPalindrome(string):
    print('it is palindrome')
else:
    print('it is not a palindrome')