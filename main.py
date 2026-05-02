import random
import time
import sys
sys.setrecursionlimit(999999)
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted,right_sorted)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def quick_sort(arr, l, r):
    if l>=r:
        return
    pivot = arr[r]
    i = l
    for j in range(l,r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    quick_sort(arr,l,i-1)
    quick_sort(arr,i+1,r)

x = [10**3, 10**4, 10**5, 10**6]
sorted_time = []
merge_sort_time = []
quick_sort_time = []

for i in range(3,7):
    arr = [random.randint(1, 1000) for _ in range(10**i)]
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    print(f"Размер массива: {10**i}")
    print(f"{'Метод':<22} | {'Время (мс)'}")

    # sorted()
    start = time.perf_counter()
    _ = sorted(arr1)
    t1 = (time.perf_counter() - start) * 1000
    sorted_time.append(round(t1,3))

    # merge sort
    start = time.perf_counter()
    merge_sort(arr2)
    t2 = (time.perf_counter() - start) * 1000
    merge_sort_time.append(round(t2,3))

    # quick sort
    start = time.perf_counter()
    quick_sort(arr3, 0, len(arr3) - 1)
    t3 = (time.perf_counter() - start) * 1000
    quick_sort_time.append(round(t3,3))

    print(f"{'Python sorted()':<22} | {t1:.3f}")
    print(f"{'Сортировка слиянием':<22} | {t2:.3f}")
    print(f"{'Быстрая сортировка':<22} | {t3:.3f} \n")

plt.figure(figsize=(9,6))
plt.xlabel('Размер массива', fontsize = 15)
plt.ylabel('Время (мс)', fontsize = 15)
plt.plot(x, sorted_time, color = 'red')
plt.plot(x, merge_sort_time, color = 'green')
plt.plot(x, quick_sort_time, color = 'purple')
plt.xscale('log')
plt.legend(labels = ['Python sorted()', 'Сортировка слиянием', 'Быстрая сортировка'])
plt.grid()
plt.show()
