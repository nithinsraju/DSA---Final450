def merge():
    interval = [[1, 3], [2, 6], [8, 10], [15, 18], [0, 4], [1, 4]]
    i = 1
    interval.sort()
    if len(interval) < 2:
        return interval
    else:
        while i < len(interval):
            if interval[i][0] <= interval[i-1][1]:
                interval[i-1][1] = max(interval[i-1][1], interval[i][1])
                interval.pop(i)
            else:
                i += 1
        print(interval)


merge()
