import builtins as _mod_builtins

EPOLLERR = 8
EPOLLET = 2147483648
EPOLLEXCLUSIVE = 268435456
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDHUP = 8192
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256
EPOLL_CLOEXEC = 524288
PIPE_BUF = 4096
POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDHUP = 8192
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256
__doc__ = 'This module supports asynchronous I/O on multiple file descriptors.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file descriptors.'
__name__ = 'select'
__package__ = ''
class epoll(_mod_builtins.object):
    'Returns an epolling object.\n\n  sizehint\n    The expected number of events to be registered.  It must be positive,\n    or -1 to use the default.  It is only used on older systems where\n    epoll_create1() is not available; otherwise it has no effect (though its\n    value is still checked).\n  flags\n    Deprecated and completely ignored.  However, when supplied, its value\n    must be 0 or select.EPOLL_CLOEXEC, otherwise OSError is raised.'
    __class__ = epoll
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        'Returns an epolling object.\n\n  sizehint\n    The expected number of events to be registered.  It must be positive,\n    or -1 to use the default.  It is only used on older systems where\n    epoll_create1() is not available; otherwise it has no effect (though its\n    value is still checked).\n  flags\n    Deprecated and completely ignored.  However, when supplied, its value\n    must be 0 or select.EPOLL_CLOEXEC, otherwise OSError is raised.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'Close the epoll control file descriptor.\n\nFurther operations on the epoll object will raise an exception.'
        pass
    
    @property
    def closed(self):
        'True if the epoll handler is closed'
        pass
    
    def fileno(self):
        'Return the epoll control file descriptor.'
        pass
    
    @classmethod
    def fromfd(cls, type, fd):
        'Create an epoll object from a given control fd.'
        pass
    
    def modify(self, fd, eventmask):
        'Modify event mask for a registered file descriptor.\n\n  fd\n    the target file descriptor of the operation\n  eventmask\n    a bit set composed of the various EPOLL constants'
        pass
    
    def poll(self, timeout, maxevents):
        'Wait for events on the epoll file descriptor.\n\n  timeout\n    the maximum time to wait in seconds (as float);\n    a timeout of None or -1 makes poll wait indefinitely\n  maxevents\n    the maximum number of events returned; -1 means no limit\n\nReturns a list containing any descriptors that have events to report,\nas a list of (fd, events) 2-tuples.'
        pass
    
    def register(self):
        'Registers a new fd or raises an OSError if the fd is already registered.\n\n  fd\n    the target file descriptor of the operation\n  eventmask\n    a bit set composed of the various EPOLL constants\n\nThe epoll interface supports all file descriptors that support poll.'
        pass
    
    def unregister(self, fd):
        'Remove a registered file descriptor from the epoll object.\n\n  fd\n    the target file descriptor of the operation'
        pass
    

error = _mod_builtins.OSError
def poll():
    'Returns a polling object.\n\nThis object supports registering and unregistering file descriptors, and then\npolling them for I/O events.'
    pass

def select(rlist, wlist, xlist, timeout):
    'Wait until one or more file descriptors are ready for some kind of I/O.\n\nThe first three arguments are sequences of file descriptors to be waited for:\nrlist -- wait until ready for reading\nwlist -- wait until ready for writing\nxlist -- wait for an "exceptional condition"\nIf only one kind of condition is required, pass [] for the other lists.\n\nA file descriptor is either a socket or file object, or a small integer\ngotten from a fileno() method call on one of those.\n\nThe optional 4th argument specifies a timeout in seconds; it may be\na floating point number to specify fractions of seconds.  If it is absent\nor None, the call will never time out.\n\nThe return value is a tuple of three lists corresponding to the first three\narguments; each contains the subset of the corresponding file descriptors\nthat are ready.\n\n*** IMPORTANT NOTICE ***\nOn Windows, only sockets are supported; on Unix, all file\ndescriptors can be used.'
    pass

