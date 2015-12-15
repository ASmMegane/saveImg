import urllib2, re, urllib


def saveImage(img,name,number):    
    image = urllib2.urlopen(img).read()
    try:
        out = open(str(number) + '_' + name, 'wb')
        out.write(image)
        out.close()
    except IOError:
        newName = 'unnamedFile-' + str(number)
        out = open(str(number) + '_' + newName, 'wb')
        out.write(image)
        out.close()
    

url = 'http://lenta.ru/'
content = urllib2.urlopen(url).read()
imgUrls = re.findall('<img .*? src="(.*?)"', content)
count = len(imgUrls)

i = 0
for i in range(count):
    startNameImg = imgUrls[i].rfind('/')
    nameImage = imgUrls[i][startNameImg + 1:]
    saveImage(imgUrls[i], nameImage, i)

print "Loading is complete"
