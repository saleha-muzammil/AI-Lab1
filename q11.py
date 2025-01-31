def squarer(numbers):
    return [x**2 for x in numbers]
def main():
    num=[1,2,3,4,5]
    list=squarer(num)
    print(list)
if __name__=="__main__":
    main()
