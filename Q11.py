number_list = [1,2,3,4,5]

def square_each(number_list):
    new_list = [i * i for i in number_list]
    return new_list

new_list = square_each(number_list)
print(new_list)