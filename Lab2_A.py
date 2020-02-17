'''
Lab2_A
student ID 62055001
student ID 62055008
'''
print("student ID 62055001")
print("student ID 62055008")

#1 Tuple
#1.1 Write a Python program to create a tuple.
print("#1.1")
my_tuple = (1, 2, 3)
print("create a tuple :",my_tuple)                                                     #output (1, 2, 3)

#1.2 Write a Python program to create a tuple with numbers and print one item.
print("#1.2")
a, b, c = my_tuple
print("print one item :",c)                                                            #output 3

#1.3 Write a Python program to add an item in a tuple.
print("#1.3")
my_tuple += (4, 5, 6)
print("Add an item in a tuple :",my_tuple)                                             #output (1, 2, 3, 4, 5, 6)

#1.4 Write a Python program to get the 4th element and 4th element from last of a tuple.
print("#1.4")
element = my_tuple [3]
print("4th element :",element)                                                           #output 4

element1 = my_tuple [-4]
print("4th element from last :",element1)                                                #output 3

#1.5 Write a Python program to find the repeated items of a tuple.
print("#1.5")
count = my_tuple.count(3)
print("Count tuple :",count)                                                #output 1

#1.6 Write a Python program to convert a list to a tuple.
print("#1.6")
your_tuple = tuple(my_tuple)
print("Convert to a tuple :",your_tuple)                                           #output (1, 2, 3, 4, 5, 6)

#1.7 Write a Python program to slice a tuple.
print("#1.7")
slice = my_tuple[1:4]
print("slice[1:4] :",slice)                                                #output (2, 3, 4)

_slice = my_tuple[:4]
print("slice[:4] :",_slice)                                               #output (1, 2, 3, 4)

_slice = my_tuple[:]
print("slice[:] :",_slice)                                               #output (1, 2, 3, 4, 5, 6)

#1.8 Write a Python program to find the length of a tuple.
print("#1.8")
print("Length of a tuple :",len(my_tuple))                                        #output 6

#1.9 Write a Python program to unzip a list of tuples into individual lists.
print("#1.9")
my2_tuple = [("A",1) , ("B",2) , ("C",3) , ("D",4)]
print("New tuple :",my2_tuple)
print("Individual lists :",list(zip(*my2_tuple)))                                #output [('A', 'B', 'C', 'D'), (1, 2, 3, 4)] 
         
#1.10 Write a Python program to replace last value of tuples in a list.
'''
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''
print("#1.10")
my_num = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(my_num)                                               
print("Replace last value :",[a[:-1] + (100,) for a in my_num])                    #output [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
print("Replace last value :",[b[:2] + (100,) for b in my_num])                     #output [(10, 20, 100), (40, 50, 100), (70, 80, 100)]      

print([c[:2] + (9999,) for c in my2_tuple])                 #output [('A', 1, 9999), ('B', 2, 9999), ('C', 3, 9999), ('D', 4, 9999)]

#dictionary
print(2)
#2.1 Write a Python script to sort (ascending and descending) a dictionary by value.
print("#2.1")
import operator  
my_dic = {1:2, 3:4, 5:6, 7:8, 9:0}  
print('Dictionary : ',my_dic)  
sorted_my_dic = sorted(my_dic.items(), key=operator.itemgetter(0))  
print('Ascending : ',sorted_my_dic)  
sorted_my_dic = sorted(my_dic.items(), key=operator.itemgetter(0),reverse=True)  
print('Descending : ',sorted_my_dic) 

#2.2 Write a Python script to concatenate following dictionaries to create a new one.
'''
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
print("#2.2")
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
new_dic = {}
for create_dic in (dic1, dic2, dic3) : new_dic.update(create_dic)
print("Dictionaries 1 :",dic1)
print("Dictionaries 2 :",dic2)
print("Dictionaries 3 :",dic3)
print("Create a new dictionaries :",new_dic)

#2.3 Write a Python program to iterate over dictionaries using for loops.
print("#2.3")
print("For loops")
for iterate , value in new_dic.items():
    print (iterate, "x 10 =", new_dic[iterate])


#2.4 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
'''
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''
print("#2.4")
d=dict()
for x in range(1,16):
    d[x]=x**2
print("Both included")
print(d) 

#2.5 Write a Python program to iterate over dictionaries using for loops.
print("#2.5")
print("For loops")
for iterate , value in new_dic.items():
    print (iterate, "x 10 =", new_dic[iterate])

#2.6 Write a Python program to multiply all the items in a dictionary.
print("#2.6")
print(new_dic) 
result=1
for key in new_dic:    
    result = result*new_dic[key]   
print("Multiply all item :",result)

#2.7 Write a Python program to map two lists into a dictionary.
print("#2.7")
print("My tuple :",my_tuple)
my_letters = ["A", "B", "C", "D", "E", "F"]
print()
mapList = dict(zip(my_tuple, my_letters))
print("Map list :",mapList)

#2.8 Write a Python program to get the maximum and minimum value in a dictionary.
print("#2.8")
key_max = max(mapList.keys(), key=(lambda a: mapList[a]))
key_min = min(mapList.keys(), key=(lambda a: mapList[a]))

print('Max Value: ',mapList[key_max])
print('Min Value: ',mapList[key_min])

#2.9 Write a Python program to remove duplicates from Dictionary.
print("#2.9")
test_list = [{"tom": 1}, {"nine": 9}, {"tom": 1}, {"tom": 5}, {1:1}, {1:1}, {3:9}]
res_list = [i for n, i in enumerate(test_list) if i not in test_list[n + 1:]]
print("Test list :",test_list)
print("Duplicates list :",res_list)

#2.10 Write a Python program to combine two dictionary adding values for common keys.
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
print("#2.10")
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

#2.11 Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
'''
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
print("#2.11")


#2.12 Write a Python program to combine values in python list of dictionaries.
'''
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
'''
print("#2.12")

#2.13 Write a Python program to convert a list into a nested dictionary of keys.
print("#2.13")

#2.14 Write a Python program to remove spaces from dictionary keys.
print("#2.14")

#2.15 Write a Python program to get the key, value and item in a dictionary.
print("#2.15")

#2.16 Write a Python program to check multiple keys exists in a dictionary.
print("#2.16")

#2.17 Write a Python program to sort Counter by value.
'''
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
'''
print("#2.17")

#2.18 Write a Python program to replace dictionary values with their sum.
print("#2.18")

#2.19 Write a Python program to store a given dictionary in a json file.
'''
Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
print("hello world")
'''
print("#2.19")