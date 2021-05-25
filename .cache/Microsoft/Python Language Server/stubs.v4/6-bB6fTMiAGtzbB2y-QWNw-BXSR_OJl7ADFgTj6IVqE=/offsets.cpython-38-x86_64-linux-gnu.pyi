import builtins as _mod_builtins
import dateutil.relativedelta as _mod_dateutil_relativedelta
import pandas._libs.properties as _mod_pandas__libs_properties
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps
import re as _mod_re

def Any(self, *args, **kwds):
    'Internal indicator of special typing constructs.\n    See _doc instance attribute for specific docs.\n    '
    pass

class ApplyTypeError(_mod_builtins.TypeError):
    __class__ = ApplyTypeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.offsets'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

BDay = BusinessDay
BMonthBegin = BusinessMonthBegin
BMonthEnd = BusinessMonthEnd
class BQuarterBegin(QuarterOffset):
    "\n    DateOffset increments between the first business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BQuarterBegin(2)\n    Timestamp('2020-09-01 05:01:15')\n    >>> ts + BQuarterBegin(startingMonth=2)\n    Timestamp('2020-08-03 05:01:15')\n    >>> ts + BQuarterBegin(-1)\n    Timestamp('2020-03-02 05:01:15')\n    "
    __class__ = BQuarterBegin
    def __init__(self, *args, **kwargs):
        "\n    DateOffset increments between the first business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BQuarterBegin(2)\n    Timestamp('2020-09-01 05:01:15')\n    >>> ts + BQuarterBegin(startingMonth=2)\n    Timestamp('2020-08-03 05:01:15')\n    >>> ts + BQuarterBegin(-1)\n    Timestamp('2020-03-02 05:01:15')\n    "
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
    
    _day_opt = 'business_start'
    _default_starting_month = 3
    @classmethod
    def _from_name(cls):
        pass
    
    _from_name_starting_month = 1
    _output_name = 'BusinessQuarterBegin'
    _prefix = 'BQS'

class BQuarterEnd(QuarterOffset):
    "\n    DateOffset increments between the last business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterEnd()\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BQuarterEnd(2)\n    Timestamp('2020-09-30 05:01:15')\n    >>> ts + BQuarterEnd(1, startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BQuarterEnd(startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    "
    __class__ = BQuarterEnd
    def __init__(self, *args, **kwargs):
        "\n    DateOffset increments between the last business day of each Quarter.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BQuarterEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BQuarterEnd()\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BQuarterEnd(2)\n    Timestamp('2020-09-30 05:01:15')\n    >>> ts + BQuarterEnd(1, startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BQuarterEnd(startingMonth=2)\n    Timestamp('2020-05-29 05:01:15')\n    "
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
    
    _day_opt = 'business_end'
    _default_starting_month = 3
    @classmethod
    def _from_name(cls):
        pass
    
    _from_name_starting_month = 12
    _output_name = 'BusinessQuarterEnd'
    _prefix = 'BQ'

class BYearBegin(YearOffset):
    "\n    DateOffset increments between the first business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BYearBegin()\n    Timestamp('2021-01-01 05:01:15')\n    >>> ts - BYearBegin()\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(-1)\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(2)\n    Timestamp('2022-01-03 05:01:15')\n    "
    __class__ = BYearBegin
    def __init__(self, *args, **kwargs):
        "\n    DateOffset increments between the first business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearBegin\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BYearBegin()\n    Timestamp('2021-01-01 05:01:15')\n    >>> ts - BYearBegin()\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(-1)\n    Timestamp('2020-01-01 05:01:15')\n    >>> ts + BYearBegin(2)\n    Timestamp('2022-01-03 05:01:15')\n    "
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
    
    _day_opt = 'business_start'
    _default_month = 1
    @classmethod
    def _from_name(cls):
        pass
    
    _outputName = 'BusinessYearBegin'
    _prefix = 'BAS'

class BYearEnd(YearOffset):
    "\n    DateOffset increments between the last business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts - BYearEnd()\n    Timestamp('2019-12-31 05:01:15')\n    >>> ts + BYearEnd()\n    Timestamp('2020-12-31 05:01:15')\n    >>> ts + BYearEnd(3)\n    Timestamp('2022-12-30 05:01:15')\n    >>> ts + BYearEnd(-3)\n    Timestamp('2017-12-29 05:01:15')\n    >>> ts + BYearEnd(month=11)\n    Timestamp('2020-11-30 05:01:15')\n    "
    __class__ = BYearEnd
    def __init__(self, *args, **kwargs):
        "\n    DateOffset increments between the last business day of the year.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BYearEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts - BYearEnd()\n    Timestamp('2019-12-31 05:01:15')\n    >>> ts + BYearEnd()\n    Timestamp('2020-12-31 05:01:15')\n    >>> ts + BYearEnd(3)\n    Timestamp('2022-12-30 05:01:15')\n    >>> ts + BYearEnd(-3)\n    Timestamp('2017-12-29 05:01:15')\n    >>> ts + BYearEnd(month=11)\n    Timestamp('2020-11-30 05:01:15')\n    "
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
    
    _day_opt = 'business_end'
    _default_month = 12
    @classmethod
    def _from_name(cls):
        pass
    
    _outputName = 'BusinessYearEnd'
    _prefix = 'BA'

class BaseOffset(_mod_builtins.object):
    '\n    Base class for DateOffset methods that are not overridden by subclasses.\n    '
    def __add__(self, value):
        'Return self+value.'
        return BaseOffset()
    
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = BaseOffset
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getstate__(self):
        'Return a pickleable state'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        '\n    Base class for DateOffset methods that are not overridden by subclasses.\n    '
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
    
    def __mul__(self, value):
        'Return self*value.'
        return BaseOffset()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return BaseOffset()
    
    def __radd__(self, value):
        'Return value+self.'
        return BaseOffset()
    
    def __reduce_cython__(self):
        pass
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return BaseOffset()
    
    def __rsub__(self, value):
        'Return value-self.'
        return BaseOffset()
    
    def __setstate__(self, state):
        'Reconstruct an instance from a pickled state'
        return None
    
    def __setstate_cython__(self):
        pass
    
    def __sub__(self, value):
        'Return self-value.'
        return BaseOffset()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _adjust_dst = True
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    @property
    def _cache(self):
        pass
    
    _day_opt = None
    _deprecations = _mod_builtins.frozenset()
    def _get_offset_day(self):
        pass
    
    def _offset_str(self):
        pass
    
    _params = _mod_pandas__libs_properties.CachedProperty()
    @property
    def _prefix(self):
        pass
    
    def _repr_attrs(self):
        pass
    
    _use_relativedelta = False
    @classmethod
    def _validate_n(cls):
        '\n        Require that `n` be an integer.\n\n        Parameters\n        ----------\n        n : int\n\n        Returns\n        -------\n        nint : int\n\n        Raises\n        ------\n        TypeError if `int(n)` raises\n        ValueError if n != int(n)\n        '
        pass
    
    def apply_index(self, other):
        pass
    
    @property
    def base(self):
        '\n        Returns a copy of the calling offset object with n=1 and all other\n        attributes equal.\n        '
        pass
    
    def copy(self):
        pass
    
    freqstr = _mod_pandas__libs_properties.CachedProperty()
    def isAnchored(self):
        pass
    
    def is_anchored(self):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def kwds(self):
        pass
    
    @property
    def n(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def nanos(self):
        pass
    
    @property
    def normalize(self):
        pass
    
    def onOffset(self):
        pass
    
    def rollback(self):
        '\n        Roll provided date backward to next offset only if not on offset.\n\n        Returns\n        -------\n        TimeStamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n        '
        pass
    
    def rollforward(self):
        '\n        Roll provided date forward to next offset only if not on offset.\n\n        Returns\n        -------\n        TimeStamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n        '
        pass
    
    @property
    def rule_code(self):
        pass
    

class BusinessDay(BusinessMixin):
    '\n    DateOffset subclass representing possibly n business days.\n    '
    __class__ = BusinessDay
    def __init__(self, *args, **kwargs):
        '\n    DateOffset subclass representing possibly n business days.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _offset_str(self):
        pass
    
    _period_dtype_code = 5000
    _prefix = 'B'
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_on_offset(self):
        pass
    

class BusinessHour(BusinessMixin):
    '\n    DateOffset subclass representing possibly n business hours.\n    '
    __class__ = BusinessHour
    def __init__(self, *args, **kwargs):
        '\n    DateOffset subclass representing possibly n business hours.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _adjust_dst = False
    _anchor = 0
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _get_business_hours_by_sec(self):
        '\n        Return business hours in a day by seconds.\n        '
        pass
    
    def _get_closing_time(self):
        '\n        Get the closing time of a business hour interval by its opening time.\n\n        Parameters\n        ----------\n        dt : datetime\n            Opening time of a business hour interval.\n\n        Returns\n        -------\n        result : datetime\n            Corresponding closing time.\n        '
        pass
    
    def _is_on_offset(self):
        '\n        Slight speedups using calculated values.\n        '
        pass
    
    def _next_opening_time(self):
        '\n        If self.n and sign have the same sign, return the earliest opening time\n        later than or equal to current time.\n        Otherwise the latest opening time earlier than or equal to current\n        time.\n\n        Opening time always locates on BusinessDay.\n        However, closing time may not if business hour extends over midnight.\n\n        Parameters\n        ----------\n        other : datetime\n            Current time.\n        sign : int, default 1.\n            Either 1 or -1. Going forward in time if it has the same sign as\n            self.n. Going backward in time otherwise.\n\n        Returns\n        -------\n        result : datetime\n            Next opening time.\n        '
        pass
    
    _prefix = 'BH'
    def _prev_opening_time(self):
        '\n        If n is positive, return the latest opening time earlier than or equal\n        to current time.\n        Otherwise the earliest opening time later than or equal to current\n        time.\n\n        Parameters\n        ----------\n        other : datetime\n            Current time.\n\n        Returns\n        -------\n        result : datetime\n            Previous opening time.\n        '
        pass
    
    def _repr_attrs(self):
        pass
    
    def apply(self, other):
        pass
    
    @property
    def end(self):
        pass
    
    def is_on_offset(self):
        pass
    
    next_bday = _mod_pandas__libs_properties.CachedProperty()
    def rollback(self, other):
        '\n        Roll provided date backward to next offset only if not on offset.\n        '
        pass
    
    def rollforward(self, other):
        '\n        Roll provided date forward to next offset only if not on offset.\n        '
        pass
    
    @property
    def start(self):
        pass
    

class BusinessMixin(SingleConstructorOffset):
    '\n    Mixin to business types to provide related functions.\n    '
    __class__ = BusinessMixin
    def __init__(self, *args, **kwargs):
        '\n    Mixin to business types to provide related functions.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def _from_name(cls):
        pass
    
    def _init_custom(self):
        '\n        Additional __init__ for Custom subclasses.\n        '
        pass
    
    @property
    def _offset(self):
        pass
    
    def _repr_attrs(self):
        pass
    
    @property
    def calendar(self):
        pass
    
    @property
    def holidays(self):
        pass
    
    @property
    def offset(self):
        '\n        Alias for self._offset.\n        '
        pass
    
    @property
    def weekmask(self):
        pass
    

class BusinessMonthBegin(MonthOffset):
    "\n    DateOffset of one month at the first business day.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthBegin\n    >>> ts=pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BMonthBegin(2)\n    Timestamp('2020-07-01 05:01:15')\n    >>> ts + BMonthBegin(-3)\n    Timestamp('2020-03-02 05:01:15')\n    "
    __class__ = BusinessMonthBegin
    def __init__(self, *args, **kwargs):
        "\n    DateOffset of one month at the first business day.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthBegin\n    >>> ts=pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthBegin()\n    Timestamp('2020-06-01 05:01:15')\n    >>> ts + BMonthBegin(2)\n    Timestamp('2020-07-01 05:01:15')\n    >>> ts + BMonthBegin(-3)\n    Timestamp('2020-03-02 05:01:15')\n    "
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
    
    _day_opt = 'business_start'
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'BMS'

class BusinessMonthEnd(MonthOffset):
    "\n    DateOffset increments between the last business day of the month\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthEnd()\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BMonthEnd(2)\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BMonthEnd(-2)\n    Timestamp('2020-03-31 05:01:15')\n    "
    __class__ = BusinessMonthEnd
    def __init__(self, *args, **kwargs):
        "\n    DateOffset increments between the last business day of the month\n\n    Examples\n    --------\n    >>> from pandas.tseries.offset import BMonthEnd\n    >>> ts = pd.Timestamp('2020-05-24 05:01:15')\n    >>> ts + BMonthEnd()\n    Timestamp('2020-05-29 05:01:15')\n    >>> ts + BMonthEnd(2)\n    Timestamp('2020-06-30 05:01:15')\n    >>> ts + BMonthEnd(-2)\n    Timestamp('2020-03-31 05:01:15')\n    "
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
    
    _day_opt = 'business_end'
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'BM'

CBMonthBegin = CustomBusinessMonthBegin
CBMonthEnd = CustomBusinessMonthEnd
CDay = CustomBusinessDay
class CustomBusinessDay(BusinessDay):
    "\n    DateOffset subclass representing custom business days excluding holidays.\n\n    Parameters\n    ----------\n    n : int, default 1\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n    offset : timedelta, default timedelta(0)\n    "
    __class__ = CustomBusinessDay
    def __init__(self, *args, **kwargs):
        "\n    DateOffset subclass representing custom business days excluding holidays.\n\n    Parameters\n    ----------\n    n : int, default 1\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n    offset : timedelta, default timedelta(0)\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self):
        pass
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'C'
    def apply(self, other):
        pass
    
    def apply_index(self):
        pass
    
    def is_on_offset(self):
        pass
    

class CustomBusinessHour(BusinessHour):
    '\n    DateOffset subclass representing possibly n custom business days.\n    '
    __class__ = CustomBusinessHour
    def __init__(self, *args, **kwargs):
        '\n    DateOffset subclass representing possibly n custom business days.\n    '
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
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'CBH'

class CustomBusinessMonthBegin(_CustomBusinessMonth):
    __class__ = CustomBusinessMonthBegin
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'CBMS'

class CustomBusinessMonthEnd(_CustomBusinessMonth):
    __class__ = CustomBusinessMonthEnd
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'CBM'

class DateOffset(RelativeDeltaOffset):
    "\n    Standard kind of date increment used for a date range.\n\n    Works exactly like relativedelta in terms of the keyword args you\n    pass in, use of the keyword n is discouraged-- you would be better\n    off specifying n in the keywords you use, but regardless it is\n    there for you. n is needed for DateOffset subclasses.\n\n    DateOffset work as follows.  Each offset specify a set of dates\n    that conform to the DateOffset.  For example, Bday defines this\n    set to be the set of dates that are weekdays (M-F).  To test if a\n    date is in the set of a DateOffset dateOffset we can use the\n    is_on_offset method: dateOffset.is_on_offset(date).\n\n    If a date is not on a valid date, the rollback and rollforward\n    methods can be used to roll the date to the nearest valid date\n    before/after the date.\n\n    DateOffsets can be created to move dates forward a given number of\n    valid dates.  For example, Bday(2) can be added to a date to move\n    it two business days forward.  If the date does not start on a\n    valid date, first it is moved to a valid date.  Thus pseudo code\n    is:\n\n    def __add__(date):\n      date = rollback(date) # does nothing if date is valid\n      return date + <n number of periods>\n\n    When a date offset is created for a negative number of periods,\n    the date is first rolled forward.  The pseudo code is:\n\n    def __add__(date):\n      date = rollforward(date) # does nothing is date is valid\n      return date + <n number of periods>\n\n    Zero presents a problem.  Should it roll forward or back?  We\n    arbitrarily have it rollforward:\n\n    date + BDay(0) == BDay.rollforward(date)\n\n    Since 0 is a bit weird, we suggest avoiding its use.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of time periods the offset represents.\n    normalize : bool, default False\n        Whether to round the result of a DateOffset addition down to the\n        previous midnight.\n    **kwds\n        Temporal parameter that add to or replace the offset value.\n\n        Parameters that **add** to the offset (like Timedelta):\n\n        - years\n        - months\n        - weeks\n        - days\n        - hours\n        - minutes\n        - seconds\n        - microseconds\n        - nanoseconds\n\n        Parameters that **replace** the offset value:\n\n        - year\n        - month\n        - day\n        - weekday\n        - hour\n        - minute\n        - second\n        - microsecond\n        - nanosecond.\n\n    See Also\n    --------\n    dateutil.relativedelta.relativedelta : The relativedelta type is designed\n        to be applied to an existing datetime an can replace specific components of\n        that datetime, or represents an interval of time.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offsets import DateOffset\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=3)\n    Timestamp('2017-04-01 09:10:11')\n\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=2)\n    Timestamp('2017-03-01 09:10:11')\n    "
    __class__ = DateOffset
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "\n    Standard kind of date increment used for a date range.\n\n    Works exactly like relativedelta in terms of the keyword args you\n    pass in, use of the keyword n is discouraged-- you would be better\n    off specifying n in the keywords you use, but regardless it is\n    there for you. n is needed for DateOffset subclasses.\n\n    DateOffset work as follows.  Each offset specify a set of dates\n    that conform to the DateOffset.  For example, Bday defines this\n    set to be the set of dates that are weekdays (M-F).  To test if a\n    date is in the set of a DateOffset dateOffset we can use the\n    is_on_offset method: dateOffset.is_on_offset(date).\n\n    If a date is not on a valid date, the rollback and rollforward\n    methods can be used to roll the date to the nearest valid date\n    before/after the date.\n\n    DateOffsets can be created to move dates forward a given number of\n    valid dates.  For example, Bday(2) can be added to a date to move\n    it two business days forward.  If the date does not start on a\n    valid date, first it is moved to a valid date.  Thus pseudo code\n    is:\n\n    def __add__(date):\n      date = rollback(date) # does nothing if date is valid\n      return date + <n number of periods>\n\n    When a date offset is created for a negative number of periods,\n    the date is first rolled forward.  The pseudo code is:\n\n    def __add__(date):\n      date = rollforward(date) # does nothing is date is valid\n      return date + <n number of periods>\n\n    Zero presents a problem.  Should it roll forward or back?  We\n    arbitrarily have it rollforward:\n\n    date + BDay(0) == BDay.rollforward(date)\n\n    Since 0 is a bit weird, we suggest avoiding its use.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of time periods the offset represents.\n    normalize : bool, default False\n        Whether to round the result of a DateOffset addition down to the\n        previous midnight.\n    **kwds\n        Temporal parameter that add to or replace the offset value.\n\n        Parameters that **add** to the offset (like Timedelta):\n\n        - years\n        - months\n        - weeks\n        - days\n        - hours\n        - minutes\n        - seconds\n        - microseconds\n        - nanoseconds\n\n        Parameters that **replace** the offset value:\n\n        - year\n        - month\n        - day\n        - weekday\n        - hour\n        - minute\n        - second\n        - microsecond\n        - nanosecond.\n\n    See Also\n    --------\n    dateutil.relativedelta.relativedelta : The relativedelta type is designed\n        to be applied to an existing datetime an can replace specific components of\n        that datetime, or represents an interval of time.\n\n    Examples\n    --------\n    >>> from pandas.tseries.offsets import DateOffset\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=3)\n    Timestamp('2017-04-01 09:10:11')\n\n    >>> ts = pd.Timestamp('2017-01-01 09:10:11')\n    >>> ts + DateOffset(months=2)\n    Timestamp('2017-03-01 09:10:11')\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Day(Tick):
    __class__ = Day
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 86400000000000
    _period_dtype_code = 6000
    _prefix = 'D'

class Easter(SingleConstructorOffset):
    '\n    DateOffset for the Easter holiday using logic defined in dateutil.\n\n    Right now uses the revised method which is valid in years 1583-4099.\n    '
    __class__ = Easter
    def __init__(self, *args, **kwargs):
        '\n    DateOffset for the Easter holiday using logic defined in dateutil.\n\n    Right now uses the revised method which is valid in years 1583-4099.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def _from_name(cls):
        pass
    
    def apply(self, other):
        pass
    
    def is_on_offset(self):
        pass
    

class FY5253(FY5253Mixin):
    '\n    Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ... 12}, default 1\n        The month in which the fiscal year ends.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
    __class__ = FY5253
    def __init__(self, *args, **kwargs):
        '\n    Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ... 12}, default 1\n        The month in which the fiscal year ends.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
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
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    @classmethod
    def _parse_suffix(cls):
        pass
    
    _prefix = 'RE'
    def apply(self, other):
        pass
    
    def get_year_end(self):
        pass
    
    def is_on_offset(self):
        pass
    

class FY5253Mixin(SingleConstructorOffset):
    __class__ = FY5253Mixin
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def _from_name(cls):
        pass
    
    def _get_suffix_prefix(self):
        pass
    
    def get_rule_code_suffix(self):
        pass
    
    def is_anchored(self):
        pass
    
    @property
    def rule_code(self):
        pass
    
    @property
    def startingMonth(self):
        pass
    
    @property
    def variation(self):
        pass
    
    @property
    def weekday(self):
        pass
    

class FY5253Quarter(FY5253Mixin):
    '\n    DateOffset increments between business quarter dates\n    for 52-53 week fiscal year (also known as a 4-4-5 calendar).\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ..., 12}, default 1\n        The month in which fiscal years end.\n\n    qtr_with_extra_week : int {1, 2, 3, 4}, default 1\n        The quarter number that has the leap or 14 week when needed.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
    __class__ = FY5253Quarter
    def __init__(self, *args, **kwargs):
        '\n    DateOffset increments between business quarter dates\n    for 52-53 week fiscal year (also known as a 4-4-5 calendar).\n\n    It is used by companies that desire that their\n    fiscal year always end on the same day of the week.\n\n    It is a method of managing accounting periods.\n    It is a common calendar structure for some industries,\n    such as retail, manufacturing and parking industry.\n\n    For more information see:\n    https://en.wikipedia.org/wiki/4-4-5_calendar\n\n    The year may either:\n\n    - end on the last X day of the Y month.\n    - end on the last X day closest to the last day of the Y month.\n\n    X is a specific day of the week.\n    Y is a certain month of the year\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...\n\n    Parameters\n    ----------\n    n : int\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n\n    startingMonth : int {1, 2, ..., 12}, default 1\n        The month in which fiscal years end.\n\n    qtr_with_extra_week : int {1, 2, 3, 4}, default 1\n        The quarter number that has the leap or 14 week when needed.\n\n    variation : str, default "nearest"\n        Method of employing 4-4-5 calendar.\n\n        There are two options:\n\n        - "nearest" means year end is **weekday** closest to last day of month in year.\n        - "last" means year end is final **weekday** of the final month in fiscal year.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    _offset = _mod_pandas__libs_properties.CachedProperty()
    _prefix = 'REQ'
    def _rollback_to_year(self):
        '\n        Roll `other` back to the most recent date that was on a fiscal year\n        end.\n\n        Return the date of that year-end, the number of full quarters\n        elapsed between that year-end and other, and the remaining Timedelta\n        since the most recent quarter-end.\n\n        Parameters\n        ----------\n        other : datetime or Timestamp\n\n        Returns\n        -------\n        tuple of\n        prev_year_end : Timestamp giving most recent fiscal year end\n        num_qtrs : int\n        tdelta : Timedelta\n        '
        pass
    
    def apply(self, other):
        pass
    
    def get_weeks(self):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def qtr_with_extra_week(self):
        pass
    
    @property
    def rule_code(self):
        pass
    
    def year_has_extra_week(self):
        pass
    

class Hour(Tick):
    __class__ = Hour
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 3600000000000
    _period_dtype_code = 7000
    _prefix = 'H'

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'
class LastWeekOfMonth(WeekOfMonthMixin):
    '\n    Describes monthly dates in last week of month like "the last Tuesday of\n    each month".\n\n    Parameters\n    ----------\n    n : int, default 1\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
    __class__ = LastWeekOfMonth
    def __init__(self, *args, **kwargs):
        '\n    Describes monthly dates in last week of month like "the last Tuesday of\n    each month".\n\n    Parameters\n    ----------\n    n : int, default 1\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _get_offset_day(self):
        '\n        Find the day in the same month as other that has the same\n        weekday as self.weekday and is the last such day in the month.\n\n        Parameters\n        ----------\n        other: datetime\n\n        Returns\n        -------\n        day: int\n        '
        pass
    
    _prefix = 'LWOM'

MONTH_ALIASES = _mod_builtins.dict()
MONTH_TO_CAL_NUM = _mod_builtins.dict()
class Micro(Tick):
    __class__ = Micro
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 1000
    _period_dtype_code = 11000
    _prefix = 'U'

class Milli(Tick):
    __class__ = Milli
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 1000000
    _period_dtype_code = 10000
    _prefix = 'L'

class Minute(Tick):
    __class__ = Minute
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 60000000000
    _period_dtype_code = 8000
    _prefix = 'T'

class MonthBegin(MonthOffset):
    '\n    DateOffset of one month at beginning.\n    '
    __class__ = MonthBegin
    def __init__(self, *args, **kwargs):
        '\n    DateOffset of one month at beginning.\n    '
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
    
    _day_opt = 'start'
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'MS'

class MonthEnd(MonthOffset):
    '\n    DateOffset of one month end.\n    '
    __class__ = MonthEnd
    def __init__(self, *args, **kwargs):
        '\n    DateOffset of one month end.\n    '
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
    
    _day_opt = 'end'
    @classmethod
    def _from_name(cls):
        pass
    
    _period_dtype_code = 3000
    _prefix = 'M'

class MonthOffset(SingleConstructorOffset):
    __class__ = MonthOffset
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    @classmethod
    def _from_name(cls):
        pass
    
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_on_offset(self):
        pass
    

class Nano(Tick):
    __class__ = Nano
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 1
    _period_dtype_code = 12000
    _prefix = 'N'

class OffsetMeta(_mod_builtins.type):
    '\n    Metaclass that allows us to pretend that all BaseOffset subclasses\n    inherit from DateOffset (which is needed for backward-compatibility).\n    '
    __base__ = _mod_builtins.type
    __bases__ = ()
    __basicsize__ = 880
    __class__ = OffsetMeta
    __dict__ = {}
    __dictoffset__ = 264
    __flags__ = 2148292096
    def __init__(self, *args, **kwargs):
        '\n    Metaclass that allows us to pretend that all BaseOffset subclasses\n    inherit from DateOffset (which is needed for backward-compatibility).\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __instancecheck__(self, cls, obj):
        return bool
    
    __module__ = 'pandas._libs.tslibs.offsets'
    __mro__ = ()
    __name__ = 'OffsetMeta'
    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        '__prepare__() -> dict\nused to create the namespace for the class statement'
        return dict()
    
    __qualname__ = 'OffsetMeta'
    def __subclasscheck__(self, cls, obj):
        return bool
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    __weakrefoffset__ = 368

class QuarterBegin(QuarterOffset):
    '\n    DateOffset increments between Quarter start dates.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n    '
    __class__ = QuarterBegin
    def __init__(self, *args, **kwargs):
        '\n    DateOffset increments between Quarter start dates.\n\n    startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...\n    startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...\n    startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...\n    '
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
    
    _day_opt = 'start'
    _default_starting_month = 3
    @classmethod
    def _from_name(cls):
        pass
    
    _from_name_starting_month = 1
    _prefix = 'QS'

class QuarterEnd(QuarterOffset):
    '\n    DateOffset increments between Quarter end dates.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/31/2007, 6/30/2007, ...\n    '
    __class__ = QuarterEnd
    def __init__(self, *args, **kwargs):
        '\n    DateOffset increments between Quarter end dates.\n\n    startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...\n    startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...\n    startingMonth = 3 corresponds to dates like 3/31/2007, 6/30/2007, ...\n    '
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
    
    _day_opt = 'end'
    _default_starting_month = 3
    @classmethod
    def _from_name(cls):
        pass
    
    @property
    def _period_dtype_code(self):
        pass
    
    _prefix = 'Q'

class QuarterOffset(SingleConstructorOffset):
    __class__ = QuarterOffset
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_anchored(self):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def rule_code(self):
        pass
    
    @property
    def startingMonth(self):
        pass
    

class RelativeDeltaOffset(BaseOffset):
    '\n    DateOffset subclass backed by a dateutil relativedelta object.\n    '
    __class__ = RelativeDeltaOffset
    def __getstate__(self):
        'Return a pickleable state'
        pass
    
    def __init__(self, *args, **kwargs):
        '\n    DateOffset subclass backed by a dateutil relativedelta object.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce_cython__(self):
        pass
    
    def __setstate__(self, state):
        'Reconstruct an instance from a pickled state'
        return None
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _adjust_dst = False
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_on_offset(self):
        pass
    

class Second(Tick):
    __class__ = Second
    def __init__(self, *args, **kwargs):
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _nanos_inc = 1000000000
    _period_dtype_code = 9000
    _prefix = 'S'

class SemiMonthBegin(SemiMonthOffset):
    "\n    Two DateOffset's per month repeating on the first\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {2, 3,...,27}, default 15\n    "
    __class__ = SemiMonthBegin
    def __init__(self, *args, **kwargs):
        "\n    Two DateOffset's per month repeating on the first\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {2, 3,...,27}, default 15\n    "
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'SMS'
    def is_on_offset(self):
        pass
    

class SemiMonthEnd(SemiMonthOffset):
    "\n    Two DateOffset's per month repeating on the last\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {1, 3,...,27}, default 15\n    "
    __class__ = SemiMonthEnd
    def __init__(self, *args, **kwargs):
        "\n    Two DateOffset's per month repeating on the last\n    day of the month and day_of_month.\n\n    Parameters\n    ----------\n    n : int\n    normalize : bool, default False\n    day_of_month : int, {1, 3,...,27}, default 15\n    "
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
    
    @classmethod
    def _from_name(cls):
        pass
    
    _min_day_of_month = 1
    _prefix = 'SM'
    def is_on_offset(self):
        pass
    

class SemiMonthOffset(SingleConstructorOffset):
    __class__ = SemiMonthOffset
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    _default_day_of_month = 15
    @classmethod
    def _from_name(cls):
        pass
    
    _min_day_of_month = 2
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    @property
    def day_of_month(self):
        pass
    
    @property
    def rule_code(self):
        pass
    

class SingleConstructorOffset(BaseOffset):
    __class__ = SingleConstructorOffset
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def _from_name(cls):
        pass
    

class Tick(SingleConstructorOffset):
    def __add__(self, value):
        'Return self+value.'
        return Tick()
    
    __array_priority__ = 1000
    __class__ = Tick
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
    
    def __mul__(self, value):
        'Return self*value.'
        return Tick()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __radd__(self, value):
        'Return value+self.'
        return Tick()
    
    def __rmul__(self, value):
        'Return value*self.'
        return Tick()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Tick()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    _adjust_dst = False
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _next_higher_resolution(self):
        pass
    
    _prefix = 'undefined'
    def _repr_attrs(self):
        pass
    
    def apply(self):
        pass
    
    @property
    def delta(self):
        pass
    
    def is_anchored(self):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def nanos(self):
        pass
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
class Week(SingleConstructorOffset):
    '\n    Weekly offset.\n\n    Parameters\n    ----------\n    weekday : int or None, default None\n        Always generate specific day of week. 0 for Monday.\n    '
    __class__ = Week
    def __init__(self, *args, **kwargs):
        '\n    Weekly offset.\n\n    Parameters\n    ----------\n    weekday : int or None, default None\n        Always generate specific day of week. 0 for Monday.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    _inc = _mod_datetime.timedelta()
    @property
    def _period_dtype_code(self):
        pass
    
    _prefix = 'W'
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_anchored(self):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def rule_code(self):
        pass
    
    @property
    def weekday(self):
        pass
    

class WeekOfMonth(WeekOfMonthMixin):
    '\n    Describes monthly dates like "the Tuesday of the 2nd week of each month".\n\n    Parameters\n    ----------\n    n : int\n    week : int {0, 1, 2, 3, ...}, default 0\n        A specific integer for the week of the month.\n        e.g. 0 is 1st week of month, 1 is the 2nd week, etc.\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
    __class__ = WeekOfMonth
    def __init__(self, *args, **kwargs):
        '\n    Describes monthly dates like "the Tuesday of the 2nd week of each month".\n\n    Parameters\n    ----------\n    n : int\n    week : int {0, 1, 2, 3, ...}, default 0\n        A specific integer for the week of the month.\n        e.g. 0 is 1st week of month, 1 is the 2nd week, etc.\n    weekday : int {0, 1, ..., 6}, default 0\n        A specific integer for the day of the week.\n\n        - 0 is Monday\n        - 1 is Tuesday\n        - 2 is Wednesday\n        - 3 is Thursday\n        - 4 is Friday\n        - 5 is Saturday\n        - 6 is Sunday.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _get_offset_day(self):
        "\n        Find the day in the same month as other that has the same\n        weekday as self.weekday and is the self.week'th such day in the month.\n\n        Parameters\n        ----------\n        other : datetime\n\n        Returns\n        -------\n        day : int\n        "
        pass
    
    _prefix = 'WOM'

class WeekOfMonthMixin(SingleConstructorOffset):
    '\n    Mixin for methods common to WeekOfMonth and LastWeekOfMonth.\n    '
    __class__ = WeekOfMonthMixin
    def __init__(self, *args, **kwargs):
        '\n    Mixin for methods common to WeekOfMonth and LastWeekOfMonth.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def _from_name(cls):
        pass
    
    def apply(self, other):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def rule_code(self):
        pass
    
    @property
    def week(self):
        pass
    
    @property
    def weekday(self):
        pass
    

class YearBegin(YearOffset):
    '\n    DateOffset increments between calendar year begin dates.\n    '
    __class__ = YearBegin
    def __init__(self, *args, **kwargs):
        '\n    DateOffset increments between calendar year begin dates.\n    '
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
    
    _day_opt = 'start'
    _default_month = 1
    @classmethod
    def _from_name(cls):
        pass
    
    _prefix = 'AS'

class YearEnd(YearOffset):
    '\n    DateOffset increments between calendar year ends.\n    '
    __class__ = YearEnd
    def __init__(self, *args, **kwargs):
        '\n    DateOffset increments between calendar year ends.\n    '
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
    
    _day_opt = 'end'
    _default_month = 12
    @classmethod
    def _from_name(cls):
        pass
    
    @property
    def _period_dtype_code(self):
        pass
    
    _prefix = 'A'

class YearOffset(SingleConstructorOffset):
    '\n    DateOffset that just needs a month.\n    '
    __class__ = YearOffset
    def __init__(self, *args, **kwargs):
        '\n    DateOffset that just needs a month.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _apply_array(self, other):
        return numpy.ndarray
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def _get_offset_day(self):
        pass
    
    def apply(self, other):
        pass
    
    def apply_index(self, other):
        pass
    
    def is_on_offset(self):
        pass
    
    @property
    def month(self):
        pass
    
    @property
    def rule_code(self):
        pass
    

class _CustomBusinessMonth(BusinessMixin):
    "\n    DateOffset subclass representing custom business month(s).\n\n    Increments between beginning/end of month dates.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n        Calendar to integrate.\n    offset : timedelta, default timedelta(0)\n        Time offset to apply.\n    "
    __class__ = _CustomBusinessMonth
    def __init__(self, *args, **kwargs):
        "\n    DateOffset subclass representing custom business month(s).\n\n    Increments between beginning/end of month dates.\n\n    Parameters\n    ----------\n    n : int, default 1\n        The number of months represented.\n    normalize : bool, default False\n        Normalize start/end dates to midnight before generating date range.\n    weekmask : str, Default 'Mon Tue Wed Thu Fri'\n        Weekmask of valid business days, passed to ``numpy.busdaycalendar``.\n    holidays : list\n        List/array of dates to exclude from the set of valid business days,\n        passed to ``numpy.busdaycalendar``.\n    calendar : pd.HolidayCalendar or np.busdaycalendar\n        Calendar to integrate.\n    offset : timedelta, default timedelta(0)\n        Time offset to apply.\n    "
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
    
    _attributes = _mod_builtins.tuple()
    @classmethod
    def _from_name(cls):
        pass
    
    def apply(self, other):
        pass
    
    cbday_roll = _mod_pandas__libs_properties.CachedProperty()
    m_offset = _mod_pandas__libs_properties.CachedProperty()
    month_roll = _mod_pandas__libs_properties.CachedProperty()

__builtins__ = {}
__doc__ = None
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/offsets.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.offsets'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_BaseOffset():
    pass

def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_RelativeDeltaOffset():
    pass

__test__ = _mod_builtins.dict()
_dont_uppercase = _mod_builtins.set()
def _get_offset():
    "\n    Return DateOffset object associated with rule name.\n\n    Examples\n    --------\n    _get_offset('EOM') --> BMonthEnd(1)\n    "
    pass

_lite_rule_alias = _mod_builtins.dict()
_offset_map = _mod_builtins.dict()
_relativedelta_kwds = _mod_builtins.set()
def apply_array_wraps():
    pass

def apply_index_wraps():
    pass

def apply_wrapper_core():
    pass

def apply_wraps():
    pass

cache_readonly = _mod_pandas__libs_properties.CachedProperty
def delta_to_tick():
    pass

def easter(year, method):
    '\n    This method was ported from the work done by GM Arts,\n    on top of the algorithm by Claus Tondering, which was\n    based in part on the algorithm of Ouding (1940), as\n    quoted in "Explanatory Supplement to the Astronomical\n    Almanac", P.  Kenneth Seidelmann, editor.\n\n    This algorithm implements three different easter\n    calculation methods:\n\n    1 - Original calculation in Julian calendar, valid in\n        dates after 326 AD\n    2 - Original method, with date converted to Gregorian\n        calendar, valid in years 1583 to 4099\n    3 - Revised method, in Gregorian calendar, valid in\n        years 1583 to 4099 as well\n\n    These methods are represented by the constants:\n\n    * ``EASTER_JULIAN   = 1``\n    * ``EASTER_ORTHODOX = 2``\n    * ``EASTER_WESTERN  = 3``\n\n    The default method is method 3.\n\n    More about the algorithm may be found at:\n\n    `GM Arts: Easter Algorithms <http://www.gmarts.org/index.php?go=415>`_\n\n    and\n\n    `The Calendar FAQ: Easter <https://www.tondering.dk/claus/cal/easter.php>`_\n\n    '
    pass

int_to_weekday = _mod_builtins.dict()
opattern = _mod_re.Pattern()
prefix_mapping = _mod_builtins.dict()
relativedelta = _mod_dateutil_relativedelta.relativedelta
def roll_convention():
    '\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : int, generally the day component of a datetime\n    n : number of periods to increment, before adjusting for rolling\n    compare : int, generally the day component of a datetime, in the same\n              month as the datetime form which `other` was taken.\n\n    Returns\n    -------\n    n : int number of periods to increment\n    '
    pass

def roll_qtrday():
    "\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : int reference month giving the first month of the year\n    day_opt : {'start', 'end', 'business_start', 'business_end'}\n        The convention to use in finding the day in a given month against\n        which to compare for rollforward/rollbackward decisions.\n    modby : int 3 for quarters, 12 for years\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    See Also\n    --------\n    get_day_of_month : Find the day in a month provided an offset.\n    "
    pass

def shift_day():
    "\n    Increment the datetime `other` by the given number of days, retaining\n    the time-portion of the datetime.  For tz-naive datetimes this is\n    equivalent to adding a timedelta.  For tz-aware datetimes it is similar to\n    dateutil's relativedelta.__add__, but handles pytz tzinfo objects.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    days : int\n\n    Returns\n    -------\n    shifted: datetime or Timestamp\n    "
    pass

def shift_month():
    "\n    Given a datetime (or Timestamp) `stamp`, an integer `months` and an\n    option `day_opt`, return a new datetimelike that many months later,\n    with day determined by `day_opt` using relativedelta semantics.\n\n    Scalar analogue of shift_months\n\n    Parameters\n    ----------\n    stamp : datetime or Timestamp\n    months : int\n    day_opt : None, 'start', 'end', 'business_start', 'business_end', or int\n        None: returned datetimelike has the same day as the input, or the\n              last day of the month if the new month is too short\n        'start': returned datetimelike has day=1\n        'end': returned datetimelike has day on the last day of the month\n        'business_start': returned datetimelike has day on the first\n            business day of the month\n        'business_end': returned datetimelike has day on the last\n            business day of the month\n        int: returned datetimelike has day equal to day_opt\n\n    Returns\n    -------\n    shifted : datetime or Timestamp (same as input `stamp`)\n    "
    pass

def shift_months():
    "\n    Given an int64-based datetime index, shift all elements\n    specified number of months using DateOffset semantics\n\n    day_opt: {None, 'start', 'end', 'business_start', 'business_end'}\n       * None: day of month\n       * 'start' 1st day of month\n       * 'end' last day of month\n    "
    pass

def to_offset():
    '\n    Return DateOffset object from string or tuple representation\n    or datetime.timedelta object.\n\n    Parameters\n    ----------\n    freq : str, tuple, datetime.timedelta, DateOffset or None\n\n    Returns\n    -------\n    DateOffset or None\n\n    Raises\n    ------\n    ValueError\n        If freq is an invalid frequency\n\n    See Also\n    --------\n    DateOffset : Standard kind of date increment used for a date range.\n\n    Examples\n    --------\n    >>> to_offset("5min")\n    <5 * Minutes>\n\n    >>> to_offset("1D1H")\n    <25 * Hours>\n\n    >>> to_offset("2W")\n    <2 * Weeks: weekday=6>\n\n    >>> to_offset("2B")\n    <2 * BusinessDays>\n\n    >>> to_offset(pd.Timedelta(days=1))\n    <Day>\n\n    >>> to_offset(Hour())\n    <Hour>\n    '
    pass

weekday_to_int = _mod_builtins.dict()
