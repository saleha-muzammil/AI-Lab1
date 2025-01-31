def fibonacigen(n):
    output=[]
    a,b=0,1
    for _ in range(n):
        output.append(a)
        a,b = b,a+b
    return output

def main():
    n = int(input("Enter the number of terms: "))
    fib_sequence = fibonacigen(n)
    print(fib_sequence)

if __name__=="__main__":
    main()
