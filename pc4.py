import time
import urllib
# import urllib2
import re

#=========================================
#urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
#end. 400 times is more than enough
#=========================================
#----------The first nothing is 12345------
# response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
#response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
print response.info()
html = response.read()

print html

response.close()

raw_input()
