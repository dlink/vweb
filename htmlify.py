from html import *
from htmltable import HtmlTable

def htmlify(data, type='table'):
    if isinstance(data, list):
        table = HtmlTable(cellpadding=2)
        for row in data:
            if isinstance(row, list):
                for i, col in enumerate(row):
                    if isinstance(col, list):
                        row[i] = ', '.join(str(c) for c in col)
                table.addRow(row)
            else:
                table.addRow([str(row)])
        return table.getTable()
    if isinstance(data, dict):
        if type == 'table':
            return dict2table(data)
        return dict2dl(data)
    if isinstance(data, (str, unicode)) and '\033[' in data:
        from utils import system_call
        return system_call("echo '%s' | aha" % data, 1)

    return p(data)


def dict2table(data):
    table = HtmlTable()
    for k, v in sorted(data.items()):
        table.addRow([k or "&nbsp;", str(v)])
    return table.getTable()


def dict2dl(data):
    html = ''
    for k, v in sorted(data.items()):
        html += '  <dt>%s</dt>\n' % k
        html += '  <dd>%s</dd>\n' % v
    return '<dl>\n%s</dl>' % html if html else ''
