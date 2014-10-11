#!/usr/bin/env python

# This page shows how to use HtmlTable, and html methods

from htmlpage import HtmlPage
from htmltable import HtmlTable
from html import *

class AmericanPanters(HtmlPage):
    
    def __init__(self):
        HtmlPage.__init__(self, "Painters")
        self.style = 'body {background-color: lightblue}' \
                     'table {background-color: white}'
        
    def getHtmlContent(self):
        return self.getHeader() + \
               self.getBody() + \
               self.getFooter()

    def getHeader(self):
        return center(h3('American Painters'))

    def getBody(self):
        table = HtmlTable(cellspacing=2, cellpadding=2, border=1)
        table.addHeader(['Painter', 'Style', 'Born', 'Until'])
        table.setRowBGColor(table.rownum, 'lightgreen')
        for row in self.getData():
            table.addRow(row)
        return center(table.getTable())
    
    def getFooter(self):
        return ''

    def getData(self):
        href = 'https://www.google.com/search?q=%s'
        painters=[['Andy Warhol', 'Pop', 1928, 1987], 
                  ['Elsworth Kelly', 'Minimal',1933, 'Living Spencertown, NY'],
                  ['Jackon Pollock', 'Abstract Expressionist', 1912, 1956],
                  ['Sol LeWitt', 'Conceptualist', 1928, 2007],
                  ['Robert Motherwell', 'Abstract Expressionist', 1915, 1991],
                  ]
        # Convert names to links
        for p in painters:
            p[0] = a(p[0], href=href % p[0])
        return painters
            
if __name__ == '__main__':
    AmericanPanters().go()
    

