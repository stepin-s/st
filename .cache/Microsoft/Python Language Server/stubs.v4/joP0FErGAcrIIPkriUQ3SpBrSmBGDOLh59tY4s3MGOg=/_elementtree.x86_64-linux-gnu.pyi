def Comment():
    pass

def Element():
    pass

class ElementTree:
    __class__ = ElementTree
    __dict__ = {}
    def __init__(self, element, file):
        pass
    
    __module__ = '__builtin__'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _setroot(self, element):
        pass
    
    def find(self, path, namespaces):
        pass
    
    def findall(self, path, namespaces):
        pass
    
    def findtext(self, path, default, namespaces):
        pass
    
    def getiterator(self, tag):
        pass
    
    def getroot(self):
        pass
    
    def iter(self, tag):
        pass
    
    def iterfind(self, path, namespaces):
        pass
    
    def parse(self, source, parser):
        pass
    
    def write(self, file_or_filename, encoding, xml_declaration, default_namespace, method):
        pass
    
    def write_c14n(self, file):
        pass
    

def PI():
    pass

class ParseError(SyntaxError):
    __class__ = ParseError
    __dict__ = {}
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    __module__ = 'cElementTree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def ProcessingInstruction():
    pass

class QName(object):
    __class__ = QName
    def __cmp__(self, other):
        pass
    
    __dict__ = {}
    def __hash__(self):
        return 0
    
    def __init__(self, text_or_uri, tag):
        pass
    
    __module__ = 'xml.etree.ElementTree'
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def SubElement():
    pass

def TreeBuilder():
    pass

VERSION = '1.0.6'
def XML(text):
    pass

def XMLID(text):
    pass

def XMLParser():
    pass

def XMLTreeBuilder():
    pass

__doc__ = None
__file__ = '/usr/lib/python2.7/lib-dynload/_elementtree.x86_64-linux-gnu.so'
__name__ = '_elementtree'
__package__ = None
__version__ = '1.0.6'
def dump(elem):
    pass

def fromstring(text):
    pass

def fromstringlist(sequence, parser):
    pass

def iselement(element):
    pass

class iterparse(object):
    __class__ = iterparse
    __dict__ = {}
    def __init__(self, file, events):
        pass
    
    def __iter__(self):
        return iterparse()
    
    __module__ = '__builtin__'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def next(self):
        pass
    
    root = None

def parse(source, parser):
    pass

def register_namespace(prefix, uri):
    pass

def tostring(element, encoding, method):
    pass

def tostringlist(element, encoding, method):
    pass

