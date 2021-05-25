import builtins as _mod_builtins
import curses as _mod_curses

ALL_MOUSE_EVENTS = 268435455
A_ALTCHARSET = 4194304
A_ATTRIBUTES = 4294967040
A_BLINK = 524288
A_BOLD = 2097152
A_CHARTEXT = 255
A_COLOR = 65280
A_DIM = 1048576
A_HORIZONTAL = 33554432
A_INVIS = 8388608
A_ITALIC = 2147483648
A_LEFT = 67108864
A_LOW = 134217728
A_NORMAL = 0
A_PROTECT = 16777216
A_REVERSE = 262144
A_RIGHT = 268435456
A_STANDOUT = 65536
A_TOP = 536870912
A_UNDERLINE = 131072
A_VERTICAL = 1073741824
BUTTON1_CLICKED = 4
BUTTON1_DOUBLE_CLICKED = 8
BUTTON1_PRESSED = 2
BUTTON1_RELEASED = 1
BUTTON1_TRIPLE_CLICKED = 16
BUTTON2_CLICKED = 128
BUTTON2_DOUBLE_CLICKED = 256
BUTTON2_PRESSED = 64
BUTTON2_RELEASED = 32
BUTTON2_TRIPLE_CLICKED = 512
BUTTON3_CLICKED = 4096
BUTTON3_DOUBLE_CLICKED = 8192
BUTTON3_PRESSED = 2048
BUTTON3_RELEASED = 1024
BUTTON3_TRIPLE_CLICKED = 16384
BUTTON4_CLICKED = 131072
BUTTON4_DOUBLE_CLICKED = 262144
BUTTON4_PRESSED = 65536
BUTTON4_RELEASED = 32768
BUTTON4_TRIPLE_CLICKED = 524288
BUTTON_ALT = 134217728
BUTTON_CTRL = 33554432
BUTTON_SHIFT = 67108864
COLOR_BLACK = 0
COLOR_BLUE = 4
COLOR_CYAN = 6
COLOR_GREEN = 2
COLOR_MAGENTA = 5
COLOR_RED = 1
COLOR_WHITE = 7
COLOR_YELLOW = 3
ERR = -1
KEY_A1 = 348
KEY_A3 = 349
KEY_B2 = 350
KEY_BACKSPACE = 263
KEY_BEG = 354
KEY_BREAK = 257
KEY_BTAB = 353
KEY_C1 = 351
KEY_C3 = 352
KEY_CANCEL = 355
KEY_CATAB = 342
KEY_CLEAR = 333
KEY_CLOSE = 356
KEY_COMMAND = 357
KEY_COPY = 358
KEY_CREATE = 359
KEY_CTAB = 341
KEY_DC = 330
KEY_DL = 328
KEY_DOWN = 258
KEY_EIC = 332
KEY_END = 360
KEY_ENTER = 343
KEY_EOL = 335
KEY_EOS = 334
KEY_EXIT = 361
KEY_F0 = 264
KEY_F1 = 265
KEY_F10 = 274
KEY_F11 = 275
KEY_F12 = 276
KEY_F13 = 277
KEY_F14 = 278
KEY_F15 = 279
KEY_F16 = 280
KEY_F17 = 281
KEY_F18 = 282
KEY_F19 = 283
KEY_F2 = 266
KEY_F20 = 284
KEY_F21 = 285
KEY_F22 = 286
KEY_F23 = 287
KEY_F24 = 288
KEY_F25 = 289
KEY_F26 = 290
KEY_F27 = 291
KEY_F28 = 292
KEY_F29 = 293
KEY_F3 = 267
KEY_F30 = 294
KEY_F31 = 295
KEY_F32 = 296
KEY_F33 = 297
KEY_F34 = 298
KEY_F35 = 299
KEY_F36 = 300
KEY_F37 = 301
KEY_F38 = 302
KEY_F39 = 303
KEY_F4 = 268
KEY_F40 = 304
KEY_F41 = 305
KEY_F42 = 306
KEY_F43 = 307
KEY_F44 = 308
KEY_F45 = 309
KEY_F46 = 310
KEY_F47 = 311
KEY_F48 = 312
KEY_F49 = 313
KEY_F5 = 269
KEY_F50 = 314
KEY_F51 = 315
KEY_F52 = 316
KEY_F53 = 317
KEY_F54 = 318
KEY_F55 = 319
KEY_F56 = 320
KEY_F57 = 321
KEY_F58 = 322
KEY_F59 = 323
KEY_F6 = 270
KEY_F60 = 324
KEY_F61 = 325
KEY_F62 = 326
KEY_F63 = 327
KEY_F7 = 271
KEY_F8 = 272
KEY_F9 = 273
KEY_FIND = 362
KEY_HELP = 363
KEY_HOME = 262
KEY_IC = 331
KEY_IL = 329
KEY_LEFT = 260
KEY_LL = 347
KEY_MARK = 364
KEY_MAX = 511
KEY_MESSAGE = 365
KEY_MIN = 257
KEY_MOUSE = 409
KEY_MOVE = 366
KEY_NEXT = 367
KEY_NPAGE = 338
KEY_OPEN = 368
KEY_OPTIONS = 369
KEY_PPAGE = 339
KEY_PREVIOUS = 370
KEY_PRINT = 346
KEY_REDO = 371
KEY_REFERENCE = 372
KEY_REFRESH = 373
KEY_REPLACE = 374
KEY_RESET = 345
KEY_RESIZE = 410
KEY_RESTART = 375
KEY_RESUME = 376
KEY_RIGHT = 261
KEY_SAVE = 377
KEY_SBEG = 378
KEY_SCANCEL = 379
KEY_SCOMMAND = 380
KEY_SCOPY = 381
KEY_SCREATE = 382
KEY_SDC = 383
KEY_SDL = 384
KEY_SELECT = 385
KEY_SEND = 386
KEY_SEOL = 387
KEY_SEXIT = 388
KEY_SF = 336
KEY_SFIND = 389
KEY_SHELP = 390
KEY_SHOME = 391
KEY_SIC = 392
KEY_SLEFT = 393
KEY_SMESSAGE = 394
KEY_SMOVE = 395
KEY_SNEXT = 396
KEY_SOPTIONS = 397
KEY_SPREVIOUS = 398
KEY_SPRINT = 399
KEY_SR = 337
KEY_SREDO = 400
KEY_SREPLACE = 401
KEY_SRESET = 344
KEY_SRIGHT = 402
KEY_SRSUME = 403
KEY_SSAVE = 404
KEY_SSUSPEND = 405
KEY_STAB = 340
KEY_SUNDO = 406
KEY_SUSPEND = 407
KEY_UNDO = 408
KEY_UP = 259
OK = 0
REPORT_MOUSE_POSITION = 268435456
_C_API = _mod_builtins.PyCapsule()
__doc__ = None
__file__ = '/usr/lib/python3.8/lib-dynload/_curses.cpython-38-x86_64-linux-gnu.so'
__name__ = '_curses'
__package__ = ''
__version__ = b'2.2'
def baudrate():
    'Return the output speed of the terminal in bits per second.'
    pass

def beep():
    'Emit a short attention sound.'
    pass

def can_change_color():
    'Return True if the programmer can change the colors displayed by the terminal.'
    pass

def cbreak(flag):
    'Enter cbreak mode.\n\n  flag\n    If false, the effect is the same as calling nocbreak().\n\nIn cbreak mode (sometimes called "rare" mode) normal tty line buffering is\nturned off and characters are available to be read one by one.  However,\nunlike raw mode, special characters (interrupt, quit, suspend, and flow\ncontrol) retain their effects on the tty driver and calling program.\nCalling first raw() then cbreak() leaves the terminal in cbreak mode.'
    pass

def color_content(color_number):
    'Return the red, green, and blue (RGB) components of the specified color.\n\n  color_number\n    The number of the color (0 - COLORS).\n\nA 3-tuple is returned, containing the R, G, B values for the given color,\nwhich will be between 0 (no component) and 1000 (maximum amount of component).'
    pass

def color_pair(color_number):
    'Return the attribute value for displaying text in the specified color.\n\n  color_number\n    The number of the color (0 - COLORS).\n\nThis attribute value can be combined with A_STANDOUT, A_REVERSE, and the\nother A_* attributes.  pair_number() is the counterpart to this function.'
    pass

def curs_set(visibility):
    'Set the cursor state.\n\n  visibility\n    0 for invisible, 1 for normal visible, or 2 for very visible.\n\nIf the terminal supports the visibility requested, the previous cursor\nstate is returned; otherwise, an exception is raised.  On many terminals,\nthe "visible" mode is an underline cursor and the "very visible" mode is\na block cursor.'
    pass

def def_prog_mode():
    'Save the current terminal mode as the "program" mode.\n\nThe "program" mode is the mode when the running program is using curses.\n\nSubsequent calls to reset_prog_mode() will restore this mode.'
    pass

def def_shell_mode():
    'Save the current terminal mode as the "shell" mode.\n\nThe "shell" mode is the mode when the running program is not using curses.\n\nSubsequent calls to reset_shell_mode() will restore this mode.'
    pass

def delay_output(ms):
    'Insert a pause in output.\n\n  ms\n    Duration in milliseconds.'
    pass

def doupdate():
    'Update the physical screen to match the virtual screen.'
    pass

def echo(flag):
    'Enter echo mode.\n\n  flag\n    If false, the effect is the same as calling noecho().\n\nIn echo mode, each character input is echoed to the screen as it is entered.'
    pass

def endwin():
    'De-initialize the library, and return terminal to normal status.'
    pass

def erasechar():
    "Return the user's current erase character."
    pass

class error(_mod_builtins.Exception):
    __class__ = error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_curses'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def filter():
    pass

def flash():
    'Flash the screen.\n\nThat is, change it to reverse-video and then change it back in a short interval.'
    pass

def flushinp():
    'Flush all input buffers.\n\nThis throws away any typeahead that has been typed by the user and has not\nyet been processed by the program.'
    pass

def getmouse():
    'Retrieve the queued mouse event.\n\nAfter getch() returns KEY_MOUSE to signal a mouse event, this function\nreturns a 5-tuple (id, x, y, z, bstate).'
    pass

def getsyx():
    'Return the current coordinates of the virtual screen cursor.\n\nReturn a (y, x) tuple.  If leaveok is currently true, return (-1, -1).'
    pass

def getwin(file):
    'Read window related data stored in the file by an earlier putwin() call.\n\nThe routine then creates and initializes a new window using that data,\nreturning the new window object.'
    pass

def halfdelay(tenths):
    'Enter half-delay mode.\n\n  tenths\n    Maximal blocking delay in tenths of seconds (1 - 255).\n\nUse nocbreak() to leave half-delay mode.'
    pass

def has_colors():
    'Return True if the terminal can display colors; otherwise, return False.'
    pass

def has_ic():
    'Return True if the terminal has insert- and delete-character capabilities.'
    pass

def has_il():
    'Return True if the terminal has insert- and delete-line capabilities.'
    pass

def has_key(key):
    'Return True if the current terminal type recognizes a key with that value.\n\n  key\n    Key number.'
    pass

def init_color(color_number, r, g, b):
    'Change the definition of a color.\n\n  color_number\n    The number of the color to be changed (0 - COLORS).\n  r\n    Red component (0 - 1000).\n  g\n    Green component (0 - 1000).\n  b\n    Blue component (0 - 1000).\n\nWhen init_color() is used, all occurrences of that color on the screen\nimmediately change to the new definition.  This function is a no-op on\nmost terminals; it is active only if can_change_color() returns 1.'
    pass

def init_pair(pair_number, fg, bg):
    'Change the definition of a color-pair.\n\n  pair_number\n    The number of the color-pair to be changed (1 - (COLOR_PAIRS-1)).\n  fg\n    Foreground color number (0 - COLORS).\n  bg\n    Background color number (0 - COLORS).\n\nIf the color-pair was previously initialized, the screen is refreshed and\nall occurrences of that color-pair are changed to the new definition.'
    pass

def initscr():
    'Initialize the library.\n\nReturn a WindowObject which represents the whole screen.'
    pass

def intrflush(flag):
    pass

def is_term_resized(nlines, ncols):
    'Return True if resize_term() would modify the window structure, False otherwise.\n\n  nlines\n    Height.\n  ncols\n    Width.'
    pass

def isendwin():
    'Return True if endwin() has been called.'
    pass

def keyname(key):
    'Return the name of specified key.\n\n  key\n    Key number.'
    pass

def killchar():
    "Return the user's current line kill character."
    pass

def longname():
    'Return the terminfo long name field describing the current terminal.\n\nThe maximum length of a verbose description is 128 characters.  It is defined\nonly after the call to initscr().'
    pass

def meta(yes):
    'Enable/disable meta keys.\n\nIf yes is True, allow 8-bit characters to be input.  If yes is False,\nallow only 7-bit characters.'
    pass

def mouseinterval(interval):
    'Set and retrieve the maximum time between press and release in a click.\n\n  interval\n    Time in milliseconds.\n\nSet the maximum time that can elapse between press and release events in\norder for them to be recognized as a click, and return the previous interval\nvalue.'
    pass

def mousemask(newmask):
    "Set the mouse events to be reported, and return a tuple (availmask, oldmask).\n\nReturn a tuple (availmask, oldmask).  availmask indicates which of the\nspecified mouse events can be reported; on complete failure it returns 0.\noldmask is the previous value of the given window's mouse event mask.\nIf this function is never called, no mouse events are ever reported."
    pass

def napms(ms):
    'Sleep for specified time.\n\n  ms\n    Duration in milliseconds.'
    pass

ncurses_version = _mod_curses.ncurses_version()
def newpad(nlines, ncols):
    'Create and return a pointer to a new pad data structure.\n\n  nlines\n    Height.\n  ncols\n    Width.'
    pass

def newwin(nlines, ncols, begin_y=0, begin_x=0):
    'newwin(nlines, ncols, [begin_y=0, begin_x=0])\nReturn a new window.\n\n  nlines\n    Height.\n  ncols\n    Width.\n  begin_y\n    Top side y-coordinate.\n  begin_x\n    Left side x-coordinate.\n\nBy default, the window will extend from the specified position to the lower\nright corner of the screen.'
    pass

def nl(flag):
    'Enter newline mode.\n\n  flag\n    If false, the effect is the same as calling nonl().\n\nThis mode translates the return key into newline on input, and translates\nnewline into return and line-feed on output.  Newline mode is initially on.'
    pass

def nocbreak():
    'Leave cbreak mode.\n\nReturn to normal "cooked" mode with line buffering.'
    pass

def noecho():
    'Leave echo mode.\n\nEchoing of input characters is turned off.'
    pass

def nonl():
    'Leave newline mode.\n\nDisable translation of return into newline on input, and disable low-level\ntranslation of newline into newline/return on output.'
    pass

def noqiflush():
    'Disable queue flushing.\n\nWhen queue flushing is disabled, normal flush of input and output queues\nassociated with the INTR, QUIT and SUSP characters will not be done.'
    pass

def noraw():
    'Leave raw mode.\n\nReturn to normal "cooked" mode with line buffering.'
    pass

def pair_content(pair_number):
    'Return a tuple (fg, bg) containing the colors for the requested color pair.\n\n  pair_number\n    The number of the color pair (1 - (COLOR_PAIRS-1)).'
    pass

def pair_number(attr):
    'Return the number of the color-pair set by the specified attribute value.\n\ncolor_pair() is the counterpart to this function.'
    pass

def putp(string):
    'Emit the value of a specified terminfo capability for the current terminal.\n\nNote that the output of putp() always goes to standard output.'
    pass

def qiflush(flag):
    'Enable queue flushing.\n\n  flag\n    If false, the effect is the same as calling noqiflush().\n\nIf queue flushing is enabled, all output in the display driver queue\nwill be flushed when the INTR, QUIT and SUSP characters are read.'
    pass

def raw(flag):
    'Enter raw mode.\n\n  flag\n    If false, the effect is the same as calling noraw().\n\nIn raw mode, normal line buffering and processing of interrupt, quit,\nsuspend, and flow control keys are turned off; characters are presented to\ncurses input functions one by one.'
    pass

def reset_prog_mode():
    'Restore the terminal to "program" mode, as previously saved by def_prog_mode().'
    pass

def reset_shell_mode():
    'Restore the terminal to "shell" mode, as previously saved by def_shell_mode().'
    pass

def resetty():
    'Restore terminal mode.'
    pass

def resize_term(nlines, ncols):
    'Backend function used by resizeterm(), performing most of the work.\n\n  nlines\n    Height.\n  ncols\n    Width.\n\nWhen resizing the windows, resize_term() blank-fills the areas that are\nextended.  The calling application should fill in these areas with appropriate\ndata.  The resize_term() function attempts to resize all windows.  However,\ndue to the calling convention of pads, it is not possible to resize these\nwithout additional interaction with the application.'
    pass

def resizeterm(nlines, ncols):
    'Resize the standard and current windows to the specified dimensions.\n\n  nlines\n    Height.\n  ncols\n    Width.\n\nAdjusts other bookkeeping data used by the curses library that record the\nwindow dimensions (in particular the SIGWINCH handler).'
    pass

def savetty():
    'Save terminal mode.'
    pass

def setsyx(y, x):
    'Set the virtual screen cursor.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n\nIf y and x are both -1, then leaveok is set.'
    pass

def setupterm(term, fd):
    'Initialize the terminal.\n\n  term\n    Terminal name.\n    If omitted, the value of the TERM environment variable will be used.\n  fd\n    File descriptor to which any initialization sequences will be sent.\n    If not supplied, the file descriptor for sys.stdout will be used.'
    pass

def start_color():
    'Initializes eight basic colors and global variables COLORS and COLOR_PAIRS.\n\nMust be called if the programmer wants to use colors, and before any other\ncolor manipulation routine is called.  It is good practice to call this\nroutine right after initscr().\n\nIt also restores the colors on the terminal to the values they had when the\nterminal was just turned on.'
    pass

def termattrs():
    'Return a logical OR of all video attributes supported by the terminal.'
    pass

def termname():
    'Return the value of the environment variable TERM, truncated to 14 characters.'
    pass

def tigetflag(capname):
    'Return the value of the Boolean capability.\n\n  capname\n    The terminfo capability name.\n\nThe value -1 is returned if capname is not a Boolean capability, or 0 if\nit is canceled or absent from the terminal description.'
    pass

def tigetnum(capname):
    'Return the value of the numeric capability.\n\n  capname\n    The terminfo capability name.\n\nThe value -2 is returned if capname is not a numeric capability, or -1 if\nit is canceled or absent from the terminal description.'
    pass

def tigetstr(capname):
    'Return the value of the string capability.\n\n  capname\n    The terminfo capability name.\n\nNone is returned if capname is not a string capability, or is canceled or\nabsent from the terminal description.'
    pass

def tparm(str, i1, i2, i3, i4, i5, i6, i7, i8, i9):
    'Instantiate the specified byte string with the supplied parameters.\n\n  str\n    Parameterized byte string obtained from the terminfo database.'
    pass

def typeahead(fd):
    'Specify that the file descriptor fd be used for typeahead checking.\n\n  fd\n    File descriptor.\n\nIf fd is -1, then no typeahead checking is done.'
    pass

def unctrl(ch):
    'Return a string which is a printable representation of the character ch.\n\nControl characters are displayed as a caret followed by the character,\nfor example as ^C.  Printing characters are left as they are.'
    pass

def unget_wch(ch):
    'Push ch so the next get_wch() will return it.'
    pass

def ungetch(ch):
    'Push ch so the next getch() will return it.'
    pass

def ungetmouse(id, x, y, z, bstate):
    'Push a KEY_MOUSE event onto the input queue.\n\nThe following getmouse() will return the given state data.'
    pass

def update_lines_cols():
    pass

def use_default_colors():
    'Allow use of default values for colors on terminals supporting this feature.\n\nUse this to support transparency in your application.  The default color\nis assigned to the color number -1.'
    pass

def use_env(flag):
    'Use environment variables LINES and COLUMNS.\n\nIf used, this function should be called before initscr() or newterm() are\ncalled.\n\nWhen flag is False, the values of lines and columns specified in the terminfo\ndatabase will be used, even if environment variables LINES and COLUMNS (used\nby default) are set, or if curses is running in a window (in which case\ndefault behavior would be to use the window size if LINES and COLUMNS are\nnot set).'
    pass

version = b'2.2'
class window(_mod_builtins.object):
    __class__ = window
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addch(self, y=None, x=None, ch=None, attr=_curses.A_NORMAL):
        'addch([y, x,] ch, [attr=_curses.A_NORMAL])\nPaint the character.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  ch\n    Character to add.\n  attr\n    Attributes for the character.\n\nPaint character ch at (y, x) with attributes attr,\noverwriting any character previously painted at that location.\nBy default, the character position and attributes are the\ncurrent settings for the window object.'
        pass
    
    def addnstr(self, y=None, x=None, str=None, n=None, attr=None):
        'addnstr([y, x,] str, n, [attr])\nPaint at most n characters of the string.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  str\n    String to add.\n  n\n    Maximal number of characters.\n  attr\n    Attributes for characters.\n\nPaint at most n characters of the string str at (y, x) with\nattributes attr, overwriting anything previously on the display.\nBy default, the character position and attributes are the\ncurrent settings for the window object.'
        pass
    
    def addstr(self, y=None, x=None, str=None, attr=None):
        'addstr([y, x,] str, [attr])\nPaint the string.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  str\n    String to add.\n  attr\n    Attributes for characters.\n\nPaint the string str at (y, x) with attributes attr,\noverwriting anything previously on the display.\nBy default, the character position and attributes are the\ncurrent settings for the window object.'
        pass
    
    def attroff(self, attr):
        'Remove attribute attr from the "background" set.'
        pass
    
    def attron(self, attr):
        'Add attribute attr from the "background" set.'
        pass
    
    def attrset(self, attr):
        'Set the "background" set of attributes.'
        pass
    
    def bkgd(self, ch, attr):
        'Set the background property of the window.\n\n  ch\n    Background character.\n  attr\n    Background attributes.'
        pass
    
    def bkgdset(self, ch, attr):
        "Set the window's background.\n\n  ch\n    Background character.\n  attr\n    Background attributes."
        pass
    
    def border(self):
        'Draw a border around the edges of the window.\n\n  ls\n    Left side.\n  rs\n    Right side.\n  ts\n    Top side.\n  bs\n    Bottom side.\n  tl\n    Upper-left corner.\n  tr\n    Upper-right corner.\n  bl\n    Bottom-left corner.\n  br\n    Bottom-right corner.\n\nEach parameter specifies the character to use for a specific part of the\nborder.  The characters can be specified as integers or as one-character\nstrings.  A 0 value for any parameter will cause the default character to be\nused for that parameter.'
        pass
    
    def box(self, verch=0, horch=0):
        'box([verch=0, horch=0])\nDraw a border around the edges of the window.\n\n  verch\n    Left and right side.\n  horch\n    Top and bottom side.\n\nSimilar to border(), but both ls and rs are verch and both ts and bs are\nhorch.  The default corner characters are always used by this function.'
        pass
    
    def chgat(self):
        pass
    
    def clear(self):
        pass
    
    def clearok(self):
        pass
    
    def clrtobot(self):
        pass
    
    def clrtoeol(self):
        pass
    
    def cursyncup(self):
        pass
    
    def delch(self):
        'delch([y, x])\nDelete any character at (y, x).\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.'
        pass
    
    def deleteln(self):
        pass
    
    def derwin(self):
        'derwin([nlines=0, ncols=0,] begin_y, begin_x)\nCreate a sub-window (window-relative coordinates).\n\n  nlines\n    Height.\n  ncols\n    Width.\n  begin_y\n    Top side y-coordinate.\n  begin_x\n    Left side x-coordinate.\n\nderwin() is the same as calling subwin(), except that begin_y and begin_x\nare relative to the origin of the window, rather than relative to the entire\nscreen.'
        pass
    
    def echochar(self, ch, attr):
        'Add character ch with attribute attr, and refresh.\n\n  ch\n    Character to add.\n  attr\n    Attributes for the character.'
        pass
    
    def enclose(self, y, x):
        'Return True if the screen-relative coordinates are enclosed by the window.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.'
        pass
    
    @property
    def encoding(self):
        'the typecode character used to create the array'
        pass
    
    def erase(self):
        pass
    
    def get_wch(self, y=None, x=None):
        'get_wch([y, x])\nGet a wide character from terminal keyboard.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n\nReturn a character for most keys, or an integer for function keys,\nkeypad keys, and other special keys.'
        pass
    
    def getbegyx(self):
        pass
    
    def getbkgd(self):
        "Return the window's current background character/attribute pair."
        pass
    
    def getch(self, y=None, x=None):
        'getch([y, x])\nGet a character code from terminal keyboard.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n\nThe integer returned does not have to be in ASCII range: function keys,\nkeypad keys and so on return numbers higher than 256.  In no-delay mode, -1\nis returned if there is no input, else getch() waits until a key is pressed.'
        pass
    
    def getkey(self):
        'getkey([y, x])\nGet a character (string) from terminal keyboard.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n\nReturning a string instead of an integer, as getch() does.  Function keys,\nkeypad keys and other special keys return a multibyte string containing the\nkey name.  In no-delay mode, an exception is raised if there is no input.'
        pass
    
    def getmaxyx(self):
        pass
    
    def getparyx(self):
        pass
    
    def getstr(self):
        pass
    
    def getyx(self):
        pass
    
    def hline(self, y=None, x=None, ch=None, n=None, attr=_curses.A_NORMAL):
        'hline([y, x,] ch, n, [attr=_curses.A_NORMAL])\nDisplay a horizontal line.\n\n  y\n    Starting Y-coordinate.\n  x\n    Starting X-coordinate.\n  ch\n    Character to draw.\n  n\n    Line length.\n  attr\n    Attributes for the characters.'
        pass
    
    def idcok(self):
        pass
    
    def idlok(self):
        pass
    
    def immedok(self):
        pass
    
    def inch(self, y=None, x=None):
        'inch([y, x])\nReturn the character at the given position in the window.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n\nThe bottom 8 bits are the character proper, and upper bits are the attributes.'
        pass
    
    def insch(self, y=None, x=None, ch=None, attr=_curses.A_NORMAL):
        'insch([y, x,] ch, [attr=_curses.A_NORMAL])\nInsert a character before the current or specified position.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  ch\n    Character to insert.\n  attr\n    Attributes for the character.\n\nAll characters to the right of the cursor are shifted one position right, with\nthe rightmost characters on the line being lost.'
        pass
    
    def insdelln(self):
        pass
    
    def insertln(self):
        pass
    
    def insnstr(self, y=None, x=None, str=None, n=None, attr=None):
        'insnstr([y, x,] str, n, [attr])\nInsert at most n characters of the string.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  str\n    String to insert.\n  n\n    Maximal number of characters.\n  attr\n    Attributes for characters.\n\nInsert a character string (as many characters as will fit on the line)\nbefore the character under the cursor, up to n characters.  If n is zero\nor negative, the entire string is inserted.  All characters to the right\nof the cursor are shifted right, with the rightmost characters on the line\nbeing lost.  The cursor position does not change (after moving to y, x, if\nspecified).'
        pass
    
    def insstr(self, y=None, x=None, str=None, attr=None):
        'insstr([y, x,] str, [attr])\nInsert the string before the current or specified position.\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  str\n    String to insert.\n  attr\n    Attributes for characters.\n\nInsert a character string (as many characters as will fit on the line)\nbefore the character under the cursor.  All characters to the right of\nthe cursor are shifted right, with the rightmost characters on the line\nbeing lost.  The cursor position does not change (after moving to y, x,\nif specified).'
        pass
    
    def instr(self):
        pass
    
    def is_linetouched(self, line):
        'Return True if the specified line was modified, otherwise return False.\n\n  line\n    Line number.\n\nRaise a curses.error exception if line is not valid for the given window.'
        pass
    
    def is_wintouched(self):
        pass
    
    def keypad(self):
        pass
    
    def leaveok(self):
        pass
    
    def move(self):
        pass
    
    def mvderwin(self):
        pass
    
    def mvwin(self):
        pass
    
    def nodelay(self):
        pass
    
    def notimeout(self):
        pass
    
    def noutrefresh(self, pminrow=None, pmincol=None, sminrow=None, smincol=None, smaxrow=None, smaxcol=None):
        'noutrefresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])\nMark for refresh but wait.\n\nThis function updates the data structure representing the desired state of the\nwindow, but does not force an update of the physical screen.  To accomplish\nthat, call doupdate().'
        pass
    
    def overlay(self, destwin, sminrow=None, smincol=None, dminrow=None, dmincol=None, dmaxrow=None, dmaxcol=None):
        'overlay(destwin, [sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])\nOverlay the window on top of destwin.\n\nThe windows need not be the same size, only the overlapping region is copied.\nThis copy is non-destructive, which means that the current background\ncharacter does not overwrite the old contents of destwin.\n\nTo get fine-grained control over the copied region, the second form of\noverlay() can be used.  sminrow and smincol are the upper-left coordinates\nof the source window, and the other variables mark a rectangle in the\ndestination window.'
        pass
    
    def overwrite(self):
        'overwrite(destwin, [sminrow, smincol, dminrow, dmincol, dmaxrow,\n          dmaxcol])\nOverwrite the window on top of destwin.\n\nThe windows need not be the same size, in which case only the overlapping\nregion is copied.  This copy is destructive, which means that the current\nbackground character overwrites the old contents of destwin.\n\nTo get fine-grained control over the copied region, the second form of\noverwrite() can be used. sminrow and smincol are the upper-left coordinates\nof the source window, the other variables mark a rectangle in the destination\nwindow.'
        pass
    
    def putwin(self, file):
        'Write all data associated with the window into the provided file object.\n\nThis information can be later retrieved using the getwin() function.'
        pass
    
    def redrawln(self, beg, num):
        'Mark the specified lines corrupted.\n\n  beg\n    Starting line number.\n  num\n    The number of lines.\n\nThey should be completely redrawn on the next refresh() call.'
        pass
    
    def redrawwin(self):
        pass
    
    def refresh(self, pminrow=None, pmincol=None, sminrow=None, smincol=None, smaxrow=None, smaxcol=None):
        'refresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])\nUpdate the display immediately.\n\nSynchronize actual screen with previous drawing/deleting methods.\nThe 6 optional arguments can only be specified when the window is a pad\ncreated with newpad().  The additional parameters are needed to indicate\nwhat part of the pad and screen are involved.  pminrow and pmincol specify\nthe upper left-hand corner of the rectangle to be displayed in the pad.\nsminrow, smincol, smaxrow, and smaxcol specify the edges of the rectangle to\nbe displayed on the screen.  The lower right-hand corner of the rectangle to\nbe displayed in the pad is calculated from the screen coordinates, since the\nrectangles must be the same size.  Both rectangles must be entirely contained\nwithin their respective structures.  Negative values of pminrow, pmincol,\nsminrow, or smincol are treated as if they were zero.'
        pass
    
    def resize(self):
        pass
    
    def scroll(self, lines=1):
        'scroll([lines=1])\nScroll the screen or scrolling region.\n\n  lines\n    Number of lines to scroll.\n\nScroll upward if the argument is positive and downward if it is negative.'
        pass
    
    def scrollok(self):
        pass
    
    def setscrreg(self, top, bottom):
        'Define a software scrolling region.\n\n  top\n    First line number.\n  bottom\n    Last line number.\n\nAll scrolling actions will take place in this region.'
        pass
    
    def standend(self):
        pass
    
    def standout(self):
        pass
    
    def subpad(self):
        'subwin([nlines=0, ncols=0,] begin_y, begin_x)\nCreate a sub-window (screen-relative coordinates).\n\n  nlines\n    Height.\n  ncols\n    Width.\n  begin_y\n    Top side y-coordinate.\n  begin_x\n    Left side x-coordinate.\n\nBy default, the sub-window will extend from the specified position to the\nlower right corner of the window.'
        pass
    
    def subwin(self):
        'subwin([nlines=0, ncols=0,] begin_y, begin_x)\nCreate a sub-window (screen-relative coordinates).\n\n  nlines\n    Height.\n  ncols\n    Width.\n  begin_y\n    Top side y-coordinate.\n  begin_x\n    Left side x-coordinate.\n\nBy default, the sub-window will extend from the specified position to the\nlower right corner of the window.'
        pass
    
    def syncdown(self):
        pass
    
    def syncok(self):
        pass
    
    def syncup(self):
        pass
    
    def timeout(self):
        pass
    
    def touchline(self, start, count, changed=True):
        'touchline(start, count, [changed=True])\nPretend count lines have been changed, starting with line start.\n\nIf changed is supplied, it specifies whether the affected lines are marked\nas having been changed (changed=True) or unchanged (changed=False).'
        pass
    
    def touchwin(self):
        pass
    
    def untouchwin(self):
        pass
    
    def vline(self, y=None, x=None, ch=None, n=None, attr=_curses.A_NORMAL):
        'vline([y, x,] ch, n, [attr=_curses.A_NORMAL])\nDisplay a vertical line.\n\n  y\n    Starting Y-coordinate.\n  x\n    Starting X-coordinate.\n  ch\n    Character to draw.\n  n\n    Line length.\n  attr\n    Attributes for the character.'
        pass
    

