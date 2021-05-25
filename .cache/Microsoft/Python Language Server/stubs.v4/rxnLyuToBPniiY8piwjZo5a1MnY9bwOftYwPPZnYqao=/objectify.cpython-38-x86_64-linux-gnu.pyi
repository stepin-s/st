import builtins as _mod_builtins
import lxml.etree as _mod_lxml_etree

class BoolElement(IntElement):
    "Boolean type base on string values: 'true' or 'false'.\n\n    Note that this inherits from IntElement to mimic the behaviour of\n    Python's bool type.\n    "
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = BoolElement
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _init(self):
        pass
    
    @property
    def pyval(self):
        pass
    

def DataElement(_value, attrib, nsmap, **_attributes):
    "DataElement(_value, attrib=None, nsmap=None, _pytype=None, _xsi=None, **_attributes)\n\n    Create a new element from a Python value and XML attributes taken from\n    keyword arguments or a dictionary passed as second argument.\n\n    Automatically adds a 'pytype' attribute for the Python type of the value,\n    if the type can be identified.  If '_pytype' or '_xsi' are among the\n    keyword arguments, they will be used instead.\n\n    If the _value argument is an ObjectifiedDataElement instance, its py:pytype,\n    xsi:type and other attributes and nsmap are reused unless they are redefined\n    in attrib and/or keyword arguments.\n    "
    pass

def E():
    'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
    pass

def Element(_tag, attrib, nsmap, **_attributes):
    'Element(_tag, attrib=None, nsmap=None, _pytype=None, **_attributes)\n\n    Objectify specific version of the lxml.etree Element() factory that\n    always creates a structural (tree) element.\n\n    NOTE: requires parser based element class lookup activated in lxml.etree!\n    '
    pass

class ElementMaker(_mod_builtins.object):
    'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = ElementMaker
    def __getattr__(self):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, namespace=None, nsmap=None, annotate=True, makeelement=None):
        'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class FloatElement(NumberElement):
    __class__ = FloatElement
    __dict__ = {}
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _init(self):
        pass
    

class IntElement(NumberElement):
    __class__ = IntElement
    __dict__ = {}
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _init(self):
        pass
    

class LongElement(NumberElement):
    __class__ = LongElement
    __dict__ = {}
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _init(self):
        pass
    

class NoneElement(ObjectifiedDataElement):
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = NoneElement
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def pyval(self):
        pass
    

class NumberElement(ObjectifiedDataElement):
    def __abs__(self):
        'abs(self)'
        return NumberElement()
    
    def __add__(self, value):
        'Return self+value.'
        return NumberElement()
    
    def __and__(self, value):
        'Return self&value.'
        return NumberElement()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = NumberElement
    def __complex__(self):
        pass
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __invert__(self):
        '~self'
        return NumberElement()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lshift__(self, value):
        'Return self<<value.'
        return NumberElement()
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mod__(self, value):
        'Return self%value.'
        return NumberElement()
    
    def __mul__(self, value):
        'Return self*value.'
        return NumberElement()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return NumberElement()
    
    def __or__(self, value):
        'Return self|value.'
        return NumberElement()
    
    def __pos__(self):
        '+self'
        return NumberElement()
    
    def __pow__(self, value, mod):
        'Return pow(self, value, mod).'
        return NumberElement()
    
    def __radd__(self, value):
        'Return value+self.'
        return NumberElement()
    
    def __rand__(self, value):
        'Return value&self.'
        return NumberElement()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rlshift__(self, value):
        'Return value<<self.'
        return NumberElement()
    
    def __rmod__(self, value):
        'Return value%self.'
        return NumberElement()
    
    def __rmul__(self, value):
        'Return value*self.'
        return NumberElement()
    
    def __ror__(self, value):
        'Return value|self.'
        return NumberElement()
    
    def __rpow__(self, value, mod):
        'Return pow(value, self, mod).'
        return NumberElement()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return NumberElement()
    
    def __rshift__(self, value):
        'Return self>>value.'
        return NumberElement()
    
    def __rsub__(self, value):
        'Return value-self.'
        return NumberElement()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return NumberElement()
    
    def __rxor__(self, value):
        'Return value^self.'
        return NumberElement()
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return NumberElement()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def __xor__(self, value):
        'Return self^value.'
        return NumberElement()
    
    def _setValueParser(self, function):
        'Set the function that parses the Python value from a string.\n\n        Do not use this unless you know what you are doing.\n        '
        pass
    
    @property
    def pyval(self):
        pass
    

class ObjectPath(_mod_builtins.object):
    "ObjectPath(path)\n    Immutable object that represents a compiled object path.\n\n    Example for a path: 'root.child[1].{other}child[25]'\n    "
    def __call__(self):
        'Follow the attribute path in the object structure and return the\n        target attribute value.\n\n        If it it not found, either returns a default value (if one was passed\n        as second argument) or raises AttributeError.\n        '
        pass
    
    __class__ = ObjectPath
    def __init__(self, path):
        "ObjectPath(path)\n    Immutable object that represents a compiled object path.\n\n    Example for a path: 'root.child[1].{other}child[25]'\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addattr(self, root, value):
        'addattr(self, root, value)\n\n        Append a value to the target element in a subtree.\n\n        If any of the children on the path does not exist, it is created.\n        '
        pass
    
    @property
    def find(self):
        pass
    
    def hasattr(self, root):
        'hasattr(self, root)'
        pass
    
    def setattr(self, root, value):
        'setattr(self, root, value)\n\n        Set the value of the target element in a subtree.\n\n        If any of the children on the path does not exist, it is created.\n        '
        pass
    

class ObjectifiedDataElement(ObjectifiedElement):
    "This is the base class for all data type Elements.  Subclasses should\n    override the 'pyval' property and possibly the __str__ method.\n    "
    __class__ = ObjectifiedDataElement
    __dict__ = {}
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _setText(self, s):
        "For use in subclasses only. Don't use unless you know what you are\n        doing.\n        "
        pass
    
    @property
    def pyval(self):
        pass
    

class ObjectifiedElement(_mod_lxml_etree.ElementBase):
    'Main XML Element class.\n\n    Element children are accessed as object attributes.  Multiple children\n    with the same name are available through a list index.  Example::\n\n       >>> root = XML("<root><c1><c2>0</c2><c2>1</c2></c1></root>")\n       >>> second_c2 = root.c1.c2[1]\n       >>> print(second_c2.text)\n       1\n\n    Note that you cannot (and must not) instantiate this class or its\n    subclasses.\n    '
    __class__ = ObjectifiedElement
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    __dict__ = {}
    def __getattr__(self):
        'Return the (first) child with the given tag name.  If no namespace\n        is provided, the child will be looked up in the same one as self.\n        '
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, index):
        'Return a sibling, counting from the first child of the parent.  The\n        method behaves like both a dict and a sequence.\n\n        * If argument is an integer, returns the sibling at that position.\n\n        * If argument is a string, does the same as getattr().  This can be\n          used to provide namespaces for element lookup, or to look up\n          children with special names (``text`` etc.).\n\n        * If argument is a slice object, returns the matching slice.\n        '
        pass
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Iterate over self and all siblings with the same tag.\n        '
        return ObjectifiedElement()
    
    def __len__(self):
        'Count self and siblings with the same tag.\n        '
        return 0
    
    def __reduce__(self):
        return ''; return ()
    
    def __setattr__(self):
        'Set the value of the (first) child with the given tag name.  If no\n        namespace is provided, the child will be looked up in the same one as\n        self.\n        '
        return None
    
    def __setitem__(self, index, value):
        'Set the value of a sibling, counting from the first child of the\n        parent.  Implements key assignment, item assignment and slice\n        assignment.\n\n        * If argument is an integer, sets the sibling at that position.\n\n        * If argument is a string, does the same as setattr().  This is used\n          to provide namespaces for element lookup.\n\n        * If argument is a sequence (list, tuple, etc.), assign the contained\n          items to the siblings.\n        '
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addattr(self, tag, value):
        'addattr(self, tag, value)\n\n        Add a child value to the element.\n\n        As opposed to append(), it sets a data value, not an element.\n        '
        pass
    
    def countchildren(self):
        'countchildren(self)\n\n        Return the number of children of this element, regardless of their\n        name.\n        '
        pass
    
    def descendantpaths(self, prefix):
        'descendantpaths(self, prefix=None)\n\n        Returns a list of object path expressions for all descendants.\n        '
        pass
    
    def getchildren(self):
        'getchildren(self)\n\n        Returns a sequence of all direct children.  The elements are\n        returned in document order.\n        '
        pass
    
    @property
    def text(self):
        pass
    

class ObjectifyElementClassLookup(_mod_lxml_etree.ElementClassLookup):
    'ObjectifyElementClassLookup(self, tree_class=None, empty_data_class=None)\n    Element class lookup method that uses the objectify classes.\n    '
    __class__ = ObjectifyElementClassLookup
    def __init__(self, tree_class=None, empty_data_class=None):
        "Lookup mechanism for objectify.\n\n        The default Element classes can be replaced by passing subclasses of\n        ObjectifiedElement and ObjectifiedDataElement as keyword arguments.\n        'tree_class' defines inner tree classes (defaults to\n        ObjectifiedElement), 'empty_data_class' defines the default class for\n        empty data elements (defaults to StringElement).\n        "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

PYTYPE_ATTRIBUTE = '{http://codespeak.net/lxml/objectify/pytype}pytype'
class PyType(_mod_builtins.object):
    'PyType(self, name, type_check, type_class, stringify=None)\n    User defined type.\n\n    Named type that contains a type check function, a type class that\n    inherits from ObjectifiedDataElement and an optional "stringification"\n    function.  The type check must take a string as argument and raise\n    ValueError or TypeError if it cannot handle the string value.  It may be\n    None in which case it is not considered for type guessing.  For registered\n    named types, the \'stringify\' function (or unicode() if None) is used to\n    convert a Python object with type name \'name\' to the string representation\n    stored in the XML tree.\n\n    Example::\n\n        PyType(\'int\', int, MyIntClass).register()\n\n    Note that the order in which types are registered matters.  The first\n    matching type will be used.\n    '
    __class__ = PyType
    def __init__(self, name, type_check, type_class, stringify=None):
        'PyType(self, name, type_check, type_class, stringify=None)\n    User defined type.\n\n    Named type that contains a type check function, a type class that\n    inherits from ObjectifiedDataElement and an optional "stringification"\n    function.  The type check must take a string as argument and raise\n    ValueError or TypeError if it cannot handle the string value.  It may be\n    None in which case it is not considered for type guessing.  For registered\n    named types, the \'stringify\' function (or unicode() if None) is used to\n    convert a Python object with type name \'name\' to the string representation\n    stored in the XML tree.\n\n    Example::\n\n        PyType(\'int\', int, MyIntClass).register()\n\n    Note that the order in which types are registered matters.  The first\n    matching type will be used.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def name(self):
        pass
    
    def register(self, before, after):
        "register(self, before=None, after=None)\n\n        Register the type.\n\n        The additional keyword arguments 'before' and 'after' accept a\n        sequence of type names that must appear before/after the new type in\n        the type list.  If any of them is not currently known, it is simply\n        ignored.  Raises ValueError if the dependencies cannot be fulfilled.\n        "
        pass
    
    @property
    def stringify(self):
        pass
    
    @property
    def type_check(self):
        pass
    
    def unregister(self):
        'unregister(self)'
        pass
    
    @property
    def xmlSchemaTypes(self):
        'The list of XML Schema datatypes this Python type maps to.\n\n        Note that this must be set before registering the type!\n        '
        pass
    

class StringElement(ObjectifiedDataElement):
    "String data class.\n\n    Note that this class does *not* support the sequence protocol of strings:\n    len(), iter(), str_attr[0], str_attr[0:1], etc. are *not* supported.\n    Instead, use the .text attribute to get a 'real' string.\n    "
    def __add__(self, value):
        'Return self+value.'
        return StringElement()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = StringElement
    def __complex__(self):
        pass
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mod__(self, value):
        'Return self%value.'
        return StringElement()
    
    def __mul__(self, value):
        'Return self*value.'
        return StringElement()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return StringElement()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmod__(self, value):
        'Return value%self.'
        return StringElement()
    
    def __rmul__(self, value):
        'Return value*self.'
        return StringElement()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def pyval(self):
        pass
    
    def strlen(self):
        pass
    

def SubElement(_parent, _tag, attrib, nsmap, **_extra):
    'SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra)\n\n    Subelement factory.  This function creates an element instance, and\n    appends it to an existing element.\n    '
    pass

def XML(xml, parser):
    'XML(xml, parser=None, base_url=None)\n\n    Objectify specific version of the lxml.etree XML() literal factory\n    that uses the objectify parser.\n\n    You can pass a different parser as second argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    pass

__all__ = _mod_builtins.list()
__builtins__ = {}
def __checkBool(s):
    pass

__doc__ = '\nThe ``lxml.objectify`` module implements a Python object API for XML.\nIt is based on `lxml.etree`.\n'
__file__ = '/usr/lib/python3/dist-packages/lxml/objectify.cpython-38-x86_64-linux-gnu.so'
def __lower_bool(b):
    pass

__name__ = 'lxml.objectify'
__package__ = 'lxml'
def __parseBool(s):
    pass

__test__ = _mod_builtins.dict()
def __unpickleElementTree(data):
    pass

__version__ = '4.5.0'
def annotate(element_or_tree):
    "annotate(element_or_tree, ignore_old=True, ignore_xsi=False, empty_pytype=None, empty_type=None, annotate_xsi=0, annotate_pytype=1)\n\n    Recursively annotates the elements of an XML tree with 'xsi:type'\n    and/or 'py:pytype' attributes.\n\n    If the 'ignore_old' keyword argument is True (the default), current\n    'py:pytype' attributes will be ignored for the type annotation. Set to False\n    if you want reuse existing 'py:pytype' information (iff appropriate for the\n    element text value).\n\n    If the 'ignore_xsi' keyword argument is False (the default), existing\n    'xsi:type' attributes will be used for the type annotation, if they fit the\n    element text values. \n    \n    Note that the mapping from Python types to XSI types is usually ambiguous.\n    Currently, only the first XSI type name in the corresponding PyType\n    definition will be used for annotation.  Thus, you should consider naming\n    the widest type first if you define additional types.\n\n    The default 'py:pytype' annotation of empty elements can be set with the\n    ``empty_pytype`` keyword argument. Pass 'str', for example, to make\n    string values the default.\n\n    The default 'xsi:type' annotation of empty elements can be set with the\n    ``empty_type`` keyword argument.  The default is not to annotate empty\n    elements.  Pass 'string', for example, to make string values the default.\n\n    The keyword arguments 'annotate_xsi' (default: 0) and 'annotate_pytype'\n    (default: 1) control which kind(s) of annotation to use. \n    "
    pass

def deannotate(element_or_tree):
    "deannotate(element_or_tree, pytype=True, xsi=True, xsi_nil=False, cleanup_namespaces=False)\n\n    Recursively de-annotate the elements of an XML tree by removing 'py:pytype'\n    and/or 'xsi:type' attributes and/or 'xsi:nil' attributes.\n\n    If the 'pytype' keyword argument is True (the default), 'py:pytype'\n    attributes will be removed. If the 'xsi' keyword argument is True (the \n    default), 'xsi:type' attributes will be removed.\n    If the 'xsi_nil' keyword argument is True (default: False), 'xsi:nil'\n    attributes will be removed.\n\n    Note that this does not touch the namespace declarations by\n    default.  If you want to remove unused namespace declarations from\n    the tree, pass the option ``cleanup_namespaces=True``.\n    "
    pass

def dump(element):
    'dump(_Element element not None)\n\n    Return a recursively generated string representation of an element.\n    '
    pass

def enable_recursive_str(on):
    'enable_recursive_str(on=True)\n\n    Enable a recursively generated tree representation for str(element),\n    based on objectify.dump(element).\n    '
    pass

def fromstring(xml, parser):
    'fromstring(xml, parser=None, base_url=None)\n\n    Objectify specific version of the lxml.etree fromstring() function\n    that uses the objectify parser.\n\n    You can pass a different parser as second argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    pass

def getRegisteredTypes():
    'getRegisteredTypes()\n\n    Returns a list of the currently registered PyType objects.\n\n    To add a new type, retrieve this list and call unregister() for all\n    entries.  Then add the new type at a suitable position (possibly replacing\n    an existing one) and call register() for all entries.\n\n    This is necessary if the new type interferes with the type check functions\n    of existing ones (normally only int/float/bool) and must the tried before\n    other types.  To add a type that is not yet parsable by the current type\n    check functions, you can simply register() it, which will append it to the\n    end of the type list.\n    '
    pass

def makeparser(**kw):
    'makeparser(remove_blank_text=True, **kw)\n\n    Create a new XML parser for objectify trees.\n\n    You can pass all keyword arguments that are supported by\n    ``etree.XMLParser()``.  Note that this parser defaults to removing\n    blank text.  You can disable this by passing the\n    ``remove_blank_text`` boolean keyword option yourself.\n    '
    pass

def parse(f, parser):
    'parse(f, parser=None, base_url=None)\n\n    Parse a file or file-like object with the objectify parser.\n\n    You can pass a different parser as second argument.\n\n    The ``base_url`` keyword allows setting a URL for the document\n    when parsing from a file-like object.  This is needed when looking\n    up external entities (DTD, XInclude, ...) with relative paths.\n    '
    pass

def pyannotate(element_or_tree):
    "pyannotate(element_or_tree, ignore_old=False, ignore_xsi=False, empty_pytype=None)\n\n    Recursively annotates the elements of an XML tree with 'pytype'\n    attributes.\n\n    If the 'ignore_old' keyword argument is True (the default), current 'pytype'\n    attributes will be ignored and replaced.  Otherwise, they will be checked\n    and only replaced if they no longer fit the current text value.\n\n    Setting the keyword argument ``ignore_xsi`` to True makes the function\n    additionally ignore existing ``xsi:type`` annotations.  The default is to\n    use them as a type hint.\n\n    The default annotation of empty elements can be set with the\n    ``empty_pytype`` keyword argument.  The default is not to annotate empty\n    elements.  Pass 'str', for example, to make string values the default.\n    "
    pass

def pytypename(obj):
    'pytypename(obj)\n\n    Find the name of the corresponding PyType for a Python object.\n    '
    pass

def set_default_parser(new_parser):
    "set_default_parser(new_parser = None)\n\n    Replace the default parser used by objectify's Element() and\n    fromstring() functions.\n\n    The new parser must be an etree.XMLParser.\n\n    Call without arguments to reset to the original parser.\n    "
    pass

def set_pytype_attribute_tag(attribute_tag):
    'set_pytype_attribute_tag(attribute_tag=None)\n    Change name and namespace of the XML attribute that holds Python type\n    information.\n\n    Do not use this unless you know what you are doing.\n\n    Reset by calling without argument.\n\n    Default: "{http://codespeak.net/lxml/objectify/pytype}pytype"\n    '
    pass

def xsiannotate(element_or_tree):
    "xsiannotate(element_or_tree, ignore_old=False, ignore_pytype=False, empty_type=None)\n\n    Recursively annotates the elements of an XML tree with 'xsi:type'\n    attributes.\n\n    If the 'ignore_old' keyword argument is True (the default), current\n    'xsi:type' attributes will be ignored and replaced.  Otherwise, they will be\n    checked and only replaced if they no longer fit the current text value.\n\n    Note that the mapping from Python types to XSI types is usually ambiguous.\n    Currently, only the first XSI type name in the corresponding PyType\n    definition will be used for annotation.  Thus, you should consider naming\n    the widest type first if you define additional types.\n\n    Setting the keyword argument ``ignore_pytype`` to True makes the function\n    additionally ignore existing ``pytype`` annotations.  The default is to\n    use them as a type hint.\n\n    The default annotation of empty elements can be set with the\n    ``empty_type`` keyword argument.  The default is not to annotate empty\n    elements.  Pass 'string', for example, to make string values the default.\n    "
    pass

