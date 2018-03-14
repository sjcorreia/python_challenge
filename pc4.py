import time
import urllib
# import urllib2
import re

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'

# =========================================
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough
# =========================================
# ----------The first nothing is 12345------
nothing = '12345'
for x in xrange(400):
    response = urllib.urlopen(URL % nothing)
    # print response.info()
    html = response.read()
    response.close()
    # print html
    try:
        nothing = html.split()[5]
    except:
        print html
        break
