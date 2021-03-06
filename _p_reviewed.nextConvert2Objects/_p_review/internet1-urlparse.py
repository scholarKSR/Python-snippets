#! /usr/bin/python

#INTERNET
#urlparse()

from urlparse import urlparse
url0 = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url0)
print parsed
#
url1 = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url1)
print 'scheme   :', parsed.scheme
print 'netloc   :', parsed.netloc
print 'path     :', parsed.path
print 'params   :', parsed.params
print 'query    :', parsed.query
print 'fragment :', parsed.fragment
print 'username :', parsed.username
print 'password :', parsed.password
print 'hostname :', parsed.hostname, '(netloc in lowercase)'
print 'port     :', parsed.port

#urlsplit()
#for urls following RFC 2396
print '-------urlsplit-----------'
from urlparse import urlsplit
url2 = 'http://uer:pwd@NetLoc:80/p1;param/p2;param?query=arg#frag'
parsed = urlsplit(url2)
print parsed
print 'scheme   :', parsed.scheme
print 'netloc   :', parsed.netloc
print 'path     :', parsed.path
#print 'params   :', parsed.params
print 'query    :', parsed.query
print 'fragment :', parsed.fragment
print 'username :', parsed.username
print 'password :', parsed.password
print 'hostname :', parsed.hostname, '(netloc in lowercase)'
print 'port     :', parsed.port

#urldefrag()
#for fragment identifier
print '-------urldefrag-----------------'
from urlparse import urldefrag
original = url0
print 'Original: ',  original
url, fragment = urldefrag(original)
print 'url		:', url
print 'fragment:', fragment

#unparsing
print '--------unparsing-----------'
from urlparse import urlparse
original= url0
print 'ORIG 	:',original
parsed = urlparse(original)
print 'PARSED	:',parsed.geturl()
#geturl() only works on the object returned by urlparse() or urlsplit()
#
print '------'
from urlparse import urlparse, urlunparse
original= url0
print 'ORIG 	:',original
parsed = urlparse(original)
print 'PARSED	:',type(parsed),parsed
t = parsed[:]
print 'TUPLE	:', type(t),t
print 'NEW		:', urlunparse(t)

#if the url included superfluous parts those may be dropped from the reconstructed url
print '-------'
from urlparse import urlparse, urlunparse
original= 'http://netloc/path;?#'
print 'ORIG 	:',original
parsed = urlparse(original)
print 'PARSED	:',type(parsed),parsed
t = parsed[:]
print 'TUPLE	:', type(t),t
print 'NEW		:', urlunparse(t)

#JOINING
print '-------JOINING----------'
from urlparse import urljoin
print urljoin('http://www.example.com/path/file.html','anotherfile.html')
print urljoin('http://www.example.com/path/file.html','../anotherfile.html')

#non relative parts are handled the same way as os.path.join()
print urljoin('http://www.example.com/path/', '/subpath/file.html')
print urljoin('http://www.example.com/path/', 'subpath/file.html')


'''
more info:
>http://docs.python.org/lib/module-urlparse.html
>urllib (pg 651)
>urllib2 (pg 657)
>RFC 1738 (http://tools.ietf.org/html/rfc1738.html) URL syntax
>RFC 1808 (http://tools.ietf.org/html/rfc1808.html) relative urls
>RFC 2396 (http://tools.ietf.org/html/rfc2396.html)URI generic syntax
>RFC 3986 (http://tools.ietf.org/html/rfc3986.html)URI syntax
'''
