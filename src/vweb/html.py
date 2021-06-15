#  Html Utility Program
#
#   This program aims to provide a method call for each HTML tag name.
#   It provides a mechanism for Tag attributes.
#   It makes no attempt to validate tags and attributes.
#
#       These commands:
#            b('hi')
#            p(font('some text', color='green'))
#            a('Chapter 2', href='chapter2.html')
#   
#       Returns these string:
#            "<b>hi</b>
#            "<p><font color='red'>text</font></p>"
#            "<a href='chapter2.html'>Chapter 2</a>
#
#   Python keyword conflicts:
#       Use a trailing underscore: eq. p('text', class_='special')
#
#   Use of hyphens (-) in attribute names, not allowed in python:
#       Use understore (_): eq. div(p('text'), data_timestamp='2013-07-25')
#       produces: <div data-timestamp="2013-07-25"><p>text</p>\n</div>
#
#   Use htmltable.py for HTML table tags.

# Constants:

HTSPACE = '&nbsp;'
            
def htmlTag(tag, s, attrs):
    '''Generic html tag method.
       Trailing underscores removed from attribute names, to allow for
       use of python keywords, ie. class_, for_

       Newlines can be turned on or off with newline=True|False,
       default=True
    '''
    nl = '\n'
    if attrs:
        list = []
        for k, v in attrs.items():
            # control newlines
            if k == 'newline':
                #nl = '\n' if v else ''
                if v:
                    nl = '\n'
                else:
                    nl = ''
                continue
            list.append('%s="%s"' % (k.rstrip('_').replace('_', '-'), v))
        return "<%s %s>%s</%s>%s" % (tag, ' '.join(list), s, tag, nl)
    
    return "<%s>%s</%s>%s" % (tag, s, tag, nl)        

def htmlSingleTag(tag, attrs):
    '''Generic single html tag method.
       Trailing underscores removed from attribute names, to allow for use
          of keywords, ie. class_
    '''
    if attrs:
        list = []
        for k, v in attrs.items():
            list.append('%s="%s"' % (k.rstrip('_').replace('_', '-'), v))
        return "<%s %s />\n" % (tag, ' '.join(list))
    
    return "<%s />" % tag

def html_comment(str):
    '''Return string inside html comment'''
    return "<!-- %s -->" % str

# The tags:

def a        (s, **attrs): return htmlTag ('a'       , s, attrs)
def article  (s, **attrs): return htmlTag ('article' , s, attrs)
def b        (s, **attrs): return htmlTag ('b'       , s, attrs)
def big      (s, **attrs): return htmlTag ('big'     , s, attrs)
def body     (s, **attrs): return htmlTag ('body'    , s, attrs)
def button   (s, **attrs): return htmlTag ('button'    , s, attrs)
def center   (s, **attrs): return htmlTag ('center'  , s, attrs)
def div      (s, **attrs): return htmlTag ('div'     , s, attrs)
def dd       (s, **attrs): return htmlTag ('dd'      , s, attrs)
def dl       (s, **attrs): return htmlTag ('dl'      , s, attrs)
def dt       (s, **attrs): return htmlTag ('dt'      , s, attrs)
def figure   (s, **attrs): return htmlTag ('figure'  , s, attrs)
def figurecaption(s, **attrs): return htmlTag ('figurecaption'  , s, attrs)
def font     (s, **attrs): return htmlTag ('font'    , s, attrs)
def footer   (s, **attrs): return htmlTag ('footer'  , s, attrs)
def form     (s, **attrs): return htmlTag ('form'    , s, attrs)
def h1       (s, **attrs): return htmlTag ('h1'      , s, attrs)
def h2       (s, **attrs): return htmlTag ('h2'      , s, attrs)
def h3       (s, **attrs): return htmlTag ('h3'      , s, attrs)
def h4       (s, **attrs): return htmlTag ('h4'      , s, attrs)
def head     (s, **attrs): return htmlTag ('head'    , s, attrs)
def header   (s, **attrs): return htmlTag ('header'  , s, attrs)
def html     (s, **attrs): return htmlTag ('html'    , s, attrs)
def i        (s, **attrs): return htmlTag ('i   '    , s, attrs)
def label    (s, **attrs): return htmlTag ('label'   , s, attrs)
def li       (s, **attrs): return htmlTag ('li'      , s, attrs)
def nav      (s, **attrs): return htmlTag ('nav'     , s, attrs)
def nobr     (s, **attrs): return htmlTag ('nobr'    , s, attrs)
def option   (s, **attrs): return htmlTag ('option'  , s, attrs)
def p        (s, **attrs): return htmlTag ('p'       , s, attrs)
def pre      (s, **attrs): return htmlTag ('pre'     , s, attrs)
def script   (s, **attrs): return htmlTag ('script'  , s, attrs)
def section  (s, **attrs): return htmlTag ('section' , s, attrs)
def select   (s, **attrs): return htmlTag ('select'  , s, attrs)
def small    (s, **attrs): return htmlTag ('small'   , s, attrs)
def span     (s, **attrs): return htmlTag ('span'    , s, attrs)
def strong   (s, **attrs): return htmlTag ('strong'  , s, attrs)
def style    (s, **attrs): return htmlTag ('style'   , s, attrs)
def textarea (s, **attrs): return htmlTag ('textarea', s, attrs)
def title    (s, **attrs): return htmlTag ('title'   , s, attrs)
def ul       (s, **attrs): return htmlTag ('ul'      , s, attrs)

# The Single Tags:

def br    (**attrs): return htmlSingleTag ('br'   , attrs)
def embed (**attrs): return htmlSingleTag ('embed', attrs)
def hr    (**attrs): return htmlSingleTag ('hr'   , attrs)
def img   (**attrs): return htmlSingleTag ('img'  , attrs)
def input (**attrs): return htmlSingleTag ('input', attrs)
def meta  (**attrs): return htmlSingleTag ('meta' , attrs)

