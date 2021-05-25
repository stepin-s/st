import MySQLdb._exceptions as _mod_MySQLdb__exceptions
import _mysql as _mod__mysql
import builtins as _mod_builtins

DataError = _mod_MySQLdb__exceptions.DataError
DatabaseError = _mod_MySQLdb__exceptions.DatabaseError
Error = _mod_MySQLdb__exceptions.Error
IntegrityError = _mod_MySQLdb__exceptions.IntegrityError
InterfaceError = _mod_MySQLdb__exceptions.InterfaceError
InternalError = _mod_MySQLdb__exceptions.InternalError
MySQLError = _mod_MySQLdb__exceptions.MySQLError
NotSupportedError = _mod_MySQLdb__exceptions.NotSupportedError
OperationalError = _mod_MySQLdb__exceptions.OperationalError
ProgrammingError = _mod_MySQLdb__exceptions.ProgrammingError
Warning = _mod_MySQLdb__exceptions.Warning
__builtins__ = {}
__doc__ = 'an adaptation of the MySQL C API (mostly)\n\nYou probably are better off using MySQLdb instead of using this\nmodule directly.\n\nIn general, renaming goes from mysql_* to _mysql.*. _mysql.connect()\nreturns a connection object (MYSQL). Functions which expect MYSQL * as\nan argument are now methods of the connection object. A number of things\nreturn result objects (MYSQL_RES). Functions which expect MYSQL_RES * as\nan argument are now methods of the result object. Deprecated functions\n(as of 3.23) are NOT implemented.\n'
__file__ = '/usr/lib/python3/dist-packages/MySQLdb/_mysql.cpython-38-x86_64-linux-gnu.so'
__name__ = 'MySQLdb._mysql'
__package__ = 'MySQLdb'
__version__ = '1.4.4'
def connect():
    'Returns a MYSQL connection object. Exclusive use of\nkeyword parameters strongly recommended. Consult the\nMySQL C API documentation for more details.\n\nhost\n  string, host to connect\n\nuser\n  string, user to connect as\n\npasswd\n  string, password to use\n\ndb\n  string, database to use\n\nport\n  integer, TCP/IP port to connect to\n\nunix_socket\n  string, location of unix_socket (UNIX-ish only)\n\nconv\n  mapping, maps MySQL FIELD_TYPE.* to Python functions which\n  convert a string to the appropriate Python type\n\nconnect_timeout\n  number of seconds to wait before the connection\n  attempt fails.\n\ncompress\n  if set, gzip compression is enabled\n\nnamed_pipe\n  if set, connect to server via named pipe (Windows only)\n\ninit_command\n  command which is run once the connection is created\n\nread_default_file\n  see the MySQL documentation for mysql_options()\n\nread_default_group\n  see the MySQL documentation for mysql_options()\n\nclient_flag\n  client flags from MySQLdb.constants.CLIENT\n\nload_infile\n  int, non-zero enables LOAD LOCAL INFILE, zero disables\n\n'
    pass

connection = _mod__mysql.connection
def debug():
    'Does a DBUG_PUSH with the given string.\nmysql_debug() uses the Fred Fish debug library.\nTo use this function, you must compile the client library to\nsupport debugging.\n'
    pass

def escape(obj, dict):
    'escape(obj, dict) -- escape any special characters in object obj\nusing mapping dict to provide quoting functions for each type.\nReturns a SQL literal string.'
    pass

def escape_string(s):
    'escape_string(s) -- quote any SQL-interpreted characters in string s.\n\nUse connection.escape_string(s), if you use it at all.\n_mysql.escape_string(s) cannot handle character sets. You are\nprobably better off using connection.escape(o) instead, since\nit will escape entire sequences as well as strings.'
    pass

def get_client_info():
    'get_client_info() -- Returns a string that represents\nthe client library version.'
    pass

result = _mod__mysql.result
def string_literal(obj):
    'string_literal(obj) -- converts object obj into a SQL string literal.\nThis means, any special SQL characters are escaped, and it is enclosed\nwithin single quotes. In other words, it performs:\n\n"\'%s\'" % escape_string(str(obj))\n\nUse connection.string_literal(obj), if you use it at all.\n_mysql.string_literal(obj) cannot handle character sets.'
    pass

version_info = _mod_builtins.tuple()
