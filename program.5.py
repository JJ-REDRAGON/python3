#nested for loops

for a in range(1,10+1):
    for b in range(1,5+1):
        print(b,end=' ')
    print()

print('---')

psym = input('enter a character: ')
height = int(input('enter yout height: '))
for a in range(1,height+1):
    for b in range(1,a+1):
        print(psym,end=' ')
    print()
