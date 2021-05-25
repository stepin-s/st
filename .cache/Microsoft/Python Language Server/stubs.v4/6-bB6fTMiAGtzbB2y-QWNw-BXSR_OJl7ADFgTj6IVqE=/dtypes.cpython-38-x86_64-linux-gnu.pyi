import builtins as _mod_builtins
import enum as _mod_enum

Enum = _mod_enum.Enum
class FreqGroup(_mod_builtins.object):
    FR_ANN = 1000
    FR_BUS = 5000
    FR_DAY = 6000
    FR_HR = 7000
    FR_MIN = 8000
    FR_MS = 10000
    FR_MTH = 3000
    FR_NS = 12000
    FR_QTR = 2000
    FR_SEC = 9000
    FR_UND = -10000
    FR_US = 11000
    FR_WK = 4000
    __class__ = FreqGroup
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.dtypes'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def get_freq_group(self, code):
        return 'int'
    

class PeriodDtypeBase(_mod_builtins.object):
    '\n    Similar to an actual dtype, this contains all of the information\n    describing a PeriodDtype in an integer code.\n    '
    __class__ = PeriodDtypeBase
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        '\n    Similar to an actual dtype, this contains all of the information\n    describing a PeriodDtype in an integer code.\n    '
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
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _dtype_code(self):
        pass
    
    @property
    def date_offset(self):
        '\n        Corresponding DateOffset object.\n\n        This mapping is mainly for backward-compatibility.\n        '
        pass
    
    @property
    def freq_group(self):
        pass
    
    @classmethod
    def from_date_offset(cls):
        pass
    

class Resolution(_mod_enum.Enum):
    'An enumeration.'
    RESO_DAY = Resolution()
    RESO_HR = Resolution()
    RESO_MIN = Resolution()
    RESO_MS = Resolution()
    RESO_MTH = Resolution()
    RESO_NS = Resolution()
    RESO_QTR = Resolution()
    RESO_SEC = Resolution()
    RESO_US = Resolution()
    RESO_YR = Resolution()
    __class__ = Resolution
    __members__ = _mod_builtins.mappingproxy()
    __module__ = 'pandas._libs.tslibs.dtypes'

__builtins__ = {}
__doc__ = None
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/dtypes.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.dtypes'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
_attrname_to_abbrevs = _mod_builtins.dict()
_period_code_map = _mod_builtins.dict()
_reverse_period_code_map = _mod_builtins.dict()
