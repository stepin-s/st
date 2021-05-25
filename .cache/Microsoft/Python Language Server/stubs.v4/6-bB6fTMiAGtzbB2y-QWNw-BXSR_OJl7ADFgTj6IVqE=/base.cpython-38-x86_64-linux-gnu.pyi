import builtins as _mod_builtins
import datetime as _mod_datetime

class ABCTimestamp(_mod_datetime.datetime):
    __class__ = ABCTimestamp
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce_cython__(self):
        pass
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def combine(cls):
        'date, time -> datetime with same date and time fields'
        pass
    
    @classmethod
    def fromisocalendar(cls):
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        pass
    
    @classmethod
    def fromisoformat(cls):
        'string -> datetime from datetime.isoformat() output'
        pass
    
    @classmethod
    def fromordinal(cls):
        'int -> date corresponding to a proleptic Gregorian ordinal.'
        pass
    
    @classmethod
    def fromtimestamp(cls):
        "timestamp[, tz] -> tz's local time from POSIX timestamp."
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    @classmethod
    def today(cls):
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
        pass
    
    @classmethod
    def utcfromtimestamp(cls):
        'Construct a naive UTC datetime from a POSIX timestamp.'
        pass
    
    @classmethod
    def utcnow(cls):
        'Return a new datetime representing UTC day and time.'
        pass
    

__builtins__ = {}
__doc__ = '\nWe define base classes that will be inherited by Timestamp, Timedelta, etc\nin order to allow for fast isinstance checks without circular dependency issues.\n\nThis is analogous to core.dtypes.generic.\n'
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/base.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.base'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_ABCTimestamp():
    pass

__test__ = _mod_builtins.dict()
