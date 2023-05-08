#1-basic
#by using for loop
for x in range(0,151):
    print(x)

#by using while loop
x=0
while x <= 150:
    print(x)
    x+=1

#2-multiple of five
for x in range (0,1000):
    if x % 5 == 0: 
        print(x)

#3-counting
for x in range (1,101):
    if x % 10 == 0: 
        print("Coding")
    elif x % 5 == 0: 
        print("Coding Dojo")
    else:
        print(x)

#4-Add odd integers 
sum = 0
for x in range (0,500001):
    if x % 2 != 0: 
        sum+=x
print(sum)

#5-Countdown by Fours
for x in range (2018,0,-4):
    print(x)

#6-Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range (lowNum,highNum+1):
    if x % mult == 0 :
        print(x)