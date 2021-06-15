#!/usr/bin/python3

# This program outputs:

# Content-Type: text/html
# 
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
# <html>
# <head>
# <title>Now's the time</title>
# <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
# </head>
# 
# <body >
# <form action="" name="form1" method="POST">
# 
#         <h3>My Page</h3>
#         <p>Now is the time for all good folks
#         to come to the aid of their country.</p>
# 
# </form>
# </body>
# </html>

from htmlpage import HtmlPage

class MyPage(HtmlPage):
    
    def __init__(self):
        HtmlPage.__init__(self, "Now's the time")

    def getHtmlContent(self):
        return '''
        <h3>My Page</h3>
        <p>Now is the time for all good folks 
        to come to the aid of their country.</p>
        '''

if __name__ == '__main__':
    myPage = MyPage()
    myPage.go()

