def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()

multiplication_table()