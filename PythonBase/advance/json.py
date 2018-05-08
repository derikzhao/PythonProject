# encoding:UTF-8

import json
import simplejson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

str = json.dumps(data)

print(str)

data2 = json.loads(str)
print(data2)
print(data2[0]["a"])

str2 = simplejson.dumps(data)
print(str2)

data3 = simplejson.loads(str2)
print(data3)

