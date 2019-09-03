list1 = list(map(int,input().split(' ')))
list2 = list(map(int,input().split(' ')))
biglist = list1 + list2
biglist.sort()
def middle(a):
    split = (len(a))% 2
    if (split != 0):
        add = a[split] + a[split+1]
        return add
    else:
        add2 = a[split] + a[split-1]
        return add2
output = middle(biglist)
print(output)



