#!/usr/bin/python
#-*- coding: utf-8 -*-

START_INDENT = 0
INDENTATION_INC = 2

DEBUG_UNICODE_ERROR = 0

class HtmlTableError (Exception): pass

class HtmlTable (object):
    '''Html Table Abstraction Layer

       Example:

       table = HtmlTable
    '''
    def __init__ (self, class_=None, id=None, border=0, cellspacing=0, 
                  cellpadding=0, width=0, start_indent=START_INDENT,
                  indentation_inc=INDENTATION_INC, blank_cell='&nbsp;',
                  cell_error_value=None):
        self.table = {}
        self.attrs = {}
        self.rownum = 0
        self.colnum = 0
        self.class_ = class_
        self.id = id
        self.border = border
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.width = width
        self.start_indent = start_indent
        self.indentation_inc = indentation_inc
        self.blank_cell = blank_cell
        self.cell_error_value = cell_error_value

        self.header_rows = {}
        self.footer_rows = {}
        
        self.row_id      = {}
        self.row_class   = {}
        self.row_bgcolor = {}
        self.row_valign  = {}

        self.col_class     = {}
        self.col_align     = {}
        self.col_valign    = {}
        self.col_start_tag = {}
        self.col_end_tag   = {}
        self.col_width     = {}
        
        self.cell_class    = {}
        self.cell_colspan  = {}
        self.cell_rowspan  = {}
        self.cell_align    = {}
        
    def addHeader(self, row_array):
        return self.addRow(row_array, header=1)
        
    def addFooter(self, row_array):
        return self.addRow(row_array, footer=1)

    def addRow(self, row_array, header=0, footer=0):
        row = self.rownum
        self.rownum +=1

        if header:
            self.header_rows[row] = 1
        elif footer:
            self.footer_rows[row] = 1
            
        col = 0
        for data in row_array:
            key = '%i:%i' % (row, col)
            self.table[key] = data
            col += 1
            self.colnum = max(col, self.colnum)

    # Row setters

    def setRowId (self, row, id):
        r = row-1
        self.row_id[r] = id
        
    def setRowClass (self, row, class_):
        r = row-1
        self.row_class[r] = class_

    def setRowBGColor (self, row, color):
        r = row-1
        self.row_bgcolor[r] = color
        
    def setRowVAlign (self, row, valign):
        r = row-1
        self.row_valign[r] = valign

    # Col Setters

    def setColClass  (self, col, class_):
        c = col-1
        self.col_class[c] = class_

    def setColAlign (self, col, align):
        c = col-1
        self.col_align[c] = align
        
    def setColVAlign (self, col, valign):
        c = col-1
        self.col_valign[c] = valign
        
    def setColFormat (self, col, start_tag, end_tag):
        c = col-1
        self.col_start_tag[c] = start_tag
        self.col_end_tag[c]   = end_tag

    def setColWidth(self, col, width):
        c = col-1
        self.col_width[c] = width
    
    # Cell Setters

    def setCellClass(self, row, col, class_):
        r = row-1
        c = col-1
        key = '%i:%i' % (r,c)
        self.cell_class[key] = class_

    def setCellColSpan(self, row, col, colspan):
        r = row-1
        c = col-1
        key = '%i:%i' % (r,c)
        self.cell_colspan[key] = colspan

    def setCellRowSpan(self, row, col, rowspan):
        r = row-1
        c = col-1
        key = '%i:%i' % (r,c)
        self.cell_rowspan[key] = rowspan

    def setCellAlign(self, row, col, align):
        r = row-1
        c = col-1
        key = '%i:%i' % (r,c)
        self.cell_align[key] = align

    def validateTable(self):
        # validate header rows are contiguous
        if self.header_rows:
            for row in range(0, self.header_rows.keys()[-1]):
                if not self.header_rows.has_key(row):
                    raise HtmlTableError(
                        'Html Table Header tags (TH) must be contiguous, and '
                        'begin at Row 1.  Header Rows: %s' 
                        % [x+1 for x in self.header_rows.keys()])
        # validate footer rows are contiguous and at the end
        if self.footer_rows:
            for row in range(self.footer_rows.keys()[0], self.rownum):
                if not self.footer_rows.has_key(row):
                    raise HtmlTableError(
                        'Html Table Footer tags must be continguous, and'
                        'at the end of table.  Footer rows: %s'
                        % [x+1 for x in self.footer_rows.keys()])

    def getTable(self):
        self.validateTable()

        if self.footer_rows:
            start_footer_row = self.rownum - len(self.footer_rows) + 1
        
        attrs = ['cellpadding="%i"' % self.cellpadding, 
                 'cellspacing="%i"' % self.cellspacing]
        if self.class_:
            attrs.append('class="%s"' % self.class_)
        if self.id:
            attrs.append('id="%s"' % self.id)
        if self.width:
            attrs.append('width="%s"' % self.width)
        if self.border:
            attrs.append('border="%s"' % self.border)
        for k, v in self.attrs.items():
            attrs.append('%s="%s"' % (k, v))
        
        o = '%s<table %s>\n' % (' '*self.start_indent, ' '.join(attrs))

        running_rowspans = []
        for row in xrange(self.rownum):

            # decrement rowspans
            running_rowspans = [rs - 1 for rs in running_rowspans if rs > 0]
            
            # THEAD tag:
            if row == 0:
                if self.header_rows:
                    o += '%s<thead>\n' % self.indent(1)
                else:
                    o += '%s<tbody>\n' % self.indent(1)
            elif self.row_bgcolor.has_key(row):
                row_color = ' style="background-color: %s;"' % \
                            self.row_bgcolor[row]

            # TR Tag:
            elements = ''
            if self.row_class.has_key(row):
                elements += ' class="%s"' % self.row_class[row]
            if self.row_bgcolor.has_key(row):
                elements += ' bgcolor="%s"' % self.row_bgcolor[row]
            if self.row_valign.has_key(row):
                elements += ' valign="%s"' % self.row_valign[row]
            o += '%s<tr%s>\n' % (self.indent(2), elements)
            
            # TD Tags:
            running_colspan = 0
            for col in xrange(self.colnum - len(running_rowspans)):

                if running_colspan:
                    running_colspan -= 1
                    continue

                key = '%s:%s' % (row, col)

                elements = ''
                classes = []
                if self.cell_class.has_key(key):
                    classes.append(self.cell_class[key])
                if self.cell_colspan.has_key(key):
                    elements += ' colspan="%s"' % self.cell_colspan[key]
                    running_colspan = self.cell_colspan[key]-1
                if self.cell_rowspan.has_key(key):
                    elements += ' rowspan="%s"' % self.cell_rowspan[key]
                    running_rowspans.append(self.cell_rowspan[key] - 1)
                if self.cell_align.has_key(key):
                    elements += ' align="%s"' % self.cell_align[key]
                if self.row_id.has_key(row):
                    elements += ' id="%s"' % self.row_id[row]
                if self.col_class.has_key(col):
                    classes.append(self.col_class[col])
                if self.col_align.has_key(col) and \
                        not self.cell_align.has_key(key):
                    elements += ' align="%s"' % self.col_align[col]
                if self.col_valign.has_key(col):
                    elements += ' valign="%s"' % self.col_valign[col]
                if self.col_width.has_key(col):
                    elements += ' width="%s"' % self.col_width[col]
                if classes:
                    elements += ' class="%s"' % ' '.join(classes)

                ## td/th 
                if row in self.header_rows or row in self.footer_rows: 
                    coltag = 'th'
                else:                             
                    coltag = 'td'
                o += '%s<%s%s>' % (self.indent(3), coltag, elements)

                if self.col_start_tag.has_key(col):
                    o += self.col_start_tag[col]

                try:
                    value = self.table.get(key, '')
                    if isinstance(value, (int, long, list, dict)):
                        value = unicode(value)
                    o += value
                    #o += unicode(self.table[key]).encode('utf-8')
                except Exception, e:
                    if DEBUG_UNICODE_ERROR:
                        from datetime import datetime
                        open('/var/log/fwk/htmltable_unicode_error',
                             'a').write('%s: Value = "%s"\n' % (datetime.now(),
                                                            value))
                    if self.cell_error_value is not None:
                        o += self.cell_error_value
                    else:
                        o += "%s: %s" % (e.__class__.__name__, e)
                    #o += self.blank_cell
                    
                if self.col_end_tag.has_key(col):
                    o += self.col_end_tag[col]

                o += '</%s>\n' % coltag
            o += '%s</tr>\n' % self.indent(2)

            # close THEAD tag, start TBODY tag
            if self.header_rows.has_key(row) and \
                    not self.header_rows.has_key(row+1):
                o += '%s</thead>\n' % self.indent(1)
                o += '%s<tbody>\n' % self.indent(1)
                
            # close TBODY tag, start TFOOT tag
            if self.footer_rows and row == start_footer_row-2:
                o += '%s</tbody>\n' % self.indent(1)
                o += '%s<tfoot>\n' % self.indent(1)

        if self.footer_rows:
            o += '%s</tfoot>\n' % self.indent(1)
        else:
            o += '%s</tbody>\n' % self.indent(1)
        o += '%s</table>\n' % (' '*self.start_indent)

        return o

    def indent(self, n):
        return ' '.ljust(self.start_indent + (n * self.indentation_inc))


def test():
    table = HtmlTable()
    table.addHeader(['header'])
    table.addRow(['row', 'row2', 'row3', 'row4'])
    table.addRow(['a1'])
    table.addRow(['a2', 'a3'])
    table.addRow(['a4', 'a5', 'a6', 'a7'])
    table.addRow(['a8', 'a9'])
    table.addFooter(['foot', 'foot2'])
    table.setCellColSpan(1, 1, 4)
    table.setCellRowSpan(2, 1, 2)
    table.setCellRowSpan(2, 2, 3)
    table.setCellRowSpan(2, 3, 4)
    table.setCellColSpan(6, 1, 2)
    table.setCellColSpan(6, 3, 2)
    print table.getTable()

if __name__ == '__main__':
    test()
