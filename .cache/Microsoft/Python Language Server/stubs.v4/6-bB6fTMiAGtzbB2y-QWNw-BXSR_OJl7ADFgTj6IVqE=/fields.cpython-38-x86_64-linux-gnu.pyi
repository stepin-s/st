import builtins as _mod_builtins
import pandas._libs.tslibs.strptime as _mod_pandas__libs_tslibs_strptime

DAYS_FULL = _mod_builtins.list()
LC_TIME = 2
LocaleTime = _mod_pandas__libs_tslibs_strptime.LocaleTime
MONTHS_FULL = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nFunctions for accessing attributes of Timestamp/datetime64/datetime-like\nobjects and arrays\n'
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/fields.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.fields'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def build_field_sarray():
    '\n    Datetime as int64 representation to a structured array of fields\n    '
    pass

def build_isocalendar_sarray():
    '\n    Given a int64-based datetime array, return the ISO 8601 year, week, and day\n    as a structured array.\n    '
    pass

def get_date_field():
    '\n    Given a int64-based datetime index, extract the year, month, etc.,\n    field and return an array of these values.\n    '
    pass

def get_date_name_field():
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. day_name)\n    '
    pass

def get_locale_names():
    '\n    Returns an array of localized day or month names.\n\n    Parameters\n    ----------\n    name_type : string, attribute of LocaleTime() in which to return localized\n        names\n    locale : string\n\n    Returns\n    -------\n    list of locale names\n    '
    pass

def get_start_end_field():
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    pass

def get_timedelta_field():
    '\n    Given a int64-based timedelta index, extract the days, hrs, sec.,\n    field and return an array of these values.\n    '
    pass

def isleapyear_arr():
    'vectorized version of isleapyear; NaT evaluates as False'
    pass

def month_position_check():
    pass

def set_locale(*args, **kwds):
    '\n    Context manager for temporarily setting a locale.\n\n    Parameters\n    ----------\n    new_locale : str or tuple\n        A string of the form <language_country>.<encoding>. For example to set\n        the current locale to US English with a UTF8 encoding, you would pass\n        "en_US.UTF-8".\n    lc_var : int, default `locale.LC_ALL`\n        The category of the locale being set.\n\n    Notes\n    -----\n    This is useful when you want to run a particular block of code under a\n    particular locale, without globally setting the locale. This probably isn\'t\n    thread-safe.\n    '
    pass

