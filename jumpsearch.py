import os
os.system('cls')


def jumpSearch(arr, x):

    n = len(arr)

    step = int( n ** 0.5)

    #mencari block yang berisi elemen x (input)
    prev = 0
    while arr[min(step, n) - 1]< x:
        prev = step
        step += int(n ** 0.5)
        if prev > n:
            return - 1

        
    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return - 1


    if arr[prev] == x:
        return prev

    return -1
    
data = [1, 2, 3, 4, 5]

x = 3

result = jumpSearch(data, x)
if result == -1:
    print(f"Elemen {x} tidak ditemukan")
else:
    print(f"Elemen ditemukan pada index ke - {result}")
