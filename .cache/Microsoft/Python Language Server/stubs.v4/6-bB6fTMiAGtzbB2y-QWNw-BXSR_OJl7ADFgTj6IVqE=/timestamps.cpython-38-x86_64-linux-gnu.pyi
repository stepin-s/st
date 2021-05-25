import builtins as _mod_builtins
import datetime as _mod_datetime
import pandas._libs.tslibs.base as _mod_pandas__libs_tslibs_base
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas

OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
class RoundTo(_mod_builtins.object):
    '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
    MINUS_INFTY = _mod_builtins.property()
    NEAREST_HALF_EVEN = _mod_builtins.property()
    NEAREST_HALF_MINUS_INFTY = _mod_builtins.property()
    NEAREST_HALF_PLUS_INFTY = _mod_builtins.property()
    PLUS_INFTY = _mod_builtins.property()
    __class__ = RoundTo
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.timestamps'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
class Timestamp(_Timestamp):
    "\n    Pandas replacement for python datetime.datetime object.\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp.\n    freq : str, DateOffset\n        Offset which Timestamp will have.\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n    hour, minute, second, microsecond : int, optional, default 0\n    nanosecond : int, optional, default 0\n        .. versionadded:: 0.23.0\n    tzinfo : datetime.tzinfo, optional, default None\n    fold : {0, 1}, default None, keyword-only\n        Due to daylight saving time, one wall clock time can occur twice\n        when shifting from summer to winter time; fold describes whether the\n        datetime-like corresponds  to the first (0) or the second time (1)\n        the wall clock hits the ambiguous time\n\n        .. versionadded:: 1.1.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
    __class__ = Timestamp
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "\n    Pandas replacement for python datetime.datetime object.\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp.\n    freq : str, DateOffset\n        Offset which Timestamp will have.\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n    hour, minute, second, microsecond : int, optional, default 0\n    nanosecond : int, optional, default 0\n        .. versionadded:: 0.23.0\n    tzinfo : datetime.tzinfo, optional, default None\n    fold : {0, 1}, default None, keyword-only\n        Due to daylight saving time, one wall clock time can occur twice\n        when shifting from summer to winter time; fold describes whether the\n        datetime-like corresponds  to the first (0) or the second time (1)\n        the wall clock hits the ambiguous time\n\n        .. versionadded:: 1.1.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
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
    
    def _round(self, freq, mode, ambiguous, nonexistent):
        pass
    
    def astimezone(self, tz):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def ceil(self, freq, ambiguous, nonexistent):
        "\n        return a new Timestamp ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        pass
    
    def combine(self, cls, date, time):
        '\n        Timestamp.combine(date, time)\n\n        date, time -> datetime with same date and time fields.\n        '
        pass
    
    @property
    def daysinmonth(self):
        '\n        Return the number of days in the month.\n        '
        pass
    
    def floor(self, freq, ambiguous, nonexistent):
        "\n        return a new Timestamp floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n        "
        pass
    
    freqstr = _mod_builtins.property()
    @classmethod
    def fromisocalendar(cls):
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        pass
    
    @classmethod
    def fromisoformat(cls):
        'string -> datetime from datetime.isoformat() output'
        pass
    
    def fromordinal(self, cls, ordinal, freq, tz):
        '\n        Timestamp.fromordinal(ordinal, freq=None, tz=None)\n\n        Passed an ordinal, translate and convert to a ts.\n        Note: by definition there cannot be any tz info on the ordinal itself.\n\n        Parameters\n        ----------\n        ordinal : int\n            Date corresponding to a proleptic Gregorian ordinal.\n        freq : str, DateOffset\n            Offset to apply to the Timestamp.\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for the Timestamp.\n        '
        pass
    
    def fromtimestamp(self, cls, ts):
        "\n        Timestamp.fromtimestamp(ts)\n\n        timestamp[, tz] -> tz's local time from POSIX timestamp.\n        "
        pass
    
    max = Timestamp()
    min = Timestamp()
    def now(self, cls, tz):
        '\n        Timestamp.now(tz=None)\n\n        Return new Timestamp object representing current time local to\n        tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        pass
    
    def replace(self, year, month, day, hour, minute, second, microsecond, nanosecond, tzinfo, fold):
        '\n        implements datetime.replace, handles nanoseconds.\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional, default is 0\n\n        Returns\n        -------\n        Timestamp with fields replaced\n        '
        pass
    
    resolution = _mod_pandas__libs_tslibs_timedeltas.Timedelta()
    def round(self, freq, ambiguous, nonexistent):
        "\n        Round the Timestamp to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n        ambiguous : bool or {'raise', 'NaT'}, default 'raise'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n            .. versionadded:: 0.24.0\n        nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    def strptime(self, cls, date_string, format):
        '\n        Timestamp.strptime(string, format)\n\n        Function is not implemented. Use pd.to_datetime().\n        '
        pass
    
    def to_julian_date(self):
        '\n        Convert TimeStamp to a Julian Date.\n        0 Julian date is noon January 1, 4713 BC.\n        '
        return numpy.float64
    
    def today(self, cls, tz):
        '\n        Timestamp.today(cls, tz=None)\n\n        Return the current time in the local timezone.  This differs\n        from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n        '
        pass
    
    tz = _mod_builtins.property()
    def tz_convert(self, tz):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def tz_localize(self, tz, ambiguous, nonexistent):
        "\n        Convert naive Timestamp to local time zone, or remove\n        timezone from tz-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            The behavior is as follows:\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n        "
        pass
    
    def utcfromtimestamp(self, cls, ts):
        '\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a naive UTC datetime from a POSIX timestamp.\n        '
        pass
    
    def utcnow(self, cls):
        '\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n        '
        pass
    
    @property
    def weekofyear(self):
        '\n        Return the week number of the year.\n        '
        pass
    

class _Timestamp(_mod_pandas__libs_tslibs_base.ABCTimestamp):
    def __add__(self, value):
        'Return self+value.'
        return _Timestamp()
    
    __array_priority__ = 100
    __class__ = _Timestamp
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
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __radd__(self, value):
        'Return value+self.'
        return _Timestamp()
    
    def __reduce__(self):
        return ''; return ()
    
    def __reduce_ex__(self, protocol):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rsub__(self, value):
        'Return value-self.'
        return _Timestamp()
    
    def __setstate__(self, state):
        return None
    
    def __sub__(self, value):
        'Return self-value.'
        return _Timestamp()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _date_repr(self):
        pass
    
    @property
    def _repr_base(self):
        pass
    
    @property
    def _short_repr(self):
        pass
    
    @property
    def _time_repr(self):
        pass
    
    @property
    def asm8(self):
        '\n        Return numpy datetime64 format in nanoseconds.\n        '
        pass
    
    @classmethod
    def combine(cls):
        'date, time -> datetime with same date and time fields'
        pass
    
    def day_name(self):
        '\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the day name.\n\n        Returns\n        -------\n        day_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    @property
    def dayofweek(self):
        '\n        Return day of the week.\n        '
        pass
    
    @property
    def dayofyear(self):
        '\n        Return the day of the year.\n        '
        pass
    
    @property
    def days_in_month(self):
        '\n        Return the number of days in the month.\n        '
        pass
    
    @property
    def freq(self):
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
    
    @property
    def is_leap_year(self):
        '\n        Return True if year is a leap year.\n        '
        pass
    
    @property
    def is_month_end(self):
        '\n        Return True if date is last day of month.\n        '
        pass
    
    @property
    def is_month_start(self):
        '\n        Return True if date is first day of month.\n        '
        pass
    
    @property
    def is_quarter_end(self):
        '\n        Return True if date is last day of the quarter.\n        '
        pass
    
    @property
    def is_quarter_start(self):
        '\n        Return True if date is first day of the quarter.\n        '
        pass
    
    @property
    def is_year_end(self):
        '\n        Return True if date is last day of the year.\n        '
        pass
    
    @property
    def is_year_start(self):
        '\n        Return True if date is first day of the year.\n        '
        pass
    
    def isoformat(self):
        pass
    
    def month_name(self):
        '\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the month name.\n\n        Returns\n        -------\n        month_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    @property
    def nanosecond(self):
        pass
    
    def normalize(self):
        '\n        Normalize Timestamp to midnight, preserving tz information.\n        '
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @property
    def quarter(self):
        '\n        Return the quarter of the year.\n        '
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def timestamp(self):
        'Return POSIX timestamp as float.'
        pass
    
    def to_datetime64(self):
        "\n        Return a numpy.datetime64 object with 'ns' precision.\n        "
        pass
    
    def to_numpy(self):
        '\n        Convert the Timestamp to a NumPy datetime64.\n\n        .. versionadded:: 0.25.0\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n        '
        pass
    
    def to_period(self):
        '\n        Return an period of which this timestamp is an observation.\n        '
        pass
    
    def to_pydatetime(self):
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
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
    
    @property
    def value(self):
        pass
    
    @property
    def week(self):
        '\n        Return the week number of the year.\n        '
        pass
    

__builtins__ = {}
__doc__ = '\n_Timestamp is a c-defined subclass of datetime.datetime\n\n_Timestamp is PITA. Because we inherit from datetime, which has very specific\nconstruction requirements, we need to do object instantiation in python\n(see Timestamp class below). This will serve as a C extension type that\nshadows the python class, where we do any heavy lifting.\n'
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/timestamps.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.timestamps'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_no_input = _mod_builtins.object()
_zero_time = _mod_datetime.time()
def get_date_name_field():
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. day_name)\n    '
    pass

def get_start_end_field():
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    pass

def integer_op_not_supported():
    pass

def round_nsint64():
    '\n    Applies rounding mode at given frequency\n\n    Parameters\n    ----------\n    values : :obj:`ndarray`\n    mode : instance of `RoundTo` enumeration\n    freq : str, obj\n\n    Returns\n    -------\n    :obj:`ndarray`\n    '
    pass

