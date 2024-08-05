def pickingNumbers():
    a = [1, 1, 2, 3, 2, 4, 4, 5, 5, 2, 5, 6, 7, 6, 6, 8, 9, 8, 9, 0]
    a.sort()
    temparr = []
    maxArrr = 0
    min = a[0]
    for i in a:
        print(i, i - min)
        if (i - min) <= 1:
            temparr.append(i)
        else:
            if len(temparr) >= maxArrr:
                maxArrr = len(temparr)
            min = i
            temparr.clear()
            temparr.append(i)
    if len(temparr) >= maxArrr:
        maxArrr = len(temparr)

    print(f"The length of maximum sub list is {maxArrr}")

pickingNumbers()