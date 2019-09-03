list1 = list(map(int,input().split(' ')))
list2 = list(map(int,input().split(' ')))
a = list1 + list2
a.sort()
split = (len(a))% 2
    if (split != 0):
        add = a[split] + a[split+1]
        print(add)
    else:
        add2 = a[split] + a[split-1]
        print(add2)



