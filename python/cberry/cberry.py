'''Wrapper for RAIO8870.h

Generated with:
/home/pi/ctypesgen-read-only/ctypesgen.py -lcberry ../../RAIO8870.h ../../tft.h /usr/local/include/bcm2835.h -o cberry.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["cberry"] = load_library("cberry")

# 1 libraries
# End libraries

# No modules

# /home/pi/lib/RAIO8870.h: 277
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'low',
    'high',
]
struct_anon_1._fields_ = [
    ('low', c_ubyte),
    ('high', c_ubyte),
]

# /home/pi/lib/RAIO8870.h: 274
class union_my_union(Union):
    pass

union_my_union.__slots__ = [
    'value',
    'split',
]
union_my_union._fields_ = [
    ('value', c_uint32),
    ('split', struct_anon_1),
]

enum_DRAW_MODES = c_int # /home/pi/lib/RAIO8870.h: 287

CIRCLE_NONFILL = 0 # /home/pi/lib/RAIO8870.h: 287

CIRCLE_FILL = (CIRCLE_NONFILL + 1) # /home/pi/lib/RAIO8870.h: 287

SQUARE_NONFILL = (CIRCLE_FILL + 1) # /home/pi/lib/RAIO8870.h: 287

SQUARE_FILL = (SQUARE_NONFILL + 1) # /home/pi/lib/RAIO8870.h: 287

LINE = (SQUARE_FILL + 1) # /home/pi/lib/RAIO8870.h: 287

# /home/pi/lib/RAIO8870.h: 292
if hasattr(_libs['cberry'], 'RAIO_init'):
    RAIO_init = _libs['cberry'].RAIO_init
    RAIO_init.argtypes = []
    RAIO_init.restype = None

# /home/pi/lib/RAIO8870.h: 295
if hasattr(_libs['cberry'], 'RAIO_power_off'):
    RAIO_power_off = _libs['cberry'].RAIO_power_off
    RAIO_power_off.argtypes = []
    RAIO_power_off.restype = None

# /home/pi/lib/RAIO8870.h: 296
if hasattr(_libs['cberry'], 'RAIO_power_on'):
    RAIO_power_on = _libs['cberry'].RAIO_power_on
    RAIO_power_on.argtypes = []
    RAIO_power_on.restype = None

# /home/pi/lib/RAIO8870.h: 300
if hasattr(_libs['cberry'], 'RAIO_SetRegister'):
    RAIO_SetRegister = _libs['cberry'].RAIO_SetRegister
    RAIO_SetRegister.argtypes = [c_uint8, c_uint8]
    RAIO_SetRegister.restype = None

# /home/pi/lib/RAIO8870.h: 305
if hasattr(_libs['cberry'], 'RAIO_SetBacklightPWMValue'):
    RAIO_SetBacklightPWMValue = _libs['cberry'].RAIO_SetBacklightPWMValue
    RAIO_SetBacklightPWMValue.argtypes = [c_uint8]
    RAIO_SetBacklightPWMValue.restype = None

# /home/pi/lib/RAIO8870.h: 310
if hasattr(_libs['cberry'], 'Active_Window'):
    Active_Window = _libs['cberry'].Active_Window
    Active_Window.argtypes = [c_uint16, c_uint16, c_uint16, c_uint16]
    Active_Window.restype = None

# /home/pi/lib/RAIO8870.h: 315
if hasattr(_libs['cberry'], 'BTE_mode'):
    BTE_mode = _libs['cberry'].BTE_mode
    BTE_mode.argtypes = [c_uint8, c_uint8]
    BTE_mode.restype = None

# /home/pi/lib/RAIO8870.h: 320
if hasattr(_libs['cberry'], 'Text_Background_Color'):
    Text_Background_Color = _libs['cberry'].Text_Background_Color
    Text_Background_Color.argtypes = [c_uint8]
    Text_Background_Color.restype = None

# /home/pi/lib/RAIO8870.h: 321
if hasattr(_libs['cberry'], 'Text_Foreground_Color'):
    Text_Foreground_Color = _libs['cberry'].Text_Foreground_Color
    Text_Foreground_Color.argtypes = [c_uint8]
    Text_Foreground_Color.restype = None

# /home/pi/lib/RAIO8870.h: 326
if hasattr(_libs['cberry'], 'RAIO_clear_screen'):
    RAIO_clear_screen = _libs['cberry'].RAIO_clear_screen
    RAIO_clear_screen.argtypes = []
    RAIO_clear_screen.restype = None

# /home/pi/lib/RAIO8870.h: 331
if hasattr(_libs['cberry'], 'Set_Geometric_Coordinate'):
    Set_Geometric_Coordinate = _libs['cberry'].Set_Geometric_Coordinate
    Set_Geometric_Coordinate.argtypes = [c_uint16, c_uint16, c_uint16, c_uint16]
    Set_Geometric_Coordinate.restype = None

# /home/pi/lib/RAIO8870.h: 332
if hasattr(_libs['cberry'], 'Set_Geometric_Coordinate_circle'):
    Set_Geometric_Coordinate_circle = _libs['cberry'].Set_Geometric_Coordinate_circle
    Set_Geometric_Coordinate_circle.argtypes = [c_uint16, c_uint16, c_uint8]
    Set_Geometric_Coordinate_circle.restype = None

# /home/pi/lib/RAIO8870.h: 337
if hasattr(_libs['cberry'], 'RAIO_set_cursor'):
    RAIO_set_cursor = _libs['cberry'].RAIO_set_cursor
    RAIO_set_cursor.argtypes = [c_uint16, c_uint16]
    RAIO_set_cursor.restype = None

# /home/pi/lib/RAIO8870.h: 342
if hasattr(_libs['cberry'], 'RAIO_Write_Picture'):
    RAIO_Write_Picture = _libs['cberry'].RAIO_Write_Picture
    RAIO_Write_Picture.argtypes = [POINTER(c_uint16), c_uint32]
    RAIO_Write_Picture.restype = None

# /home/pi/lib/RAIO8870.h: 347
if hasattr(_libs['cberry'], 'RAIO_StartDrawing'):
    RAIO_StartDrawing = _libs['cberry'].RAIO_StartDrawing
    RAIO_StartDrawing.argtypes = [c_int16]
    RAIO_StartDrawing.restype = None

# /home/pi/lib/RAIO8870.h: 352
if hasattr(_libs['cberry'], 'Draw_Line'):
    Draw_Line = _libs['cberry'].Draw_Line
    Draw_Line.argtypes = [c_uint16, c_uint16, c_uint16, c_uint16]
    Draw_Line.restype = None

# /home/pi/lib/RAIO8870.h: 353
if hasattr(_libs['cberry'], 'Draw_Square'):
    Draw_Square = _libs['cberry'].Draw_Square
    Draw_Square.argtypes = [c_uint16, c_uint16, c_uint16, c_uint16]
    Draw_Square.restype = None

# /home/pi/lib/RAIO8870.h: 358
if hasattr(_libs['cberry'], 'RAIO_print_text'):
    RAIO_print_text = _libs['cberry'].RAIO_print_text
    RAIO_print_text.argtypes = [c_uint16, c_uint16, POINTER(c_ubyte), c_uint8, c_uint8]
    RAIO_print_text.restype = None

# /home/pi/lib/RAIO8870.h: 363
if hasattr(_libs['cberry'], 'RAIO_SetFontSizeFactor'):
    RAIO_SetFontSizeFactor = _libs['cberry'].RAIO_SetFontSizeFactor
    RAIO_SetFontSizeFactor.argtypes = [c_uint8]
    RAIO_SetFontSizeFactor.restype = None

# /home/pi/lib/tft.h: 79
for _lib in _libs.values():
    try:
        number = (union_my_union).in_dll(_lib, 'number')
        break
    except:
        pass

# /home/pi/lib/tft.h: 84
if hasattr(_libs['cberry'], 'TFT_init_board'):
    TFT_init_board = _libs['cberry'].TFT_init_board
    TFT_init_board.argtypes = []
    TFT_init_board.restype = None

# /home/pi/lib/tft.h: 89
if hasattr(_libs['cberry'], 'TFT_hard_reset'):
    TFT_hard_reset = _libs['cberry'].TFT_hard_reset
    TFT_hard_reset.argtypes = []
    TFT_hard_reset.restype = None

# /home/pi/lib/tft.h: 94
if hasattr(_libs['cberry'], 'TFT_wait_for_raio'):
    TFT_wait_for_raio = _libs['cberry'].TFT_wait_for_raio
    TFT_wait_for_raio.argtypes = []
    TFT_wait_for_raio.restype = None

# /home/pi/lib/tft.h: 99
if hasattr(_libs['cberry'], 'TFT_RegWrite'):
    TFT_RegWrite = _libs['cberry'].TFT_RegWrite
    TFT_RegWrite.argtypes = [c_uint16]
    TFT_RegWrite.restype = None

# /home/pi/lib/tft.h: 104
if hasattr(_libs['cberry'], 'TFT_DataWrite'):
    TFT_DataWrite = _libs['cberry'].TFT_DataWrite
    TFT_DataWrite.argtypes = [c_uint16]
    TFT_DataWrite.restype = None

# /home/pi/lib/tft.h: 109
if hasattr(_libs['cberry'], 'TFT_DataMultiWrite'):
    TFT_DataMultiWrite = _libs['cberry'].TFT_DataMultiWrite
    TFT_DataMultiWrite.argtypes = [POINTER(c_uint16), c_uint32]
    TFT_DataMultiWrite.restype = None

# /usr/local/include/bcm2835.h: 355
try:
    bcm2835_st = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_st')
except:
    pass

# /usr/local/include/bcm2835.h: 359
try:
    bcm2835_gpio = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_gpio')
except:
    pass

# /usr/local/include/bcm2835.h: 363
try:
    bcm2835_pwm = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_pwm')
except:
    pass

# /usr/local/include/bcm2835.h: 367
try:
    bcm2835_clk = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_clk')
except:
    pass

# /usr/local/include/bcm2835.h: 371
try:
    bcm2835_pads = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_pads')
except:
    pass

# /usr/local/include/bcm2835.h: 375
try:
    bcm2835_spi0 = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_spi0')
except:
    pass

# /usr/local/include/bcm2835.h: 379
try:
    bcm2835_bsc0 = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_bsc0')
except:
    pass

# /usr/local/include/bcm2835.h: 383
try:
    bcm2835_bsc1 = (POINTER(c_uint32)).in_dll(_libs['cberry'], 'bcm2835_bsc1')
except:
    pass

enum_anon_2 = c_int # /usr/local/include/bcm2835.h: 474

BCM2835_PAD_GROUP_GPIO_0_27 = 0 # /usr/local/include/bcm2835.h: 474

BCM2835_PAD_GROUP_GPIO_28_45 = 1 # /usr/local/include/bcm2835.h: 474

BCM2835_PAD_GROUP_GPIO_46_53 = 2 # /usr/local/include/bcm2835.h: 474

bcm2835PadGroup = enum_anon_2 # /usr/local/include/bcm2835.h: 474

enum_anon_3 = c_int # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_03 = 0 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_05 = 1 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_07 = 4 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_08 = 14 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_10 = 15 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_11 = 17 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_12 = 18 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_13 = 21 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_15 = 22 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_16 = 23 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_18 = 24 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_19 = 10 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_21 = 9 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_22 = 25 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_23 = 11 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_24 = 8 # /usr/local/include/bcm2835.h: 531

RPI_GPIO_P1_26 = 7 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_03 = 2 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_05 = 3 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_07 = 4 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_08 = 14 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_10 = 15 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_11 = 17 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_12 = 18 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_13 = 27 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_15 = 22 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_16 = 23 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_18 = 24 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_19 = 10 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_21 = 9 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_22 = 25 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_23 = 11 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_24 = 8 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P1_26 = 7 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P5_03 = 28 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P5_04 = 29 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P5_05 = 30 # /usr/local/include/bcm2835.h: 531

RPI_V2_GPIO_P5_06 = 31 # /usr/local/include/bcm2835.h: 531

RPiGPIOPin = enum_anon_3 # /usr/local/include/bcm2835.h: 531

enum_anon_4 = c_int # /usr/local/include/bcm2835.h: 577

BCM2835_SPI_BIT_ORDER_LSBFIRST = 0 # /usr/local/include/bcm2835.h: 577

BCM2835_SPI_BIT_ORDER_MSBFIRST = 1 # /usr/local/include/bcm2835.h: 577

bcm2835SPIBitOrder = enum_anon_4 # /usr/local/include/bcm2835.h: 577

enum_anon_5 = c_int # /usr/local/include/bcm2835.h: 587

BCM2835_SPI_MODE0 = 0 # /usr/local/include/bcm2835.h: 587

BCM2835_SPI_MODE1 = 1 # /usr/local/include/bcm2835.h: 587

BCM2835_SPI_MODE2 = 2 # /usr/local/include/bcm2835.h: 587

BCM2835_SPI_MODE3 = 3 # /usr/local/include/bcm2835.h: 587

bcm2835SPIMode = enum_anon_5 # /usr/local/include/bcm2835.h: 587

enum_anon_6 = c_int # /usr/local/include/bcm2835.h: 597

BCM2835_SPI_CS0 = 0 # /usr/local/include/bcm2835.h: 597

BCM2835_SPI_CS1 = 1 # /usr/local/include/bcm2835.h: 597

BCM2835_SPI_CS2 = 2 # /usr/local/include/bcm2835.h: 597

BCM2835_SPI_CS_NONE = 3 # /usr/local/include/bcm2835.h: 597

bcm2835SPIChipSelect = enum_anon_6 # /usr/local/include/bcm2835.h: 597

enum_anon_7 = c_int # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_65536 = 0 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_32768 = 32768 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_16384 = 16384 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_8192 = 8192 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_4096 = 4096 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_2048 = 2048 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_1024 = 1024 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_512 = 512 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_256 = 256 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_128 = 128 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_64 = 64 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_32 = 32 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_16 = 16 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_8 = 8 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_4 = 4 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_2 = 2 # /usr/local/include/bcm2835.h: 624

BCM2835_SPI_CLOCK_DIVIDER_1 = 1 # /usr/local/include/bcm2835.h: 624

bcm2835SPIClockDivider = enum_anon_7 # /usr/local/include/bcm2835.h: 624

enum_anon_8 = c_int # /usr/local/include/bcm2835.h: 671

BCM2835_I2C_CLOCK_DIVIDER_2500 = 2500 # /usr/local/include/bcm2835.h: 671

BCM2835_I2C_CLOCK_DIVIDER_626 = 626 # /usr/local/include/bcm2835.h: 671

BCM2835_I2C_CLOCK_DIVIDER_150 = 150 # /usr/local/include/bcm2835.h: 671

BCM2835_I2C_CLOCK_DIVIDER_148 = 148 # /usr/local/include/bcm2835.h: 671

bcm2835I2CClockDivider = enum_anon_8 # /usr/local/include/bcm2835.h: 671

enum_anon_9 = c_int # /usr/local/include/bcm2835.h: 681

BCM2835_I2C_REASON_OK = 0 # /usr/local/include/bcm2835.h: 681

BCM2835_I2C_REASON_ERROR_NACK = 1 # /usr/local/include/bcm2835.h: 681

BCM2835_I2C_REASON_ERROR_CLKT = 2 # /usr/local/include/bcm2835.h: 681

BCM2835_I2C_REASON_ERROR_DATA = 4 # /usr/local/include/bcm2835.h: 681

bcm2835I2CReasonCodes = enum_anon_9 # /usr/local/include/bcm2835.h: 681

enum_anon_10 = c_int # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_32768 = 32768 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_16384 = 16384 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_8192 = 8192 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_4096 = 4096 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_2048 = 2048 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_1024 = 1024 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_512 = 512 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_256 = 256 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_128 = 128 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_64 = 64 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_32 = 32 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_16 = 16 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_8 = 8 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_4 = 4 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_2 = 2 # /usr/local/include/bcm2835.h: 755

BCM2835_PWM_CLOCK_DIVIDER_1 = 1 # /usr/local/include/bcm2835.h: 755

bcm2835PWMClockDivider = enum_anon_10 # /usr/local/include/bcm2835.h: 755

# /usr/local/include/bcm2835.h: 779
if hasattr(_libs['cberry'], 'bcm2835_init'):
    bcm2835_init = _libs['cberry'].bcm2835_init
    bcm2835_init.argtypes = []
    bcm2835_init.restype = c_int

# /usr/local/include/bcm2835.h: 783
if hasattr(_libs['cberry'], 'bcm2835_close'):
    bcm2835_close = _libs['cberry'].bcm2835_close
    bcm2835_close.argtypes = []
    bcm2835_close.restype = c_int

# /usr/local/include/bcm2835.h: 791
if hasattr(_libs['cberry'], 'bcm2835_set_debug'):
    bcm2835_set_debug = _libs['cberry'].bcm2835_set_debug
    bcm2835_set_debug.argtypes = [c_uint8]
    bcm2835_set_debug.restype = None

# /usr/local/include/bcm2835.h: 807
if hasattr(_libs['cberry'], 'bcm2835_peri_read'):
    bcm2835_peri_read = _libs['cberry'].bcm2835_peri_read
    bcm2835_peri_read.argtypes = [POINTER(c_uint32)]
    bcm2835_peri_read.restype = c_uint32

# /usr/local/include/bcm2835.h: 816
if hasattr(_libs['cberry'], 'bcm2835_peri_read_nb'):
    bcm2835_peri_read_nb = _libs['cberry'].bcm2835_peri_read_nb
    bcm2835_peri_read_nb.argtypes = [POINTER(c_uint32)]
    bcm2835_peri_read_nb.restype = c_uint32

# /usr/local/include/bcm2835.h: 825
if hasattr(_libs['cberry'], 'bcm2835_peri_write'):
    bcm2835_peri_write = _libs['cberry'].bcm2835_peri_write
    bcm2835_peri_write.argtypes = [POINTER(c_uint32), c_uint32]
    bcm2835_peri_write.restype = None

# /usr/local/include/bcm2835.h: 833
if hasattr(_libs['cberry'], 'bcm2835_peri_write_nb'):
    bcm2835_peri_write_nb = _libs['cberry'].bcm2835_peri_write_nb
    bcm2835_peri_write_nb.argtypes = [POINTER(c_uint32), c_uint32]
    bcm2835_peri_write_nb.restype = None

# /usr/local/include/bcm2835.h: 846
if hasattr(_libs['cberry'], 'bcm2835_peri_set_bits'):
    bcm2835_peri_set_bits = _libs['cberry'].bcm2835_peri_set_bits
    bcm2835_peri_set_bits.argtypes = [POINTER(c_uint32), c_uint32, c_uint32]
    bcm2835_peri_set_bits.restype = None

# /usr/local/include/bcm2835.h: 858
if hasattr(_libs['cberry'], 'bcm2835_gpio_fsel'):
    bcm2835_gpio_fsel = _libs['cberry'].bcm2835_gpio_fsel
    bcm2835_gpio_fsel.argtypes = [c_uint8, c_uint8]
    bcm2835_gpio_fsel.restype = None

# /usr/local/include/bcm2835.h: 864
if hasattr(_libs['cberry'], 'bcm2835_gpio_set'):
    bcm2835_gpio_set = _libs['cberry'].bcm2835_gpio_set
    bcm2835_gpio_set.argtypes = [c_uint8]
    bcm2835_gpio_set.restype = None

# /usr/local/include/bcm2835.h: 870
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr'):
    bcm2835_gpio_clr = _libs['cberry'].bcm2835_gpio_clr
    bcm2835_gpio_clr.argtypes = [c_uint8]
    bcm2835_gpio_clr.restype = None

# /usr/local/include/bcm2835.h: 876
if hasattr(_libs['cberry'], 'bcm2835_gpio_set_multi'):
    bcm2835_gpio_set_multi = _libs['cberry'].bcm2835_gpio_set_multi
    bcm2835_gpio_set_multi.argtypes = [c_uint32]
    bcm2835_gpio_set_multi.restype = None

# /usr/local/include/bcm2835.h: 882
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_multi'):
    bcm2835_gpio_clr_multi = _libs['cberry'].bcm2835_gpio_clr_multi
    bcm2835_gpio_clr_multi.argtypes = [c_uint32]
    bcm2835_gpio_clr_multi.restype = None

# /usr/local/include/bcm2835.h: 889
if hasattr(_libs['cberry'], 'bcm2835_gpio_lev'):
    bcm2835_gpio_lev = _libs['cberry'].bcm2835_gpio_lev
    bcm2835_gpio_lev.argtypes = [c_uint8]
    bcm2835_gpio_lev.restype = c_uint8

# /usr/local/include/bcm2835.h: 898
if hasattr(_libs['cberry'], 'bcm2835_gpio_eds'):
    bcm2835_gpio_eds = _libs['cberry'].bcm2835_gpio_eds
    bcm2835_gpio_eds.argtypes = [c_uint8]
    bcm2835_gpio_eds.restype = c_uint8

# /usr/local/include/bcm2835.h: 904
if hasattr(_libs['cberry'], 'bcm2835_gpio_set_eds'):
    bcm2835_gpio_set_eds = _libs['cberry'].bcm2835_gpio_set_eds
    bcm2835_gpio_set_eds.argtypes = [c_uint8]
    bcm2835_gpio_set_eds.restype = None

# /usr/local/include/bcm2835.h: 913
if hasattr(_libs['cberry'], 'bcm2835_gpio_ren'):
    bcm2835_gpio_ren = _libs['cberry'].bcm2835_gpio_ren
    bcm2835_gpio_ren.argtypes = [c_uint8]
    bcm2835_gpio_ren.restype = None

# /usr/local/include/bcm2835.h: 917
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_ren'):
    bcm2835_gpio_clr_ren = _libs['cberry'].bcm2835_gpio_clr_ren
    bcm2835_gpio_clr_ren.argtypes = [c_uint8]
    bcm2835_gpio_clr_ren.restype = None

# /usr/local/include/bcm2835.h: 926
if hasattr(_libs['cberry'], 'bcm2835_gpio_fen'):
    bcm2835_gpio_fen = _libs['cberry'].bcm2835_gpio_fen
    bcm2835_gpio_fen.argtypes = [c_uint8]
    bcm2835_gpio_fen.restype = None

# /usr/local/include/bcm2835.h: 930
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_fen'):
    bcm2835_gpio_clr_fen = _libs['cberry'].bcm2835_gpio_clr_fen
    bcm2835_gpio_clr_fen.argtypes = [c_uint8]
    bcm2835_gpio_clr_fen.restype = None

# /usr/local/include/bcm2835.h: 935
if hasattr(_libs['cberry'], 'bcm2835_gpio_hen'):
    bcm2835_gpio_hen = _libs['cberry'].bcm2835_gpio_hen
    bcm2835_gpio_hen.argtypes = [c_uint8]
    bcm2835_gpio_hen.restype = None

# /usr/local/include/bcm2835.h: 939
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_hen'):
    bcm2835_gpio_clr_hen = _libs['cberry'].bcm2835_gpio_clr_hen
    bcm2835_gpio_clr_hen.argtypes = [c_uint8]
    bcm2835_gpio_clr_hen.restype = None

# /usr/local/include/bcm2835.h: 944
if hasattr(_libs['cberry'], 'bcm2835_gpio_len'):
    bcm2835_gpio_len = _libs['cberry'].bcm2835_gpio_len
    bcm2835_gpio_len.argtypes = [c_uint8]
    bcm2835_gpio_len.restype = None

# /usr/local/include/bcm2835.h: 948
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_len'):
    bcm2835_gpio_clr_len = _libs['cberry'].bcm2835_gpio_clr_len
    bcm2835_gpio_clr_len.argtypes = [c_uint8]
    bcm2835_gpio_clr_len.restype = None

# /usr/local/include/bcm2835.h: 955
if hasattr(_libs['cberry'], 'bcm2835_gpio_aren'):
    bcm2835_gpio_aren = _libs['cberry'].bcm2835_gpio_aren
    bcm2835_gpio_aren.argtypes = [c_uint8]
    bcm2835_gpio_aren.restype = None

# /usr/local/include/bcm2835.h: 959
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_aren'):
    bcm2835_gpio_clr_aren = _libs['cberry'].bcm2835_gpio_clr_aren
    bcm2835_gpio_clr_aren.argtypes = [c_uint8]
    bcm2835_gpio_clr_aren.restype = None

# /usr/local/include/bcm2835.h: 966
if hasattr(_libs['cberry'], 'bcm2835_gpio_afen'):
    bcm2835_gpio_afen = _libs['cberry'].bcm2835_gpio_afen
    bcm2835_gpio_afen.argtypes = [c_uint8]
    bcm2835_gpio_afen.restype = None

# /usr/local/include/bcm2835.h: 970
if hasattr(_libs['cberry'], 'bcm2835_gpio_clr_afen'):
    bcm2835_gpio_clr_afen = _libs['cberry'].bcm2835_gpio_clr_afen
    bcm2835_gpio_clr_afen.argtypes = [c_uint8]
    bcm2835_gpio_clr_afen.restype = None

# /usr/local/include/bcm2835.h: 977
if hasattr(_libs['cberry'], 'bcm2835_gpio_pud'):
    bcm2835_gpio_pud = _libs['cberry'].bcm2835_gpio_pud
    bcm2835_gpio_pud.argtypes = [c_uint8]
    bcm2835_gpio_pud.restype = None

# /usr/local/include/bcm2835.h: 984
if hasattr(_libs['cberry'], 'bcm2835_gpio_pudclk'):
    bcm2835_gpio_pudclk = _libs['cberry'].bcm2835_gpio_pudclk
    bcm2835_gpio_pudclk.argtypes = [c_uint8, c_uint8]
    bcm2835_gpio_pudclk.restype = None

# /usr/local/include/bcm2835.h: 989
if hasattr(_libs['cberry'], 'bcm2835_gpio_pad'):
    bcm2835_gpio_pad = _libs['cberry'].bcm2835_gpio_pad
    bcm2835_gpio_pad.argtypes = [c_uint8]
    bcm2835_gpio_pad.restype = c_uint32

# /usr/local/include/bcm2835.h: 996
if hasattr(_libs['cberry'], 'bcm2835_gpio_set_pad'):
    bcm2835_gpio_set_pad = _libs['cberry'].bcm2835_gpio_set_pad
    bcm2835_gpio_set_pad.argtypes = [c_uint8, c_uint32]
    bcm2835_gpio_set_pad.restype = None

# /usr/local/include/bcm2835.h: 1007
if hasattr(_libs['cberry'], 'bcm2835_delay'):
    bcm2835_delay = _libs['cberry'].bcm2835_delay
    bcm2835_delay.argtypes = [c_uint]
    bcm2835_delay.restype = None

# /usr/local/include/bcm2835.h: 1021
if hasattr(_libs['cberry'], 'bcm2835_delayMicroseconds'):
    bcm2835_delayMicroseconds = _libs['cberry'].bcm2835_delayMicroseconds
    bcm2835_delayMicroseconds.argtypes = [c_uint64]
    bcm2835_delayMicroseconds.restype = None

# /usr/local/include/bcm2835.h: 1026
if hasattr(_libs['cberry'], 'bcm2835_gpio_write'):
    bcm2835_gpio_write = _libs['cberry'].bcm2835_gpio_write
    bcm2835_gpio_write.argtypes = [c_uint8, c_uint8]
    bcm2835_gpio_write.restype = None

# /usr/local/include/bcm2835.h: 1031
if hasattr(_libs['cberry'], 'bcm2835_gpio_write_multi'):
    bcm2835_gpio_write_multi = _libs['cberry'].bcm2835_gpio_write_multi
    bcm2835_gpio_write_multi.argtypes = [c_uint32, c_uint8]
    bcm2835_gpio_write_multi.restype = None

# /usr/local/include/bcm2835.h: 1036
if hasattr(_libs['cberry'], 'bcm2835_gpio_write_mask'):
    bcm2835_gpio_write_mask = _libs['cberry'].bcm2835_gpio_write_mask
    bcm2835_gpio_write_mask.argtypes = [c_uint32, c_uint32]
    bcm2835_gpio_write_mask.restype = None

# /usr/local/include/bcm2835.h: 1042
if hasattr(_libs['cberry'], 'bcm2835_gpio_set_pud'):
    bcm2835_gpio_set_pud = _libs['cberry'].bcm2835_gpio_set_pud
    bcm2835_gpio_set_pud.argtypes = [c_uint8, c_uint8]
    bcm2835_gpio_set_pud.restype = None

# /usr/local/include/bcm2835.h: 1057
if hasattr(_libs['cberry'], 'bcm2835_spi_begin'):
    bcm2835_spi_begin = _libs['cberry'].bcm2835_spi_begin
    bcm2835_spi_begin.argtypes = []
    bcm2835_spi_begin.restype = None

# /usr/local/include/bcm2835.h: 1062
if hasattr(_libs['cberry'], 'bcm2835_spi_end'):
    bcm2835_spi_end = _libs['cberry'].bcm2835_spi_end
    bcm2835_spi_end.argtypes = []
    bcm2835_spi_end.restype = None

# /usr/local/include/bcm2835.h: 1069
if hasattr(_libs['cberry'], 'bcm2835_spi_setBitOrder'):
    bcm2835_spi_setBitOrder = _libs['cberry'].bcm2835_spi_setBitOrder
    bcm2835_spi_setBitOrder.argtypes = [c_uint8]
    bcm2835_spi_setBitOrder.restype = None

# /usr/local/include/bcm2835.h: 1075
if hasattr(_libs['cberry'], 'bcm2835_spi_setClockDivider'):
    bcm2835_spi_setClockDivider = _libs['cberry'].bcm2835_spi_setClockDivider
    bcm2835_spi_setClockDivider.argtypes = [c_uint16]
    bcm2835_spi_setClockDivider.restype = None

# /usr/local/include/bcm2835.h: 1081
if hasattr(_libs['cberry'], 'bcm2835_spi_setDataMode'):
    bcm2835_spi_setDataMode = _libs['cberry'].bcm2835_spi_setDataMode
    bcm2835_spi_setDataMode.argtypes = [c_uint8]
    bcm2835_spi_setDataMode.restype = None

# /usr/local/include/bcm2835.h: 1088
if hasattr(_libs['cberry'], 'bcm2835_spi_chipSelect'):
    bcm2835_spi_chipSelect = _libs['cberry'].bcm2835_spi_chipSelect
    bcm2835_spi_chipSelect.argtypes = [c_uint8]
    bcm2835_spi_chipSelect.restype = None

# /usr/local/include/bcm2835.h: 1097
if hasattr(_libs['cberry'], 'bcm2835_spi_setChipSelectPolarity'):
    bcm2835_spi_setChipSelectPolarity = _libs['cberry'].bcm2835_spi_setChipSelectPolarity
    bcm2835_spi_setChipSelectPolarity.argtypes = [c_uint8, c_uint8]
    bcm2835_spi_setChipSelectPolarity.restype = None

# /usr/local/include/bcm2835.h: 1108
if hasattr(_libs['cberry'], 'bcm2835_spi_transfer'):
    bcm2835_spi_transfer = _libs['cberry'].bcm2835_spi_transfer
    bcm2835_spi_transfer.argtypes = [c_uint8]
    bcm2835_spi_transfer.restype = c_uint8

# /usr/local/include/bcm2835.h: 1120
if hasattr(_libs['cberry'], 'bcm2835_spi_transfernb'):
    bcm2835_spi_transfernb = _libs['cberry'].bcm2835_spi_transfernb
    bcm2835_spi_transfernb.argtypes = [String, String, c_uint32]
    bcm2835_spi_transfernb.restype = None

# /usr/local/include/bcm2835.h: 1128
if hasattr(_libs['cberry'], 'bcm2835_spi_transfern'):
    bcm2835_spi_transfern = _libs['cberry'].bcm2835_spi_transfern
    bcm2835_spi_transfern.argtypes = [String, c_uint32]
    bcm2835_spi_transfern.restype = None

# /usr/local/include/bcm2835.h: 1135
if hasattr(_libs['cberry'], 'bcm2835_spi_writenb'):
    bcm2835_spi_writenb = _libs['cberry'].bcm2835_spi_writenb
    bcm2835_spi_writenb.argtypes = [String, c_uint32]
    bcm2835_spi_writenb.restype = None

# /usr/local/include/bcm2835.h: 1150
if hasattr(_libs['cberry'], 'bcm2835_i2c_begin'):
    bcm2835_i2c_begin = _libs['cberry'].bcm2835_i2c_begin
    bcm2835_i2c_begin.argtypes = []
    bcm2835_i2c_begin.restype = None

# /usr/local/include/bcm2835.h: 1155
if hasattr(_libs['cberry'], 'bcm2835_i2c_end'):
    bcm2835_i2c_end = _libs['cberry'].bcm2835_i2c_end
    bcm2835_i2c_end.argtypes = []
    bcm2835_i2c_end.restype = None

# /usr/local/include/bcm2835.h: 1159
if hasattr(_libs['cberry'], 'bcm2835_i2c_setSlaveAddress'):
    bcm2835_i2c_setSlaveAddress = _libs['cberry'].bcm2835_i2c_setSlaveAddress
    bcm2835_i2c_setSlaveAddress.argtypes = [c_uint8]
    bcm2835_i2c_setSlaveAddress.restype = None

# /usr/local/include/bcm2835.h: 1164
if hasattr(_libs['cberry'], 'bcm2835_i2c_setClockDivider'):
    bcm2835_i2c_setClockDivider = _libs['cberry'].bcm2835_i2c_setClockDivider
    bcm2835_i2c_setClockDivider.argtypes = [c_uint16]
    bcm2835_i2c_setClockDivider.restype = None

# /usr/local/include/bcm2835.h: 1171
if hasattr(_libs['cberry'], 'bcm2835_i2c_set_baudrate'):
    bcm2835_i2c_set_baudrate = _libs['cberry'].bcm2835_i2c_set_baudrate
    bcm2835_i2c_set_baudrate.argtypes = [c_uint32]
    bcm2835_i2c_set_baudrate.restype = None

# /usr/local/include/bcm2835.h: 1178
if hasattr(_libs['cberry'], 'bcm2835_i2c_write'):
    bcm2835_i2c_write = _libs['cberry'].bcm2835_i2c_write
    bcm2835_i2c_write.argtypes = [String, c_uint32]
    bcm2835_i2c_write.restype = c_uint8

# /usr/local/include/bcm2835.h: 1185
if hasattr(_libs['cberry'], 'bcm2835_i2c_read'):
    bcm2835_i2c_read = _libs['cberry'].bcm2835_i2c_read
    bcm2835_i2c_read.argtypes = [String, c_uint32]
    bcm2835_i2c_read.restype = c_uint8

# /usr/local/include/bcm2835.h: 1200
if hasattr(_libs['cberry'], 'bcm2835_i2c_read_register_rs'):
    bcm2835_i2c_read_register_rs = _libs['cberry'].bcm2835_i2c_read_register_rs
    bcm2835_i2c_read_register_rs.argtypes = [String, String, c_uint32]
    bcm2835_i2c_read_register_rs.restype = c_uint8

# /usr/local/include/bcm2835.h: 1211
if hasattr(_libs['cberry'], 'bcm2835_i2c_write_read_rs'):
    bcm2835_i2c_write_read_rs = _libs['cberry'].bcm2835_i2c_write_read_rs
    bcm2835_i2c_write_read_rs.argtypes = [String, c_uint32, String, c_uint32]
    bcm2835_i2c_write_read_rs.restype = c_uint8

# /usr/local/include/bcm2835.h: 1221
if hasattr(_libs['cberry'], 'bcm2835_st_read'):
    bcm2835_st_read = _libs['cberry'].bcm2835_st_read
    bcm2835_st_read.argtypes = []
    bcm2835_st_read.restype = c_uint64

# /usr/local/include/bcm2835.h: 1226
if hasattr(_libs['cberry'], 'bcm2835_st_delay'):
    bcm2835_st_delay = _libs['cberry'].bcm2835_st_delay
    bcm2835_st_delay.argtypes = [c_uint64, c_uint64]
    bcm2835_st_delay.restype = None

# /usr/local/include/bcm2835.h: 1241
if hasattr(_libs['cberry'], 'bcm2835_pwm_set_clock'):
    bcm2835_pwm_set_clock = _libs['cberry'].bcm2835_pwm_set_clock
    bcm2835_pwm_set_clock.argtypes = [c_uint32]
    bcm2835_pwm_set_clock.restype = None

# /usr/local/include/bcm2835.h: 1248
if hasattr(_libs['cberry'], 'bcm2835_pwm_set_mode'):
    bcm2835_pwm_set_mode = _libs['cberry'].bcm2835_pwm_set_mode
    bcm2835_pwm_set_mode.argtypes = [c_uint8, c_uint8, c_uint8]
    bcm2835_pwm_set_mode.restype = None

# /usr/local/include/bcm2835.h: 1254
if hasattr(_libs['cberry'], 'bcm2835_pwm_set_range'):
    bcm2835_pwm_set_range = _libs['cberry'].bcm2835_pwm_set_range
    bcm2835_pwm_set_range.argtypes = [c_uint8, c_uint32]
    bcm2835_pwm_set_range.restype = None

# /usr/local/include/bcm2835.h: 1261
if hasattr(_libs['cberry'], 'bcm2835_pwm_set_data'):
    bcm2835_pwm_set_data = _libs['cberry'].bcm2835_pwm_set_data
    bcm2835_pwm_set_data.argtypes = [c_uint8, c_uint32]
    bcm2835_pwm_set_data.restype = None

# /home/pi/lib/RAIO8870.h: 71
try:
    DISPLAY_WIDTH = 320
except:
    pass

# /home/pi/lib/RAIO8870.h: 72
try:
    DISPLAY_HEIGHT = 240
except:
    pass

# /home/pi/lib/RAIO8870.h: 73
try:
    PICTURE_PIXELS = (DISPLAY_WIDTH * DISPLAY_HEIGHT)
except:
    pass

# /home/pi/lib/RAIO8870.h: 77
try:
    PCOD = 0
except:
    pass

# /home/pi/lib/RAIO8870.h: 78
try:
    PWRR = 1
except:
    pass

# /home/pi/lib/RAIO8870.h: 79
try:
    MRWC = 2
except:
    pass

# /home/pi/lib/RAIO8870.h: 80
try:
    PCLK = 4
except:
    pass

# /home/pi/lib/RAIO8870.h: 82
try:
    SYSR = 16
except:
    pass

# /home/pi/lib/RAIO8870.h: 83
try:
    DRGB = 17
except:
    pass

# /home/pi/lib/RAIO8870.h: 84
try:
    IOCR = 18
except:
    pass

# /home/pi/lib/RAIO8870.h: 85
try:
    IODR = 19
except:
    pass

# /home/pi/lib/RAIO8870.h: 87
try:
    HDWR = 20
except:
    pass

# /home/pi/lib/RAIO8870.h: 88
try:
    HNDFTR = 21
except:
    pass

# /home/pi/lib/RAIO8870.h: 89
try:
    HNDR = 22
except:
    pass

# /home/pi/lib/RAIO8870.h: 90
try:
    HSTR = 23
except:
    pass

# /home/pi/lib/RAIO8870.h: 91
try:
    HPWR = 24
except:
    pass

# /home/pi/lib/RAIO8870.h: 93
try:
    VDHR0 = 25
except:
    pass

# /home/pi/lib/RAIO8870.h: 94
try:
    VDHR1 = 26
except:
    pass

# /home/pi/lib/RAIO8870.h: 95
try:
    VNDR0 = 27
except:
    pass

# /home/pi/lib/RAIO8870.h: 96
try:
    VNDR1 = 28
except:
    pass

# /home/pi/lib/RAIO8870.h: 97
try:
    VSTR0 = 29
except:
    pass

# /home/pi/lib/RAIO8870.h: 98
try:
    VSTR1 = 30
except:
    pass

# /home/pi/lib/RAIO8870.h: 99
try:
    VPWR = 31
except:
    pass

# /home/pi/lib/RAIO8870.h: 101
try:
    DPCR = 32
except:
    pass

# /home/pi/lib/RAIO8870.h: 102
try:
    FNCR0 = 33
except:
    pass

# /home/pi/lib/RAIO8870.h: 103
try:
    FNCR1 = 34
except:
    pass

# /home/pi/lib/RAIO8870.h: 104
try:
    CGSR = 35
except:
    pass

# /home/pi/lib/RAIO8870.h: 105
try:
    HOFS0 = 36
except:
    pass

# /home/pi/lib/RAIO8870.h: 106
try:
    HOFS1 = 37
except:
    pass

# /home/pi/lib/RAIO8870.h: 107
try:
    VOFS0 = 38
except:
    pass

# /home/pi/lib/RAIO8870.h: 108
try:
    VOFS1 = 39
except:
    pass

# /home/pi/lib/RAIO8870.h: 109
try:
    ROMS = 40
except:
    pass

# /home/pi/lib/RAIO8870.h: 111
try:
    FLDR = 41
except:
    pass

# /home/pi/lib/RAIO8870.h: 113
try:
    HSAW0 = 48
except:
    pass

# /home/pi/lib/RAIO8870.h: 114
try:
    HSAW1 = 49
except:
    pass

# /home/pi/lib/RAIO8870.h: 115
try:
    VSAW0 = 50
except:
    pass

# /home/pi/lib/RAIO8870.h: 116
try:
    VSAW1 = 51
except:
    pass

# /home/pi/lib/RAIO8870.h: 117
try:
    HEAW0 = 52
except:
    pass

# /home/pi/lib/RAIO8870.h: 118
try:
    HEAW1 = 53
except:
    pass

# /home/pi/lib/RAIO8870.h: 119
try:
    VEAW0 = 54
except:
    pass

# /home/pi/lib/RAIO8870.h: 120
try:
    VEAW1 = 55
except:
    pass

# /home/pi/lib/RAIO8870.h: 121
try:
    HSSW0 = 56
except:
    pass

# /home/pi/lib/RAIO8870.h: 122
try:
    HSSW1 = 57
except:
    pass

# /home/pi/lib/RAIO8870.h: 123
try:
    VSSW0 = 58
except:
    pass

# /home/pi/lib/RAIO8870.h: 124
try:
    VSSW1 = 59
except:
    pass

# /home/pi/lib/RAIO8870.h: 125
try:
    HESW0 = 60
except:
    pass

# /home/pi/lib/RAIO8870.h: 126
try:
    HESW1 = 61
except:
    pass

# /home/pi/lib/RAIO8870.h: 127
try:
    VESW0 = 62
except:
    pass

# /home/pi/lib/RAIO8870.h: 128
try:
    VESW1 = 63
except:
    pass

# /home/pi/lib/RAIO8870.h: 130
try:
    MWCR0 = 64
except:
    pass

# /home/pi/lib/RAIO8870.h: 131
try:
    MWCR1 = 65
except:
    pass

# /home/pi/lib/RAIO8870.h: 132
try:
    TFCR = 66
except:
    pass

# /home/pi/lib/RAIO8870.h: 133
try:
    TBCR = 67
except:
    pass

# /home/pi/lib/RAIO8870.h: 134
try:
    BTCR = 68
except:
    pass

# /home/pi/lib/RAIO8870.h: 135
try:
    CURS = 69
except:
    pass

# /home/pi/lib/RAIO8870.h: 136
try:
    CURH0 = 70
except:
    pass

# /home/pi/lib/RAIO8870.h: 137
try:
    CURH1 = 71
except:
    pass

# /home/pi/lib/RAIO8870.h: 138
try:
    CURV0 = 72
except:
    pass

# /home/pi/lib/RAIO8870.h: 139
try:
    CURV1 = 73
except:
    pass

# /home/pi/lib/RAIO8870.h: 140
try:
    RCURH0 = 74
except:
    pass

# /home/pi/lib/RAIO8870.h: 141
try:
    RCURH01 = 75
except:
    pass

# /home/pi/lib/RAIO8870.h: 142
try:
    RCURV0 = 76
except:
    pass

# /home/pi/lib/RAIO8870.h: 143
try:
    RCURV1 = 77
except:
    pass

# /home/pi/lib/RAIO8870.h: 144
try:
    MRCD = 78
except:
    pass

# /home/pi/lib/RAIO8870.h: 145
try:
    BECR0 = 80
except:
    pass

# /home/pi/lib/RAIO8870.h: 146
try:
    BECR1 = 81
except:
    pass

# /home/pi/lib/RAIO8870.h: 147
try:
    LTPR0 = 82
except:
    pass

# /home/pi/lib/RAIO8870.h: 148
try:
    LTPR1 = 83
except:
    pass

# /home/pi/lib/RAIO8870.h: 149
try:
    HSBE0 = 84
except:
    pass

# /home/pi/lib/RAIO8870.h: 150
try:
    HSBE1 = 85
except:
    pass

# /home/pi/lib/RAIO8870.h: 151
try:
    VSBE0 = 86
except:
    pass

# /home/pi/lib/RAIO8870.h: 152
try:
    VSBE1 = 87
except:
    pass

# /home/pi/lib/RAIO8870.h: 153
try:
    HDBE0 = 88
except:
    pass

# /home/pi/lib/RAIO8870.h: 154
try:
    HDBE1 = 89
except:
    pass

# /home/pi/lib/RAIO8870.h: 155
try:
    VDBE0 = 90
except:
    pass

# /home/pi/lib/RAIO8870.h: 156
try:
    VDBE1 = 91
except:
    pass

# /home/pi/lib/RAIO8870.h: 157
try:
    BEWR0 = 92
except:
    pass

# /home/pi/lib/RAIO8870.h: 158
try:
    BEWR1 = 93
except:
    pass

# /home/pi/lib/RAIO8870.h: 159
try:
    BEHR0 = 94
except:
    pass

# /home/pi/lib/RAIO8870.h: 160
try:
    BEHR1 = 95
except:
    pass

# /home/pi/lib/RAIO8870.h: 162
try:
    BGCR0 = 96
except:
    pass

# /home/pi/lib/RAIO8870.h: 163
try:
    BGCR1 = 97
except:
    pass

# /home/pi/lib/RAIO8870.h: 164
try:
    BGCR2 = 98
except:
    pass

# /home/pi/lib/RAIO8870.h: 165
try:
    FGCR0 = 99
except:
    pass

# /home/pi/lib/RAIO8870.h: 166
try:
    FGCR1 = 100
except:
    pass

# /home/pi/lib/RAIO8870.h: 167
try:
    FGCR2 = 101
except:
    pass

# /home/pi/lib/RAIO8870.h: 168
try:
    PTNO = 102
except:
    pass

# /home/pi/lib/RAIO8870.h: 169
try:
    BGTR = 103
except:
    pass

# /home/pi/lib/RAIO8870.h: 171
try:
    TPCR0 = 112
except:
    pass

# /home/pi/lib/RAIO8870.h: 172
try:
    TPCR1 = 113
except:
    pass

# /home/pi/lib/RAIO8870.h: 173
try:
    TPXH = 114
except:
    pass

# /home/pi/lib/RAIO8870.h: 174
try:
    TPYH = 115
except:
    pass

# /home/pi/lib/RAIO8870.h: 175
try:
    TPXYL = 116
except:
    pass

# /home/pi/lib/RAIO8870.h: 177
try:
    GCHP0 = 128
except:
    pass

# /home/pi/lib/RAIO8870.h: 178
try:
    GCHP1 = 129
except:
    pass

# /home/pi/lib/RAIO8870.h: 179
try:
    GCVP0 = 130
except:
    pass

# /home/pi/lib/RAIO8870.h: 180
try:
    GCVP1 = 131
except:
    pass

# /home/pi/lib/RAIO8870.h: 181
try:
    GCC0 = 132
except:
    pass

# /home/pi/lib/RAIO8870.h: 182
try:
    GCC1 = 133
except:
    pass

# /home/pi/lib/RAIO8870.h: 184
try:
    PLLC1 = 136
except:
    pass

# /home/pi/lib/RAIO8870.h: 185
try:
    PLLC2 = 137
except:
    pass

# /home/pi/lib/RAIO8870.h: 187
try:
    P1CR = 138
except:
    pass

# /home/pi/lib/RAIO8870.h: 188
try:
    P1DCR = 139
except:
    pass

# /home/pi/lib/RAIO8870.h: 189
try:
    P2CR = 140
except:
    pass

# /home/pi/lib/RAIO8870.h: 190
try:
    P2DCR = 141
except:
    pass

# /home/pi/lib/RAIO8870.h: 191
try:
    MCLR = 142
except:
    pass

# /home/pi/lib/RAIO8870.h: 192
try:
    INTC = 143
except:
    pass

# /home/pi/lib/RAIO8870.h: 194
try:
    DCR = 144
except:
    pass

# /home/pi/lib/RAIO8870.h: 195
try:
    DLHSR0 = 145
except:
    pass

# /home/pi/lib/RAIO8870.h: 196
try:
    DLHSR1 = 146
except:
    pass

# /home/pi/lib/RAIO8870.h: 197
try:
    DLVSR0 = 147
except:
    pass

# /home/pi/lib/RAIO8870.h: 198
try:
    DLVSR1 = 148
except:
    pass

# /home/pi/lib/RAIO8870.h: 199
try:
    DLHER0 = 149
except:
    pass

# /home/pi/lib/RAIO8870.h: 200
try:
    DLHER1 = 150
except:
    pass

# /home/pi/lib/RAIO8870.h: 201
try:
    DLVER0 = 151
except:
    pass

# /home/pi/lib/RAIO8870.h: 202
try:
    DLVER1 = 152
except:
    pass

# /home/pi/lib/RAIO8870.h: 203
try:
    DCHR0 = 153
except:
    pass

# /home/pi/lib/RAIO8870.h: 204
try:
    DCHR1 = 154
except:
    pass

# /home/pi/lib/RAIO8870.h: 205
try:
    DCVR0 = 155
except:
    pass

# /home/pi/lib/RAIO8870.h: 206
try:
    DCVR1 = 156
except:
    pass

# /home/pi/lib/RAIO8870.h: 207
try:
    DCRR = 157
except:
    pass

# /home/pi/lib/RAIO8870.h: 209
try:
    TCR1 = 160
except:
    pass

# /home/pi/lib/RAIO8870.h: 210
try:
    TCR2 = 161
except:
    pass

# /home/pi/lib/RAIO8870.h: 211
try:
    OEHTCR1 = 162
except:
    pass

# /home/pi/lib/RAIO8870.h: 212
try:
    OEHTCR2 = 163
except:
    pass

# /home/pi/lib/RAIO8870.h: 213
try:
    OEHTCR3 = 164
except:
    pass

# /home/pi/lib/RAIO8870.h: 214
try:
    OEHTCR4 = 165
except:
    pass

# /home/pi/lib/RAIO8870.h: 215
try:
    OEHTCR5 = 166
except:
    pass

# /home/pi/lib/RAIO8870.h: 216
try:
    OEHTCR6 = 167
except:
    pass

# /home/pi/lib/RAIO8870.h: 217
try:
    OEHTCR7 = 168
except:
    pass

# /home/pi/lib/RAIO8870.h: 218
try:
    OEHTCR8 = 169
except:
    pass

# /home/pi/lib/RAIO8870.h: 220
try:
    STHTCR1 = 170
except:
    pass

# /home/pi/lib/RAIO8870.h: 221
try:
    STHTCR2 = 171
except:
    pass

# /home/pi/lib/RAIO8870.h: 222
try:
    STHTCR3 = 172
except:
    pass

# /home/pi/lib/RAIO8870.h: 223
try:
    STHTCR4 = 173
except:
    pass

# /home/pi/lib/RAIO8870.h: 225
try:
    Q1HCR1 = 174
except:
    pass

# /home/pi/lib/RAIO8870.h: 226
try:
    Q1HCR2 = 175
except:
    pass

# /home/pi/lib/RAIO8870.h: 228
try:
    OEVTCR1 = 176
except:
    pass

# /home/pi/lib/RAIO8870.h: 229
try:
    OEVTCR2 = 177
except:
    pass

# /home/pi/lib/RAIO8870.h: 230
try:
    OEVTCR3 = 178
except:
    pass

# /home/pi/lib/RAIO8870.h: 231
try:
    OEVTCR4 = 179
except:
    pass

# /home/pi/lib/RAIO8870.h: 232
try:
    CKVTCR1 = 180
except:
    pass

# /home/pi/lib/RAIO8870.h: 233
try:
    CKVTCR2 = 181
except:
    pass

# /home/pi/lib/RAIO8870.h: 234
try:
    CKVTCR3 = 182
except:
    pass

# /home/pi/lib/RAIO8870.h: 235
try:
    CKVTCR4 = 183
except:
    pass

# /home/pi/lib/RAIO8870.h: 236
try:
    STVTCR1 = 184
except:
    pass

# /home/pi/lib/RAIO8870.h: 237
try:
    STVTCR2 = 185
except:
    pass

# /home/pi/lib/RAIO8870.h: 238
try:
    STVTCR3 = 186
except:
    pass

# /home/pi/lib/RAIO8870.h: 239
try:
    STVTCR4 = 187
except:
    pass

# /home/pi/lib/RAIO8870.h: 240
try:
    STVTCR5 = 188
except:
    pass

# /home/pi/lib/RAIO8870.h: 241
try:
    STVTCR6 = 189
except:
    pass

# /home/pi/lib/RAIO8870.h: 242
try:
    STVTCR7 = 190
except:
    pass

# /home/pi/lib/RAIO8870.h: 243
try:
    STVTCR8 = 191
except:
    pass

# /home/pi/lib/RAIO8870.h: 245
try:
    COMTCR1 = 192
except:
    pass

# /home/pi/lib/RAIO8870.h: 246
try:
    COMTCR2 = 193
except:
    pass

# /home/pi/lib/RAIO8870.h: 247
try:
    RGBTCR1 = 194
except:
    pass

# /home/pi/lib/RAIO8870.h: 248
try:
    RGBTCR2 = 195
except:
    pass

# /home/pi/lib/RAIO8870.h: 252
try:
    COLOR_RED = 224
except:
    pass

# /home/pi/lib/RAIO8870.h: 253
try:
    COLOR_BLUE = 3
except:
    pass

# /home/pi/lib/RAIO8870.h: 254
try:
    COLOR_GREEN = 28
except:
    pass

# /home/pi/lib/RAIO8870.h: 255
try:
    COLOR_BLACK = 0
except:
    pass

# /home/pi/lib/RAIO8870.h: 256
try:
    COLOR_WHITE = 255
except:
    pass

# /home/pi/lib/RAIO8870.h: 257
try:
    COLOR_CYAN = 31
except:
    pass

# /home/pi/lib/RAIO8870.h: 258
try:
    COLOR_YELLOW = 252
except:
    pass

# /home/pi/lib/RAIO8870.h: 259
try:
    COLOR_MAGENTA = 227
except:
    pass

# /home/pi/lib/RAIO8870.h: 260
try:
    COLOR_DARK_GREEN = 12
except:
    pass

# /home/pi/lib/RAIO8870.h: 264
try:
    ROP_SOURCE = 12
except:
    pass

# /home/pi/lib/RAIO8870.h: 268
try:
    BTE_MOVE_POSITIVE = 2
except:
    pass

# /home/pi/lib/RAIO8870.h: 269
try:
    BTE_SOLID_FILL = 12
except:
    pass

# /home/pi/lib/tft.h: 61
try:
    MOSI = RPI_V2_GPIO_P1_19
except:
    pass

# /home/pi/lib/tft.h: 62
try:
    MISO = RPI_V2_GPIO_P1_21
except:
    pass

# /home/pi/lib/tft.h: 63
try:
    SCLK = RPI_V2_GPIO_P1_23
except:
    pass

# /home/pi/lib/tft.h: 64
try:
    OE = RPI_V2_GPIO_P1_11
except:
    pass

# /home/pi/lib/tft.h: 65
try:
    SPI_CE1 = RPI_V2_GPIO_P1_26
except:
    pass

# /home/pi/lib/tft.h: 66
try:
    RAIO_RS = RPI_V2_GPIO_P1_12
except:
    pass

# /home/pi/lib/tft.h: 67
try:
    RAIO_RST = RPI_V2_GPIO_P1_22
except:
    pass

# /home/pi/lib/tft.h: 68
try:
    RAIO_CS = RPI_V2_GPIO_P1_24
except:
    pass

# /home/pi/lib/tft.h: 69
try:
    RAIO_WR = RPI_V2_GPIO_P1_18
except:
    pass

# /home/pi/lib/tft.h: 70
try:
    RAIO_RD = RPI_V2_GPIO_P1_16
except:
    pass

# /home/pi/lib/tft.h: 71
try:
    RAIO_WAIT = RPI_V2_GPIO_P1_15
except:
    pass

# /home/pi/lib/tft.h: 72
try:
    RAIO_INT = RPI_V2_GPIO_P1_13
except:
    pass

# /home/pi/lib/tft.h: 74
try:
    RAIO_WRpin = 24
except:
    pass

# /usr/local/include/bcm2835.h: 325
try:
    HIGH = 1
except:
    pass

# /usr/local/include/bcm2835.h: 327
try:
    LOW = 0
except:
    pass

# /usr/local/include/bcm2835.h: 330
try:
    BCM2835_CORE_CLK_HZ = 250000000
except:
    pass

# /usr/local/include/bcm2835.h: 334
try:
    BCM2835_PERI_BASE = 536870912
except:
    pass

# /usr/local/include/bcm2835.h: 336
try:
    BCM2835_ST_BASE = (BCM2835_PERI_BASE + 12288)
except:
    pass

# /usr/local/include/bcm2835.h: 338
try:
    BCM2835_GPIO_PADS = (BCM2835_PERI_BASE + 1048576)
except:
    pass

# /usr/local/include/bcm2835.h: 340
try:
    BCM2835_CLOCK_BASE = (BCM2835_PERI_BASE + 1052672)
except:
    pass

# /usr/local/include/bcm2835.h: 342
try:
    BCM2835_GPIO_BASE = (BCM2835_PERI_BASE + 2097152)
except:
    pass

# /usr/local/include/bcm2835.h: 344
try:
    BCM2835_SPI0_BASE = (BCM2835_PERI_BASE + 2113536)
except:
    pass

# /usr/local/include/bcm2835.h: 346
try:
    BCM2835_BSC0_BASE = (BCM2835_PERI_BASE + 2117632)
except:
    pass

# /usr/local/include/bcm2835.h: 348
try:
    BCM2835_GPIO_PWM = (BCM2835_PERI_BASE + 2146304)
except:
    pass

# /usr/local/include/bcm2835.h: 350
try:
    BCM2835_BSC1_BASE = (BCM2835_PERI_BASE + 8404992)
except:
    pass

# /usr/local/include/bcm2835.h: 386
try:
    BCM2835_PAGE_SIZE = (4 * 1024)
except:
    pass

# /usr/local/include/bcm2835.h: 388
try:
    BCM2835_BLOCK_SIZE = (4 * 1024)
except:
    pass

# /usr/local/include/bcm2835.h: 395
try:
    BCM2835_GPFSEL0 = 0
except:
    pass

# /usr/local/include/bcm2835.h: 396
try:
    BCM2835_GPFSEL1 = 4
except:
    pass

# /usr/local/include/bcm2835.h: 397
try:
    BCM2835_GPFSEL2 = 8
except:
    pass

# /usr/local/include/bcm2835.h: 398
try:
    BCM2835_GPFSEL3 = 12
except:
    pass

# /usr/local/include/bcm2835.h: 399
try:
    BCM2835_GPFSEL4 = 16
except:
    pass

# /usr/local/include/bcm2835.h: 400
try:
    BCM2835_GPFSEL5 = 20
except:
    pass

# /usr/local/include/bcm2835.h: 401
try:
    BCM2835_GPSET0 = 28
except:
    pass

# /usr/local/include/bcm2835.h: 402
try:
    BCM2835_GPSET1 = 32
except:
    pass

# /usr/local/include/bcm2835.h: 403
try:
    BCM2835_GPCLR0 = 40
except:
    pass

# /usr/local/include/bcm2835.h: 404
try:
    BCM2835_GPCLR1 = 44
except:
    pass

# /usr/local/include/bcm2835.h: 405
try:
    BCM2835_GPLEV0 = 52
except:
    pass

# /usr/local/include/bcm2835.h: 406
try:
    BCM2835_GPLEV1 = 56
except:
    pass

# /usr/local/include/bcm2835.h: 407
try:
    BCM2835_GPEDS0 = 64
except:
    pass

# /usr/local/include/bcm2835.h: 408
try:
    BCM2835_GPEDS1 = 68
except:
    pass

# /usr/local/include/bcm2835.h: 409
try:
    BCM2835_GPREN0 = 76
except:
    pass

# /usr/local/include/bcm2835.h: 410
try:
    BCM2835_GPREN1 = 80
except:
    pass

# /usr/local/include/bcm2835.h: 411
try:
    BCM2835_GPFEN0 = 88
except:
    pass

# /usr/local/include/bcm2835.h: 412
try:
    BCM2835_GPFEN1 = 92
except:
    pass

# /usr/local/include/bcm2835.h: 413
try:
    BCM2835_GPHEN0 = 100
except:
    pass

# /usr/local/include/bcm2835.h: 414
try:
    BCM2835_GPHEN1 = 104
except:
    pass

# /usr/local/include/bcm2835.h: 415
try:
    BCM2835_GPLEN0 = 112
except:
    pass

# /usr/local/include/bcm2835.h: 416
try:
    BCM2835_GPLEN1 = 116
except:
    pass

# /usr/local/include/bcm2835.h: 417
try:
    BCM2835_GPAREN0 = 124
except:
    pass

# /usr/local/include/bcm2835.h: 418
try:
    BCM2835_GPAREN1 = 128
except:
    pass

# /usr/local/include/bcm2835.h: 419
try:
    BCM2835_GPAFEN0 = 136
except:
    pass

# /usr/local/include/bcm2835.h: 420
try:
    BCM2835_GPAFEN1 = 140
except:
    pass

# /usr/local/include/bcm2835.h: 421
try:
    BCM2835_GPPUD = 148
except:
    pass

# /usr/local/include/bcm2835.h: 422
try:
    BCM2835_GPPUDCLK0 = 152
except:
    pass

# /usr/local/include/bcm2835.h: 423
try:
    BCM2835_GPPUDCLK1 = 156
except:
    pass

# /usr/local/include/bcm2835.h: 450
try:
    BCM2835_PADS_GPIO_0_27 = 44
except:
    pass

# /usr/local/include/bcm2835.h: 451
try:
    BCM2835_PADS_GPIO_28_45 = 48
except:
    pass

# /usr/local/include/bcm2835.h: 452
try:
    BCM2835_PADS_GPIO_46_53 = 52
except:
    pass

# /usr/local/include/bcm2835.h: 455
try:
    BCM2835_PAD_PASSWRD = (90 << 24)
except:
    pass

# /usr/local/include/bcm2835.h: 456
try:
    BCM2835_PAD_SLEW_RATE_UNLIMITED = 16
except:
    pass

# /usr/local/include/bcm2835.h: 457
try:
    BCM2835_PAD_HYSTERESIS_ENABLED = 8
except:
    pass

# /usr/local/include/bcm2835.h: 458
try:
    BCM2835_PAD_DRIVE_2mA = 0
except:
    pass

# /usr/local/include/bcm2835.h: 459
try:
    BCM2835_PAD_DRIVE_4mA = 1
except:
    pass

# /usr/local/include/bcm2835.h: 460
try:
    BCM2835_PAD_DRIVE_6mA = 2
except:
    pass

# /usr/local/include/bcm2835.h: 461
try:
    BCM2835_PAD_DRIVE_8mA = 3
except:
    pass

# /usr/local/include/bcm2835.h: 462
try:
    BCM2835_PAD_DRIVE_10mA = 4
except:
    pass

# /usr/local/include/bcm2835.h: 463
try:
    BCM2835_PAD_DRIVE_12mA = 5
except:
    pass

# /usr/local/include/bcm2835.h: 464
try:
    BCM2835_PAD_DRIVE_14mA = 6
except:
    pass

# /usr/local/include/bcm2835.h: 465
try:
    BCM2835_PAD_DRIVE_16mA = 7
except:
    pass

# /usr/local/include/bcm2835.h: 536
try:
    BCM2835_SPI0_CS = 0
except:
    pass

# /usr/local/include/bcm2835.h: 537
try:
    BCM2835_SPI0_FIFO = 4
except:
    pass

# /usr/local/include/bcm2835.h: 538
try:
    BCM2835_SPI0_CLK = 8
except:
    pass

# /usr/local/include/bcm2835.h: 539
try:
    BCM2835_SPI0_DLEN = 12
except:
    pass

# /usr/local/include/bcm2835.h: 540
try:
    BCM2835_SPI0_LTOH = 16
except:
    pass

# /usr/local/include/bcm2835.h: 541
try:
    BCM2835_SPI0_DC = 20
except:
    pass

# /usr/local/include/bcm2835.h: 544
try:
    BCM2835_SPI0_CS_LEN_LONG = 33554432
except:
    pass

# /usr/local/include/bcm2835.h: 545
try:
    BCM2835_SPI0_CS_DMA_LEN = 16777216
except:
    pass

# /usr/local/include/bcm2835.h: 546
try:
    BCM2835_SPI0_CS_CSPOL2 = 8388608
except:
    pass

# /usr/local/include/bcm2835.h: 547
try:
    BCM2835_SPI0_CS_CSPOL1 = 4194304
except:
    pass

# /usr/local/include/bcm2835.h: 548
try:
    BCM2835_SPI0_CS_CSPOL0 = 2097152
except:
    pass

# /usr/local/include/bcm2835.h: 549
try:
    BCM2835_SPI0_CS_RXF = 1048576
except:
    pass

# /usr/local/include/bcm2835.h: 550
try:
    BCM2835_SPI0_CS_RXR = 524288
except:
    pass

# /usr/local/include/bcm2835.h: 551
try:
    BCM2835_SPI0_CS_TXD = 262144
except:
    pass

# /usr/local/include/bcm2835.h: 552
try:
    BCM2835_SPI0_CS_RXD = 131072
except:
    pass

# /usr/local/include/bcm2835.h: 553
try:
    BCM2835_SPI0_CS_DONE = 65536
except:
    pass

# /usr/local/include/bcm2835.h: 554
try:
    BCM2835_SPI0_CS_TE_EN = 32768
except:
    pass

# /usr/local/include/bcm2835.h: 555
try:
    BCM2835_SPI0_CS_LMONO = 16384
except:
    pass

# /usr/local/include/bcm2835.h: 556
try:
    BCM2835_SPI0_CS_LEN = 8192
except:
    pass

# /usr/local/include/bcm2835.h: 557
try:
    BCM2835_SPI0_CS_REN = 4096
except:
    pass

# /usr/local/include/bcm2835.h: 558
try:
    BCM2835_SPI0_CS_ADCS = 2048
except:
    pass

# /usr/local/include/bcm2835.h: 559
try:
    BCM2835_SPI0_CS_INTR = 1024
except:
    pass

# /usr/local/include/bcm2835.h: 560
try:
    BCM2835_SPI0_CS_INTD = 512
except:
    pass

# /usr/local/include/bcm2835.h: 561
try:
    BCM2835_SPI0_CS_DMAEN = 256
except:
    pass

# /usr/local/include/bcm2835.h: 562
try:
    BCM2835_SPI0_CS_TA = 128
except:
    pass

# /usr/local/include/bcm2835.h: 563
try:
    BCM2835_SPI0_CS_CSPOL = 64
except:
    pass

# /usr/local/include/bcm2835.h: 564
try:
    BCM2835_SPI0_CS_CLEAR = 48
except:
    pass

# /usr/local/include/bcm2835.h: 565
try:
    BCM2835_SPI0_CS_CLEAR_RX = 32
except:
    pass

# /usr/local/include/bcm2835.h: 566
try:
    BCM2835_SPI0_CS_CLEAR_TX = 16
except:
    pass

# /usr/local/include/bcm2835.h: 567
try:
    BCM2835_SPI0_CS_CPOL = 8
except:
    pass

# /usr/local/include/bcm2835.h: 568
try:
    BCM2835_SPI0_CS_CPHA = 4
except:
    pass

# /usr/local/include/bcm2835.h: 569
try:
    BCM2835_SPI0_CS_CS = 3
except:
    pass

# /usr/local/include/bcm2835.h: 629
try:
    BCM2835_BSC_C = 0
except:
    pass

# /usr/local/include/bcm2835.h: 630
try:
    BCM2835_BSC_S = 4
except:
    pass

# /usr/local/include/bcm2835.h: 631
try:
    BCM2835_BSC_DLEN = 8
except:
    pass

# /usr/local/include/bcm2835.h: 632
try:
    BCM2835_BSC_A = 12
except:
    pass

# /usr/local/include/bcm2835.h: 633
try:
    BCM2835_BSC_FIFO = 16
except:
    pass

# /usr/local/include/bcm2835.h: 634
try:
    BCM2835_BSC_DIV = 20
except:
    pass

# /usr/local/include/bcm2835.h: 635
try:
    BCM2835_BSC_DEL = 24
except:
    pass

# /usr/local/include/bcm2835.h: 636
try:
    BCM2835_BSC_CLKT = 28
except:
    pass

# /usr/local/include/bcm2835.h: 639
try:
    BCM2835_BSC_C_I2CEN = 32768
except:
    pass

# /usr/local/include/bcm2835.h: 640
try:
    BCM2835_BSC_C_INTR = 1024
except:
    pass

# /usr/local/include/bcm2835.h: 641
try:
    BCM2835_BSC_C_INTT = 512
except:
    pass

# /usr/local/include/bcm2835.h: 642
try:
    BCM2835_BSC_C_INTD = 256
except:
    pass

# /usr/local/include/bcm2835.h: 643
try:
    BCM2835_BSC_C_ST = 128
except:
    pass

# /usr/local/include/bcm2835.h: 644
try:
    BCM2835_BSC_C_CLEAR_1 = 32
except:
    pass

# /usr/local/include/bcm2835.h: 645
try:
    BCM2835_BSC_C_CLEAR_2 = 16
except:
    pass

# /usr/local/include/bcm2835.h: 646
try:
    BCM2835_BSC_C_READ = 1
except:
    pass

# /usr/local/include/bcm2835.h: 649
try:
    BCM2835_BSC_S_CLKT = 512
except:
    pass

# /usr/local/include/bcm2835.h: 650
try:
    BCM2835_BSC_S_ERR = 256
except:
    pass

# /usr/local/include/bcm2835.h: 651
try:
    BCM2835_BSC_S_RXF = 128
except:
    pass

# /usr/local/include/bcm2835.h: 652
try:
    BCM2835_BSC_S_TXE = 64
except:
    pass

# /usr/local/include/bcm2835.h: 653
try:
    BCM2835_BSC_S_RXD = 32
except:
    pass

# /usr/local/include/bcm2835.h: 654
try:
    BCM2835_BSC_S_TXD = 16
except:
    pass

# /usr/local/include/bcm2835.h: 655
try:
    BCM2835_BSC_S_RXR = 8
except:
    pass

# /usr/local/include/bcm2835.h: 656
try:
    BCM2835_BSC_S_TXW = 4
except:
    pass

# /usr/local/include/bcm2835.h: 657
try:
    BCM2835_BSC_S_DONE = 2
except:
    pass

# /usr/local/include/bcm2835.h: 658
try:
    BCM2835_BSC_S_TA = 1
except:
    pass

# /usr/local/include/bcm2835.h: 660
try:
    BCM2835_BSC_FIFO_SIZE = 16
except:
    pass

# /usr/local/include/bcm2835.h: 693
try:
    BCM2835_ST_CS = 0
except:
    pass

# /usr/local/include/bcm2835.h: 694
try:
    BCM2835_ST_CLO = 4
except:
    pass

# /usr/local/include/bcm2835.h: 695
try:
    BCM2835_ST_CHI = 8
except:
    pass

# /usr/local/include/bcm2835.h: 701
try:
    BCM2835_PWM_CONTROL = 0
except:
    pass

# /usr/local/include/bcm2835.h: 702
try:
    BCM2835_PWM_STATUS = 1
except:
    pass

# /usr/local/include/bcm2835.h: 703
try:
    BCM2835_PWM_DMAC = 2
except:
    pass

# /usr/local/include/bcm2835.h: 704
try:
    BCM2835_PWM0_RANGE = 4
except:
    pass

# /usr/local/include/bcm2835.h: 705
try:
    BCM2835_PWM0_DATA = 5
except:
    pass

# /usr/local/include/bcm2835.h: 706
try:
    BCM2835_PWM_FIF1 = 6
except:
    pass

# /usr/local/include/bcm2835.h: 707
try:
    BCM2835_PWM1_RANGE = 8
except:
    pass

# /usr/local/include/bcm2835.h: 708
try:
    BCM2835_PWM1_DATA = 9
except:
    pass

# /usr/local/include/bcm2835.h: 711
try:
    BCM2835_PWMCLK_CNTL = 40
except:
    pass

# /usr/local/include/bcm2835.h: 712
try:
    BCM2835_PWMCLK_DIV = 41
except:
    pass

# /usr/local/include/bcm2835.h: 713
try:
    BCM2835_PWM_PASSWRD = (90 << 24)
except:
    pass

# /usr/local/include/bcm2835.h: 715
try:
    BCM2835_PWM1_MS_MODE = 32768
except:
    pass

# /usr/local/include/bcm2835.h: 716
try:
    BCM2835_PWM1_USEFIFO = 8192
except:
    pass

# /usr/local/include/bcm2835.h: 717
try:
    BCM2835_PWM1_REVPOLAR = 4096
except:
    pass

# /usr/local/include/bcm2835.h: 718
try:
    BCM2835_PWM1_OFFSTATE = 2048
except:
    pass

# /usr/local/include/bcm2835.h: 719
try:
    BCM2835_PWM1_REPEATFF = 1024
except:
    pass

# /usr/local/include/bcm2835.h: 720
try:
    BCM2835_PWM1_SERIAL = 512
except:
    pass

# /usr/local/include/bcm2835.h: 721
try:
    BCM2835_PWM1_ENABLE = 256
except:
    pass

# /usr/local/include/bcm2835.h: 723
try:
    BCM2835_PWM0_MS_MODE = 128
except:
    pass

# /usr/local/include/bcm2835.h: 724
try:
    BCM2835_PWM_CLEAR_FIFO = 64
except:
    pass

# /usr/local/include/bcm2835.h: 725
try:
    BCM2835_PWM0_USEFIFO = 32
except:
    pass

# /usr/local/include/bcm2835.h: 726
try:
    BCM2835_PWM0_REVPOLAR = 16
except:
    pass

# /usr/local/include/bcm2835.h: 727
try:
    BCM2835_PWM0_OFFSTATE = 8
except:
    pass

# /usr/local/include/bcm2835.h: 728
try:
    BCM2835_PWM0_REPEATFF = 4
except:
    pass

# /usr/local/include/bcm2835.h: 729
try:
    BCM2835_PWM0_SERIAL = 2
except:
    pass

# /usr/local/include/bcm2835.h: 730
try:
    BCM2835_PWM0_ENABLE = 1
except:
    pass

# /usr/local/include/bcm2835.h: 759
def delay(x):
    return (bcm2835_delay (x))

# /usr/local/include/bcm2835.h: 760
def delayMicroseconds(x):
    return (bcm2835_delayMicroseconds (x))

my_union = union_my_union # /home/pi/lib/RAIO8870.h: 274

# No inserted files

