import random

def insertionSort(list_a):
    list_length = range(1, len(list_a))
    for i in list_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -= 1
    return list_a

og_list = []
og_list_length = int(input("Please type down the size of the tabel.\n"))
for x in range(0, og_list_length):
    og_list.append(random.randint(1,99))
print("Your un-sorted list is: ")
for z in og_list:
    print(z, end=" ")
print("\n")
og_list = insertionSort(og_list)
print("Your insertion-sorted list is: ")
for y in og_list:
    print(y, end=" ")
