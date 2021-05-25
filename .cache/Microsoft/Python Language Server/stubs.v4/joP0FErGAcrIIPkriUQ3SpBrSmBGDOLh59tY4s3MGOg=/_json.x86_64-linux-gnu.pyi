import __builtin__ as _mod___builtin__

Encoder = _mod___builtin__.type
Scanner = _mod___builtin__.type
__doc__ = 'json speedups\n'
__file__ = '/usr/lib/python2.7/lib-dynload/_json.x86_64-linux-gnu.so'
__name__ = '_json'
__package__ = None
def encode_basestring_ascii(basestring):
    'encode_basestring_ascii(basestring) -> str\n\nReturn an ASCII-only JSON representation of a Python string'
    return ''

make_encoder = Encoder
make_scanner = Scanner
def scanstring(basestring, end, encoding, strict=True):
    'scanstring(basestring, end, encoding, strict=True) -> (str, end)\n\nScan the string s for a JSON string. End is the index of the\ncharacter in s after the quote that started the JSON string.\nUnescapes all valid JSON string escape sequences and raises ValueError\non attempt to decode an invalid string. If strict is False then literal\ncontrol characters are allowed in the string.\n\nReturns a tuple of the decoded string and the index of the character in s\nafter the end quote.'
    return tuple()

