print("Hello World")

#while 
a = 4  
counter = 0  
while counter < 3:  
    a = a + 1  
    print(a)  
    counter = counter + 1

#for
word = "Python"  
for each_char in word:  
    print(each_char)

for number in range(5, 8):  
    print(number)


i = 0
while i < 5:
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    elif i == 4:
        print("Break at 4")
        break
    else:
        pass
    print("Current value of i:", i)


for j in range(1, 6):
    if j == 3:
        print("Skipping 3")
        continue
    elif j == 5:
        print("Breaking at 5")
        break
    else:
        pass
    print("Current value of j:", j)  
      

























