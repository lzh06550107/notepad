import urllib.request
a_url = 'http://www.baidu.com'
data = urllib.request.urlopen(a_url).read()
print(data)