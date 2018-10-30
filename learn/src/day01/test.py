import urllib.request
a_url = 'http://www.baidu.com'
data = urllib.request.urlopen(a_url).read()
print(data)

#测试结构

data = urllib.request.urlopen(a_url).read()
print(data)