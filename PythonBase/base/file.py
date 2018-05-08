
fo = open("D:/test/text.txt", "w+")


with open("D:/test/test.txt", "a") as f:
    #print f.read()
    f.write(".,.,.,lk")

with open("D:/test/test.txt", "r") as f:
    print f.read()
