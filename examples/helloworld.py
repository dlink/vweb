#!/bin/env python

from htmlpage import HtmlPage

class HelloWorld(HtmlPage):
    
    def __init__(self):
        HtmlPage.__init__(self, "Hello World")

    def getHtmlContent(self):
        return '<p>Hello, World!</p>'

if __name__ == '__main__':
    HelloWorld().go()

# The above program outputs the following...
"""
Content-Type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
<title>Hello World</title>
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
</head>

<body >
<form action="" name="form1" method="POST">
<p>Hello, World!</p>
</form>
</body>
</html>
"""
