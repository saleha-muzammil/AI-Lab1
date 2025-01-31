def dictmerger(d1,d2):
    d1.update(d2)
    print(d1)
def main():
    d1={'x': 1, 'y': 2}   
    d2={'y': 3, 'z': 6}  
    d3 ={**d1, **d2}
    # //dictmerger(d1,d2)
    print(d3)


if __name__=="__main__":
    main()

