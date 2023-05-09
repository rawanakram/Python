#1-Biggie Size
def Biggie (list):
    for i in range (len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

myList = [-1, 3, 5, -5]
y = Biggie(myList)
print(y)

#2-Count Positives
def Count (list):
    sum=0
    for i in range (len(list)):
        if list[i] > 0 :
            sum+=1
    list[len(list)-1] = sum
    return list

myList = [1,6,-4,-2,-7,-2]
y= Count (myList)
print(y)
print(Count([-1,1,1,1]))

#3-Sum Total
def SumTotal (list):
    sum=0
    for i in range (len(list)):
        sum+=list[i]
    return sum 
myList = [1,2,3,4]
sum = SumTotal(myList)
print(sum)

#4-Average 
def Average (list):
    avg = SumTotal(list)/len(list)
    return avg 
result = Average([1,2,3,4])
print(result)

#5-Length 
def Length (list):
    count=0
    for i in list:
        count+=1
    return count
length1 = Length([37,2,1,-9])
print(length1)

#6-Minimum 
def Minimum (list):
    min=list[0]
    for i in range (len(list)):
        if list[i] < min:
            min = list[i] 
    return min
min = Minimum([37,2,1,-9])
print(min)

#7-Maximum 
def Maximum (list):
    max=list[0]
    for i in range (len(list)):
        if list[i] > max:
            max = list[i] 
    return max
max = Maximum([37,2,1,-9])
print(max)

#8-Ultimate Analysis
def Analysis (list):
    dict={'sumTotal':0,'average':0, 'minimum':0, 'maximum':0,'length':0}
    dict['sumTotal']=SumTotal (list)
    dict['average']=Average (list)
    dict['minimum']=Minimum (list) 
    dict['maximum']=Maximum (list)
    dict['length']=Length (list)
    return dict
myList = [37,2,1,-9]
print(Analysis (myList))

#9-Reverse List
def Reverse (list):
    for i in range(0,len(list)//2):
        temp=list[i]
        list[i]=list[len(list)-1-i]
        list[len(list)-1-i]=temp
    return list
myList = [37,2,1,-9]
result = Reverse (myList)
print(result)
    



