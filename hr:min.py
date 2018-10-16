import datetime
a='2014-05-06 12:00:56'
b='2013-03=06 16:08:22'
start=datetime.datetime.strptime(a,'%Y-%m-%d %H%M:%S')
ends=datetime.datetime.strptime(b,'%Y-%m-%d %H:%M:%S')
diff=start-ends
