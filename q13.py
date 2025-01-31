def dupremover(list):
    
    b = []
    for x in list:
        if x not in b:
            b.append(x)
    print(b)
def main():
    a = [1, 2, 2, 3, 4, 4, 5]
    dupremover(a)


if __name__=="__main__":
    main()