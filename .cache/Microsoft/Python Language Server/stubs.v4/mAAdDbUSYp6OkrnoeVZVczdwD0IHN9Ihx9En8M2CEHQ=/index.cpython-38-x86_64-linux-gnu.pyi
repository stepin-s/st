import builtins as _mod_builtins

class BaseMultiIndexCodesEngine(_mod_builtins.object):
    '\n    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which\n    represent each label in a MultiIndex as an integer, by juxtaposing the bits\n    encoding each level, with appropriate offsets.\n\n    For instance: if 3 levels have respectively 3, 6 and 1 possible values,\n    then their labels can be represented using respectively 2, 3 and 1 bits,\n    as follows:\n     _ _ _ _____ _ __ __ __\n    |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)\n     — — — ————— — —— —— ——\n    |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)\n     — — — ————— — —— —— ——\n    |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)\n     ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾\n    and the resulting unsigned integer representation will be:\n     _ _ _ _____ _ __ __ __ __ __ __\n    |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|\n     ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾\n\n    Offsets are calculated at initialization, labels are transformed by method\n    _codes_to_ints.\n\n    Keys are located by first locating each component against the respective\n    level, then locating (the integer representation of) codes.\n    '
    __class__ = BaseMultiIndexCodesEngine
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self):
        '\n        Parameters\n        ----------\n        levels : list-like of numpy arrays\n            Levels of the MultiIndex.\n        labels : list-like of numpy arrays of integer dtype\n            Labels of the MultiIndex.\n        offsets : numpy array of uint64 dtype\n            Pre-calculated offsets, one for each level of the index.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _codes_to_ints(self):
        pass
    
    def _extract_level_codes(self):
        '\n        Map the requested list of (tuple) keys to their integer representations\n        for searching in the underlying integer index.\n\n        Parameters\n        ----------\n        target : list-like of keys\n            Each key is a tuple, with a label for each level of the index.\n\n        Returns\n        ------\n        int_keys : 1-dimensional array of dtype uint64 or object\n            Integers representing one combination each\n        '
        pass
    
    def get_indexer(self):
        '\n        Returns an array giving the positions of each value of `target` in\n        `values`, where -1 represents a value in `target` which does not\n        appear in `values`\n\n        If `method` is "backfill" then the position for a value in `target`\n        which does not appear in `values` is that of the next greater value\n        in `values` (if one exists), and -1 if there is no such value.\n\n        Similarly, if the method is "pad" then the position for a value in\n        `target` which does not appear in `values` is that of the next smaller\n        value in `values` (if one exists), and -1 if there is no such value.\n\n        Parameters\n        ----------\n        target: list-like of tuples\n            need not be sorted, but all must have the same length, which must be\n            the same as the length of all tuples in `values`\n        values : list-like of tuples\n            must be sorted and all have the same length.  Should be the set of\n            the MultiIndex\'s values.  Needed only if `method` is not None\n        method: string\n            "backfill" or "pad"\n        limit: int, optional\n            if provided, limit the number of fills to this value\n\n        Returns\n        -------\n        np.ndarray[int64_t, ndim=1] of the indexer of `target` into `values`,\n        filled with the `method` (and optionally `limit`) specified\n        '
        pass
    
    def get_indexer_no_fill(self):
        '\n        Returns an array giving the positions of each value of `target` in\n        `self.values`, where -1 represents a value in `target` which does not\n        appear in `self.values`\n\n        Parameters\n        ----------\n        target : list-like of keys\n            Each key is a tuple, with a label for each level of the index\n\n        Returns\n        -------\n        np.ndarray[int64_t, ndim=1] of the indexer of `target` into\n        `self.values`\n        '
        pass
    
    def get_indexer_non_unique(self):
        pass
    
    def get_loc(self):
        pass
    

class DatetimeEngine(Int64Engine):
    __class__ = DatetimeEngine
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_backfill_indexer(self):
        pass
    
    def get_indexer(self):
        pass
    
    def get_indexer_non_unique(self):
        pass
    
    def get_loc(self):
        pass
    
    def get_pad_indexer(self):
        pass
    

class Float32Engine(IndexEngine):
    __class__ = Float32Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Float64Engine(IndexEngine):
    __class__ = Float64Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class IndexEngine(_mod_builtins.object):
    __class__ = IndexEngine
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    def __sizeof__(self):
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear_mapping(self):
        pass
    
    def get_backfill_indexer(self):
        pass
    
    def get_indexer(self):
        pass
    
    def get_indexer_non_unique(self):
        '\n        Return an indexer suitable for taking from a non unique index\n        return the labels in the same order ast the target\n        and a missing indexer into the targets (which correspond\n        to the -1 indices in the results\n        '
        pass
    
    def get_loc(self):
        pass
    
    def get_pad_indexer(self):
        pass
    
    @property
    def is_mapping_populated(self):
        pass
    
    @property
    def is_monotonic_decreasing(self):
        pass
    
    @property
    def is_monotonic_increasing(self):
        pass
    
    @property
    def is_unique(self):
        pass
    
    @property
    def mapping(self):
        pass
    
    @property
    def over_size_threshold(self):
        pass
    
    def sizeof(self):
        ' return the sizeof our mapping '
        pass
    
    @property
    def vgetter(self):
        pass
    

class Int16Engine(IndexEngine):
    __class__ = Int16Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Int32Engine(IndexEngine):
    __class__ = Int32Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Int64Engine(IndexEngine):
    __class__ = Int64Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Int8Engine(IndexEngine):
    __class__ = Int8Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ObjectEngine(IndexEngine):
    '\n    Index Engine for use with object-dtype Index, namely the base class Index.\n    '
    __class__ = ObjectEngine
    def __init__(self, *args, **kwargs):
        '\n    Index Engine for use with object-dtype Index, namely the base class Index.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class PeriodEngine(Int64Engine):
    __class__ = PeriodEngine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_loc(self):
        pass
    

class TimedeltaEngine(DatetimeEngine):
    __class__ = TimedeltaEngine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class UInt16Engine(IndexEngine):
    __class__ = UInt16Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class UInt32Engine(IndexEngine):
    __class__ = UInt32Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class UInt64Engine(IndexEngine):
    __class__ = UInt64Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class UInt8Engine(IndexEngine):
    __class__ = UInt8Engine
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

_SIZE_CUTOFF = 1000000
__builtins__ = {}
__doc__ = None
__file__ = '/home/st/.local/lib/python3.8/site-packages/pandas/_libs/index.cpython-38-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.index'
__package__ = 'pandas._libs'
def __pyx_unpickle_BaseMultiIndexCodesEngine():
    pass

def __pyx_unpickle_DatetimeEngine():
    pass

def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Float32Engine():
    pass

def __pyx_unpickle_Float64Engine():
    pass

def __pyx_unpickle_IndexEngine():
    pass

def __pyx_unpickle_Int16Engine():
    pass

def __pyx_unpickle_Int32Engine():
    pass

def __pyx_unpickle_Int64Engine():
    pass

def __pyx_unpickle_Int8Engine():
    pass

def __pyx_unpickle_ObjectEngine():
    pass

def __pyx_unpickle_PeriodEngine():
    pass

def __pyx_unpickle_TimedeltaEngine():
    pass

def __pyx_unpickle_UInt16Engine():
    pass

def __pyx_unpickle_UInt32Engine():
    pass

def __pyx_unpickle_UInt64Engine():
    pass

def __pyx_unpickle_UInt8Engine():
    pass

__test__ = _mod_builtins.dict()
def checknull():
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n     - NA\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

