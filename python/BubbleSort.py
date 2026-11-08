def bubblesSort(list):
    for number in range(len(list)-1, 0, -1):
        for n in range(number):
            if list[n] > list[n+1]:
                temp = list[n]
                list[n] = list[n+1]
                list[n+1] = temp
                listchanged = True
            if not listchanged:
                break
list=[7, 3, 8, 5, 6, 4,]
bubblesSort(list)
print(list)