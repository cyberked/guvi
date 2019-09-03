list1 = []
list2 = []

leng = int(input("Enter the size of array >> "))
for i in range(0,leng):
    ele1 = int(input("Enter the element of frist list >> "))
    list1.append(ele1)
for i in range(0,leng):
    ele2 = int(input("Enter the element of second list>> "))
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



