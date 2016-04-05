#! /usr/bin/env python

from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It worked!")
