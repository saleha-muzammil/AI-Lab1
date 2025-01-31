def main():
    tuple = (1,2,3,4,5)
    a,b,*c = tuple
    print("First element:", a)
    print("Second element:", b)
    print("Rest of the elements:", c)
    
if __name__ == "__main__":
    main()