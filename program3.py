#For loops

for count in range(10):
    print(count)

print('--')

for x in range(6):
    print(x)

print('--')

for x in range(1,11):
    print(x)

print('--')

for x in range(3,14):
    print(x)

print('--')

for x in range(7,33):
    print(x)
    
print('--')

for x in range(1,22,2):
    print(x)

print('--')

for student in range(1,29+1,1):
    print('chocolate',student)

print('--')

for ps5 in range(50,0,-1):
    print('playstation 5 : ',ps5)

print('--')

friends = ['John','Aaron','Toaster','Alpha','Tom']

for f in friends:
    print('Invite sent to ',f)

print('--')

start = int(input('Enter a starting number: '))
end = int(input('Enter a ending number: ')) +1

for x in range(start,end):
    print(x)
