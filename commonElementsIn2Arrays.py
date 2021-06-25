def common(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            print(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1


if __name__ == '__main__':
    arr1 = []
    arr2 = []
    len_arr1 = int(input())
    len_arr2 = int(input())
    for x in range(len_arr1):
        arr1.append(int(input()))
    for y in range(len_arr2):
        arr2.append(int(input()))
    common(arr1, arr2)
