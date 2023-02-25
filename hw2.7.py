from random import randint

"""bubble_sort"""

def bubble_sort(arr):
    for i in range(10):
        for j in range(10 - i - 1):
            if arr[j] > arr[j + 1]:
                num = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = num
sort_arr = []
for i in range(10):
    sort_arr.append(randint(1, 30))
bubble_sort(sort_arr)
print(sort_arr)

"""binary_search"""

search = int(input('Num:'))
def binary_search(search, sort_arr ):
    mid = len(sort_arr) // 2
    low = 0
    high = len(sort_arr) - 1
    while sort_arr[mid] != search and low <= high:
        if search > sort_arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        print('Элемент не найден')
    else:
        print("Элемент найден", mid)
binary_search(search, sort_arr)

