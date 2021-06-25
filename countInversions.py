def count():
    arr = [2, 4, 5, 6, 7]
    i = 0
    j = i + 1
    while i < len(arr):
        if i == j:
            j += 1
            i -= 1
        if arr[i] > arr[j]:
            print(arr[i], arr[j])
            i += 1
        elif arr[i] < arr[j]:
            j += 1
        if j == len(arr) - 1:
            j = i + 1
        print(0)


count()