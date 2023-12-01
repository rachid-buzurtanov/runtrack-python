liste1 = [392, 1092, 29, 4509, 898, 88]
liste2 = [209, 59, 910, 4320, 903, 4]

def bubble_sort(arr):
    n = 0           
    for _ in arr:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

bubble_sort(liste1)
bubble_sort(liste2)



