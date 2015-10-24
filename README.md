**Vweb** is a Simple Python Website Frame work.

Source: https://github.com/dlink/vweb

It has been created over a time to address reoccuring requirements for building simple websites.  It is Python CGI, but can be used with Cherrypy.  It is not MVC.  It consists of the following modules:

### Modules

* **HtmlPage** - Super class that controlls the processing and display of webpages

* **html**     - HTML Abstraction layer for generating HTML

* **HtmlTable** - HTML Table Abstraction layer for generating HTML Tables

* **htmlify** - Some utilities

* **examples**  - Examples

### Details

##### HtmlPage

HtmlPage is a Web Page that your code subclasses.  It consists primarily of

* A Constructor **__init__()** which you override, which allows you to dynamically build the HTML HEADER with Title, Javascript, CSS, auto_refesh, output_format (html, csv)

* A **process()** method which you overide for handling incoming GET and POST parameters.

* A **getHtmlContent()** method which you overrid for generating HTML BODY

* Debugging GET and POST Variables, as well as user defined DEBUG message.

Here is Hello World:

    from htmlpage import HtmlPage
    class HelloWorld(HtmlPage):
        def __init__(self):
            HtmlPage.__init__(self, "Hello World")
        def getHtmlContent(self):
            return '<p>Hello, World!</p>'
    if __name__ == '__main__':
        HelloWorld().go()

See Other [Examples](https://github.com/dlink/vweb/tree/master/examples)

__html__

**html** is a libary module of simple one-to-one python equivalent names for each HTML tag.  It is used to generate html in python, rather than using templates like Genshi, or PHP.

The following examples ...

    b('hi')
    p(font('some text', color='green'))
    a('Chapter 2', href='chapter2.html')
    div(center(column_chooser), id='columnChooser', class_='widget')
    
Returns these string:

    <b>hi</b>
    <p><font color='red'>text</font></p>
    <a href='chapter2.html'>Chapter 2</a>
    <div id="columnChooser" class="widget">
       <center>
          < … > 
       </center>
    </div>

__HtmlTable__

**HtmlTable** is an Abstraction layer for HTML TABLES, (and it rocks the house). It was inspired by perl's HTML:Table.  

By treating tables as Python objects similar to a list of lists, uses can work more freely and creatively, leaving the output of the HTML TABLE to the getTable() method.

This example …

    from htmltable import HtmlTable
    
    # Create table - Many parameter options exist.
    table = HtmlTable()
    
    # Header
    table.addHeader(['No.', 'President'])
    
    # Table Body
    table.addRow([1, 'George Washington']) 
    table.addRow([2, 'John Adams']) 
    
    # Format adjustments
    table.setColAlign(2, 'right')
    
    # Outputing the results
    print table.getTable()

Output the following

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
            <tr>
                <td>2</td>
                <td align="right">John Adams</td>
            </tr>
        </tbody>
    </table>

__Examples__

See [Examples](https://github.com/dlink/vweb/tree/master/examples)


__Requires__

vlib - [https://github.com/dlink/vlib](https://github.com/dlink/vlib)

__Installation__

Installation
------------

__Ubuntu__

Update apt-get to the latest libraries:

    apt-get update

Install pip, if you haven't done so already:

     apt-get install python-pip
     pip install -U pip

Install Mysql DB Connectorm, if you haven't done so already:

    apt-get install python-dev libmysqlclient-dev
    pip install MySQL-python

Install vlib:

    pip install vweb

