def commonElements(a, b, c):
    # a = [1, 5, 10, 20, 40, 80]
    # b = [6, 7, 20, 80, 100]
    # c = [3, 4, 15, 20, 30, 70, 80, 120]
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            print(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1


if __name__ == '__main__':
    arr1 = []
    arr2 = []
    arr3 = []
    len_arr1 = int(input())
    len_arr2 = int(input())
    len_arr3 = int(input())
    for x in range(len_arr1):
        arr1.append(int(input()))
    for y in range(len_arr2):
        arr2.append(int(input()))
    for z in range(len_arr3):
        arr3.append(int(input()))
    commonElements(arr1, arr2, arr3)
