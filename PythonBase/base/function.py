# encoding: UTF-8

def test(str):
    print str


test("asdfasd")


# 可变对象传递（引用类型）
def testObj(list):
    #adfadsf
    list.append([2, 345, 1])
    print list


list1 = [24, 5, 6]
testObj(list1)
print(list1)
print(set('boy'))


def get(name, age="22"):
    print name
    print age


get(78)


# 可写函数说明  不定长参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
# printinfo(10);
printinfo(70, 60, 50);

# lambda

add = lambda x, y: x + y

print add(3, 4)
