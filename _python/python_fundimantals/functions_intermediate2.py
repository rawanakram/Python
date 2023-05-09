x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1-Update Values in Dictionaries and Lists
#1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students)

#3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

#4.Change the value 20 in z to 30
z[0]['y']=30
print (z)

#2-Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for i in some_list:
        for key,val in i.items():
            print(key, " _ ", val)
iterateDictionary(students)

#3-Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary [key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4-Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key,val in some_dict.items():
        print(len(val),key)
        for value in val:
            print(value)

printInfo(sports_directory)

