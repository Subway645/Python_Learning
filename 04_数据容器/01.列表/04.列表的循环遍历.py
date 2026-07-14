def list_while():
    my_list = [1,2,3,4,5]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element,end=" ")
        index += 1

def list_for():
    my_list = [1,2,3,4,5]
    for element in my_list:
        print(element, end=" ")

list_while()
print()
list_for()