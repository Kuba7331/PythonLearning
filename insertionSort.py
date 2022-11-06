import random

def insertionSort(list_a):
    list_length = range(0, len(list_a) - 1)
    for i in list_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
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
