import random


def bubble(list_a):

    list_length = len(list_a) - 1
    ifSorted = False

    while not ifSorted:
        ifSorted = True
        for i in range(0, list_length):
            if list_a[i] > list_a[i+1]:
                ifSorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

og_list = []
og_list_length = int(input("Please type down the size of the tabel.\n"))
for x in range(0, og_list_length):
    og_list.append(random.randint(1,99))
print("Your not sorted list is: ")
for z in og_list:
    print(z, end=" ")
print("\n")
og_list = bubble(og_list)
print("Your sorted list is: ")
for y in og_list:
    print(y, end=" ")