list1 = []
list2 = []

leng = int(input())
for i in range(0,leng):
    ele1 = int(input())
    list1.append(ele1)
for i in range(0,leng):
    ele2 = int(input())
    list2.append(ele2)
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



