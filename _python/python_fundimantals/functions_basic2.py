#1-Countdown
def countdown (a):
    my_list=[]
    for i in range (a,-1,-1):
        my_list.append(i)
    return my_list

y = countdown(5)
print(y)

#2-Print and Return
def print_and_return(list_num):
    for x in list_num:
        print(list_num[0])
        return(list_num[1])

Mylist_num = [1,2]
y = print_and_return(Mylist_num)
print(y)

#3-First Plus Length
def First_Plus_Length(first_list):
    sum=0
    for i in range (0, len(first_list)):
        sum = first_list[0] + len(first_list)
    return sum 

Mylist = [1,2,3,4,5]
y = First_Plus_Length(Mylist)
print(y)

#4-Values Greater than Second 
def greater (list):
    NewList=[]
    for i in range (0, len(list)):
        if list[i] > list[1]:
            NewList.append(list[i])
    print(len(NewList))
    if len(NewList)<2:
        return ("false")
    return NewList
    
myList=[4,2,3,1,5,6]
y=greater(myList)
print(y)

#5-This Length, That Value
def Length_Value(size,value):
    R_List=[]
    for i in range (0, size):
        R_List.append(value)
    return R_List

y=Length_Value (5,9)
print(y)