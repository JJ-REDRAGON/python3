numberlist = [15,1,12,57,23,92]
print(numberlist)
numberlist.sort()
print(numberlist)
numberlist.sort(reverse=True)
print(numberlist)

print('---')

newlist = [90,20,40,45,63,1,3,20,10,4]
l = len(newlist)
print(newlist)
print(l)

for i in range(0,l):
    for j in range(i,l):
        if newlist[i] > newlist[j]:
            t = newlist[i]
            newlist[i] = newlist[j]
            newlist[j] = t

print(newlist)
