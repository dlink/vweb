vweb is a simple Python Website Frame work.

It is Python CGI, but can be used with Cherrypy.  It is not MVC.

* htmlpage - Is a website page which processes cgi parameters.

             You subclass it and override 

             - process() for handling incoming parameters, and
             - getHtmlContent() to display the page.

* html     - Is an html abstraction layer

                b('hi')
                p(font('some text', color='green'))
                a('Chapter 2', href='chapter2.html')

             Returns these string:

                <b>hi</b>
                <p><font color='red'>text</font></p>
                <a href='chapter2.html'>Chapter 2</a>

* htmltable - Is an html table abstraction layer
              Inspired by perl's HTML:Table

                 from htmltable import HtmlTable

                 table = HtmlTable()
                 table.addHeader(['No.', 'President'])
                 table.addRow([1, 'George Washington']) 
                 table.setColAlign(2, 'right')
                 print table.getTable()

              Returns:

                 <table cellpadding="0" cellspacing="0">
                   <thead>
                     <tr>
                       <th>No.</th>
                       <th align="right">President</th>
                     </tr>
                   </thead>
                   <tbody>
                     <tr>
                       <td>1</td>
                       <td align="right">George Washington</td>
                     </tr>
                   </tbody>
                 </table>


* examples(n).py - Examples of how to use the code.
