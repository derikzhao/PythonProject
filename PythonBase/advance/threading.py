# encoding:UTF-8

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print "Starting " + self.name

        lock.acquire()
        print_time(self.name, self.delay, 5)
        print "Exiting " + self.name

        lock.release()


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

lock = threading.Lock()

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

threads = []

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成


print "Exiting Main Thread"
