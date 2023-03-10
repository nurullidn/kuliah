import os
os.system("cls")

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Gabungkan array temp kembali menjadi arr[l.. r]
    i = 0     # index awal subarray pertama
    j = 0     # index awal subarray kedua
    k = l     # index awal subarray gabungan
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Salin elemen L[], jika ada
    # apakah ada
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Salin elemen R[], jika ada
    # apakah ada
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l adalah untuk indeks kiri dan r adalah indeks kanan dari
# sub-array arr yang akan diurutkan
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Sama seperti (l+r)//2, tetapi menghindari luapan untuk
        # l dan h besar
        m = l+(r-l)//2
 
        # Urutkan bagian pertama dan kedua
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# Kode driver untuk diuji di atas
arr = [12, 1, [22, 3, [8, 14]], 2,6,[11],90]
n = len(arr)
print("list belum terurut")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nlist sudah terurut")
for i in range(n):
    print("%d" % arr[i],end=" ")