import builtins as _mod_builtins
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps

OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
__builtins__ = {}
__doc__ = None
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/tslib.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslib'
__package__ = 'pandas._libs'
__test__ = _mod_builtins.dict()
def _test_parse_iso8601():
    '\n    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used\n    only for testing, actual construction uses `convert_str_to_tsobject`\n    '
    pass

def array_to_datetime():
    "\n    Converts a 1D array of date-like values to a numpy array of either:\n        1) datetime64[ns] data\n        2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError\n           is encountered\n\n    Also returns a pytz.FixedOffset if an array of strings with the same\n    timezone offset is passed and utc=True is not passed. Otherwise, None\n    is returned\n\n    Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,\n    strings\n\n    Parameters\n    ----------\n    values : ndarray of object\n         date-like objects to convert\n    errors : str, default 'raise'\n         error behavior when parsing\n    dayfirst : bool, default False\n         dayfirst parsing behavior when encountering datetime strings\n    yearfirst : bool, default False\n         yearfirst parsing behavior when encountering datetime strings\n    utc : bool, default False\n         indicator whether the dates should be UTC\n    require_iso8601 : bool, default False\n         indicator whether the datetime string should be iso8601\n\n    Returns\n    -------\n    tuple (ndarray, tzoffset)\n    "
    pass

def array_with_unit_to_datetime():
    "\n    Convert the ndarray to datetime according to the time unit.\n\n    This function converts an array of objects into a numpy array of\n    datetime64[ns]. It returns the converted array\n    and also returns the timezone offset\n\n    if errors:\n      - raise: return converted values or raise OutOfBoundsDatetime\n          if out of range on the conversion or\n          ValueError for other conversions (e.g. a string)\n      - ignore: return non-convertible values as the same unit\n      - coerce: NaT for non-convertibles\n\n    Parameters\n    ----------\n    values : ndarray of object\n         Date-like objects to convert.\n    unit : str\n         Time unit to use during conversion.\n    errors : str, default 'raise'\n         Error behavior when parsing.\n\n    Returns\n    -------\n    result : ndarray of m8 values\n    tz : parsed timezone offset or None\n    "
    pass

def format_array_from_datetime():
    '\n    return a np object array of the string formatted values\n\n    Parameters\n    ----------\n    values : a 1-d i8 array\n    tz : tzinfo or None, default None\n    format : str or None, default None\n          a strftime capable string\n    na_rep : optional, default is None\n          a nat format\n\n    '
    pass

def parse_datetime_string():
    '\n    Parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

