list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for number in list1:
    for num in list2:
        x = number * num
        list3.append(x)

print(list3)