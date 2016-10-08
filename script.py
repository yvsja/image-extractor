import bs4 
import urllib.request
import re

print('Please Enter the URL')

url = input()

# print(url)

my_request = urllib.request.Request(url)
html = urllib.request.urlopen(my_request).read().decode('utf-8')

#print(html)

preg_name = re.compile('<img .*?>')

img_tags = preg_name.findall(html)

preg_imgsrc = re.compile('src=".*?"')

sources = []

for img in img_tags:
	src = preg_imgsrc.findall(img)[0]
	src = src[5:-1]
	sources.append(src)

print('Total Images Found: ' + str(len(sources)))

for src in sources:
	f = open(src[src.rfind('/') + 1:], 'wb')
	f.write(urllib.request.urlopen(urllib.request.Request(src)).read())
	f.close()
