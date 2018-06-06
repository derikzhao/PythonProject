# encoding: UTF-8

import time
import calendar
import datetime

ticks = datetime.time()
print ticks

localtime = time.localtime(datetime.time())
print localtime
print localtime[0]

i = datetime.datetime.now()
print i
print i.day

print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))


print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

cal = calendar.month(2018, 4)
print cal
print(time.timezone / 60 / 60)