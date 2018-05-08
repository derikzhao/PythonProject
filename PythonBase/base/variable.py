# encoding: UTF-8
import cmath
import math


'''
for a in "asdfasdfas":
    print  '当前：' + a

i = 0
while i < 10:
    # print i
    i += 1

if ("a" in "asdfasdf"):
    print "true"
'''
a = math.sqrt(3)
print(a)
b = cmath.sqrt(4)
print(b)

list1 = [1, 2, 34, "2"]
'''
print list1[1:len(list1)]

for x in list1:
    print(x)

for index in range(len(list1)):
    print list1[index]
'''
list1.append(6)
list1.append("45")

print(list1)

tuple1 = (1, 4, 6, 7, 8)
tuple2 = (4, 5, 6, 7, 0)
print tuple1[1:3]
print tuple1 + tuple2

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print dict["Name"]

dict["Name"] = "tom"
print dict["Name"]

for x in dict:
    print dict[x]

dict2 = dict.copy()
print(dict)
print(dict2)
del dict["Name"]
print(dict)
print(dict2)
print(dict2.has_key("Name"))


#集合 set 无序，不重复序列

set1 = {"1", "2"}
# {'1', '2'}
print(type(set1))