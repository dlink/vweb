#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
#cgitb.enable(display=0, logdir="/tmp")

#import safecgi

# constants:

DEBUG_CGI = 0

class HtmlPage(object):
    '''Super Class that contains common characteristics and behavior
    for a common set of Html Pages.

    Usage: subclass: HtmlPage
           override: process() 
                     getHtmlContent()
                     style_sheets
                     javascript
                     javascript_src
                     debug_cgi
           set  : debug_msg if desired.
           call : go()
    '''
    
    def __init__(self, title='Unnamed', include_form_tag=1):
        self.title       = title
        self.form        = cgi.FieldStorage()
        self.page_num    = 1
        self.debug_msg   = ''
        self.style        = ''
        self.style_sheets = []
        self.javascript_src = []
        self.javascript   = ''
        self.debug_cgi    = DEBUG_CGI
        self.form_name    = 'form1'
        self.form_action  = ''
        self.body_attributes = ''
        self.include_form_tag = include_form_tag
        self.auto_refresh = 0 # For refreshing every n seconds.
        self.output_format = 'html'
        self.cookie        = None

    def process(self):
        '''CGI Process step.'''
        
        if self.debug_cgi:
            self.debug_msg += '<b>cgi form values:</b> <br/>'
            for p in self.form:
                self.debug_msg += "%s: %s<br/>" % (p, self.form[p].value)
        if 'csv' in self.form and self.form['csv'].value == "1":
            self.output_format = 'csv'
            
    def getHtml(self):
        '''Return entire Html Page, NOT including HTTP Header.
        Also calls self.process()
        '''
        
        html = self.getHtmlHeader()
        report_body = self.getHtmlContent() # can set debug_msg

        html += self.debug_msg
        html += report_body
        html += self.getHtmlFooter()
        return html

    def getCsv(self):
        self.process()
        return 'Empty Body'
    
    def getHttpHeader(self):
        cookie_header = self.cookie + '\n' if self.cookie else ''
        if self.output_format == 'csv':
            return 'Content-Type: application/csv\n' + \
                   'Content-Disposition: attachment; filename=%s.csv\n' \
                   % self.__class__.__name__
        else:
            return '%sContent-Type: text/html\n' % cookie_header
        
    def getHtmlHeader(self):
        dtd_tag     = '<!DOCTYPE html PUBLIC ' \
                      '"-//W3C//DTD XHTML 1.0 Strict//EN" ' \
                      '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'
        
        title_tag   = '<title>%s</title>\n' % self.title
        
        #meta_tag    = '<meta content="text/html; charset=iso-8859-1" ' \
        #              'http-equiv="Content-Type" />\n'
        meta_tag    = '<meta content="text/html; charset=UTF-8" '\
                      'http-equiv="Content-Type" />\n'
        
        # Auto Refresh:
        if self.auto_refresh:
            meta_tag += '<meta http-equiv="Refresh" content="%s"/>\n' \
                % self.auto_refresh

        style_files_tag=''
        if self.style_sheets:
            if isinstance(self.style_sheets, str):
                self.style_sheets = [self.style_sheets]
            for style_sheet in self.style_sheets:
                style_files_tag += '<link href="%s" rel="stylesheet" ' \
                    'type="text/css" />\n' % style_sheet
        
        jscript_src_tag = ''
        if self.javascript_src:
            if isinstance(self.javascript_src, str):
                self.javascript_src = [self.javascript_src]
            for s in self.javascript_src:
                jscript_src_tag += '<script type="text/javascript" ' \
                    'language="javascript" src="%s"></script>\n' % s

        jscript_tag = ''
        if self.javascript:
            #jscript_tag='<script language="JavaScript">\n%s\n</script>\n' \
            #             % self.javascript
            jscript_tag='<script type="text/javascript" charset="utf-8">\n' \
                         '%s\n</script>\n' % self.javascript
        style_tag = ''
        if self.style:
            style_tag = '<style>\n%s</style>\n' % self.style
            
        o = ''
        o += dtd_tag
        o += '<html>\n'
        o += '<head>\n%s%s%s%s%s%s</head>\n\n' % (#dtd_tag,
                                                 title_tag,
                                                 meta_tag, style_files_tag,
                                                 style_tag,
                                                 jscript_src_tag,
                                                 jscript_tag)
        o += '<body %s>\n' % self.body_attributes
        if self.include_form_tag:
            o += '<form action="%s" name="%s" method="POST">\n' % \
                (self.form_action, self.form_name)
        return o
    
    def getHtmlFooter(self):
        o = ''
        o += '\n'
        if self.include_form_tag:
            o += '</form>\n'
        o += '</body>\n'
        o += '</html>\n'
        return o

    def getHtmlContent(self):
        return 'Empty Body'


    def getPageWidget (self, num_pages, other=''):
        '''Return a page chooser widget of the form:
        Pages: <<  1 2 3 4 5 6 7 8 9 10 11 12 13 14  >>
        '''
        if other:
            other = '%s&' % other
    
        prev_arrow = '&lt;&lt;'
        next_arrow = '&gt;&gt;'

        current_page = self.page_num
        
        # prev_link:
        if current_page == 1:
            prev_link = prev_arrow
        else:
            href = '?%sstart=%i&page=prev' % (other, current_page)
            prev_link = "<a href='%s'>%s</a>" % (href, prev_arrow)

        # next_link
        if current_page == num_pages:
            next_link = next_arrow
        else:
            href = '?%sstart=%i&page=next' % (other, current_page)
            next_link = "<a href='%s'>%s</a>" % (href, next_arrow)

        # page_links
        page_links = ''
        for i in range(0, num_pages):
            page_num = i+1
            if page_num == current_page:
                link = "<big><b>%s</b></big>" % page_num
            else:
                href = "?%spage=%s" % (other, page_num)
                link = "<a href='%s'>%s</a>" % (href, page_num)
            page_links += '%s ' % link


        output = 'Pages: %s %s %s\n' % (prev_link, page_links, next_link)
        return output


    def getCsvButton(self):
        '''Return a 'Download CSV' button that can be used on the page
           Uses a hidden field called 'csv'
           Uses javascript to reset the value of that field.
        '''
        from html import input, script
        reset_js = 'function(){document.form1.csv.value=0}'
        return script('setInterval(%s,''500)') % reset_js + \
               input(name='csv', type='hidden', value='0') + \
               input(name='csv_button', value='Download CSV', type='button',
                     onClick='document.form1.csv.value=1; submit();')

    def go(self):
        self.process()
        print self.getHttpHeader()
        if self.output_format == 'csv':
            print self.getCsv()
        else:
            print self.getHtml()

if __name__ == '__main__':
    page = HtmlPage('Untitled')
    page.go()
        
