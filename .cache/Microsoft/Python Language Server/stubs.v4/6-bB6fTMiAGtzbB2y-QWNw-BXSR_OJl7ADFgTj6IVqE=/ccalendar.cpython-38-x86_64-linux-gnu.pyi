import builtins as _mod_builtins

DAYS = _mod_builtins.list()
DAYS_FULL = _mod_builtins.list()
DAY_SECONDS = 86400
HOUR_SECONDS = 3600
MONTHS = _mod_builtins.list()
MONTHS_FULL = _mod_builtins.list()
MONTH_ALIASES = _mod_builtins.dict()
MONTH_NUMBERS = _mod_builtins.dict()
MONTH_TO_CAL_NUM = _mod_builtins.dict()
__builtins__ = {}
__doc__ = '\nCython implementations of functions resembling the stdlib calendar module\n'
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslibs/ccalendar.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.ccalendar'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def get_day_of_year():
    '\n    Return the ordinal day-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    day_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    pass

def get_days_in_month():
    '\n    Return the number of days in the given month of the given year.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    days_in_month : int\n\n    Notes\n    -----\n    Assumes that the arguments are valid.  Passing a month not between 1 and 12\n    risks a segfault.\n    '
    pass

def get_firstbday():
    '\n    Find the first day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    first_bday : int\n    '
    pass

def get_iso_calendar():
    '\n    Return the year, week, and day of year corresponding to ISO 8601\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    year : int32_t\n    week : int32_t\n    day : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    pass

def get_lastbday():
    '\n    Find the last day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    last_bday : int\n    '
    pass

def get_week_of_year():
    '\n    Return the ordinal week-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    week_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    pass

int_to_weekday = _mod_builtins.dict()
weekday_to_int = _mod_builtins.dict()
