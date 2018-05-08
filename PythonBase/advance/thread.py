# encoding:UTF-8
import numpy as np
import thread


def threadTest(name):
    print("asdf")
    for i in np.arange(10):
        print name + "-" + str(i) + "\n"



thread.start_new_thread(threadTest, ("thread1",))
thread.start_new_thread(threadTest, ("thread2",))

while 1:
    pass