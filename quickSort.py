import random

def quickSort(list_a):
    length = len(list_a)
    if length <=1:
        return  list_a
    else:
        pivot = list_a.pop()

    itemsGreater = []
    itemsLower = []

    for item in list_a:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)
    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)

og_list = []
og_list_length = int(input("Please type down the size of the tabel.\n"))
for x in range(0, og_list_length):
    og_list.append(random.randint(1,99))
print("Your un-sorted list is: ")
for z in og_list:
    print(z, end=" ")
print("\n")
og_list = quickSort(og_list)
print("Your insertion-sorted list is: ")
for y in og_list:
    print(y, end=" ")