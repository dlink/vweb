#!/usr/bin/env python

# This page shows how to capture incoming parameters
#
# It changes the background color of a div based on a pull down list.
# cute, I know.

from htmlpage import HtmlPage

class DoSomething(HtmlPage):
    
    def __init__(self):
        HtmlPage.__init__(self, "Do Something")
        self.bgcolor = 'lightblue'
        # Turn on/off Debug CGI
        #self.debug_cgi = True 

    def process(self):
        HtmlPage.process(self)
        if 'bgcolor' in self.form:
            self.bgcolor = self.form['bgcolor'].value
            
    def getHtmlContent(self):
        output = ''
        output += '<h3>Do Something</h3>'
        output += '<div style="background-color: %s;">' % self.bgcolor
        output += '<p style="padding: 100px">Choose background color:'
        output += self.getColorMenu()
        output += '</div>'
        return output

    def getColorMenu(self):
        return '''
        <select name="bgcolor" onChange="javascript:submit();">
          <option value="lightblue">lightblue</option>
          <option value="lightgreen">lightgreen</option>
          <option value="lightyellow">lightyellow</option>
        </select>
        '''

if __name__ == '__main__':
    p = DoSomething()
    p.go()

