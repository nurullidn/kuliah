import os
os.system("cls")

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = [] # list kosong buat nampung data

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))

    if left:
        result += left
    elif right:
        result += right
    return result 

angka = [2, 1, 9, 4, 6]

hasil = mergeSort(angka)

print("List Belum Terurut")
print("[2, 1, 9, 4, 6]")
print("List Sudah terurut")

print(hasil)