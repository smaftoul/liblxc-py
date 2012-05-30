'''Wrapper for lxc.h

Generated with:
/usr/local/bin/ctypesgen.py -L/usr/lib/lxc/ -lliblxc.so.0 -o liblxc.py lxc.h conf.h log.h caps.h confile.h list.h -I..

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
_libdirs = ['/usr/lib/lxc/']

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

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

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

add_library_search_dirs(['/usr/lib/lxc/'])

# Begin libraries

_libs["liblxc.so.0"] = load_library("liblxc.so.0")

# 1 libraries
# End libraries

# No modules

enum_anon_1 = c_int # ../lxc/state.h: 29

lxc_state_t = enum_anon_1 # ../lxc/state.h: 29

# /root/lxc-0.7.5/src/lxc/lxc.h: 33
class struct_lxc_msg(Structure):
    pass

# /root/lxc-0.7.5/src/lxc/conf.h: 198
class struct_lxc_conf(Structure):
    pass

# /root/lxc-0.7.5/src/lxc/lxc.h: 49
if hasattr(_libs['liblxc.so.0'], 'lxc_start'):
    lxc_start = _libs['liblxc.so.0'].lxc_start
    lxc_start.argtypes = [String, POINTER(POINTER(c_char)), POINTER(struct_lxc_conf)]
    lxc_start.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 57
if hasattr(_libs['liblxc.so.0'], 'lxc_stop'):
    lxc_stop = _libs['liblxc.so.0'].lxc_stop
    lxc_stop.argtypes = [String]
    lxc_stop.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 64
if hasattr(_libs['liblxc.so.0'], 'lxc_monitor_open'):
    lxc_monitor_open = _libs['liblxc.so.0'].lxc_monitor_open
    lxc_monitor_open.argtypes = []
    lxc_monitor_open.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 74
if hasattr(_libs['liblxc.so.0'], 'lxc_monitor_read'):
    lxc_monitor_read = _libs['liblxc.so.0'].lxc_monitor_read
    lxc_monitor_read.argtypes = [c_int, POINTER(struct_lxc_msg)]
    lxc_monitor_read.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 81
if hasattr(_libs['liblxc.so.0'], 'lxc_monitor_close'):
    lxc_monitor_close = _libs['liblxc.so.0'].lxc_monitor_close
    lxc_monitor_close.argtypes = [c_int]
    lxc_monitor_close.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 90
if hasattr(_libs['liblxc.so.0'], 'lxc_console'):
    lxc_console = _libs['liblxc.so.0'].lxc_console
    lxc_console.argtypes = [String, c_int, POINTER(c_int)]
    lxc_console.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 97
if hasattr(_libs['liblxc.so.0'], 'lxc_freeze'):
    lxc_freeze = _libs['liblxc.so.0'].lxc_freeze
    lxc_freeze.argtypes = [String]
    lxc_freeze.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 104
if hasattr(_libs['liblxc.so.0'], 'lxc_unfreeze'):
    lxc_unfreeze = _libs['liblxc.so.0'].lxc_unfreeze
    lxc_unfreeze.argtypes = [String]
    lxc_unfreeze.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lxc_state'):
        continue
    lxc_state = _lib.lxc_state
    lxc_state.argtypes = [String]
    lxc_state.restype = lxc_state_t
    break

# /root/lxc-0.7.5/src/lxc/lxc.h: 121
if hasattr(_libs['liblxc.so.0'], 'lxc_cgroup_set'):
    lxc_cgroup_set = _libs['liblxc.so.0'].lxc_cgroup_set
    lxc_cgroup_set.argtypes = [String, String, String]
    lxc_cgroup_set.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 132
if hasattr(_libs['liblxc.so.0'], 'lxc_cgroup_get'):
    lxc_cgroup_get = _libs['liblxc.so.0'].lxc_cgroup_get
    lxc_cgroup_get.argtypes = [String, String, String, c_size_t]
    lxc_cgroup_get.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 141
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lxc_strerror'):
        continue
    lxc_strerror = _lib.lxc_strerror
    lxc_strerror.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        lxc_strerror.restype = ReturnString
    else:
        lxc_strerror.restype = String
        lxc_strerror.errcheck = ReturnString
    break

# /root/lxc-0.7.5/src/lxc/lxc.h: 150
if hasattr(_libs['liblxc.so.0'], 'lxc_checkpoint'):
    lxc_checkpoint = _libs['liblxc.so.0'].lxc_checkpoint
    lxc_checkpoint.argtypes = [String, c_int, c_int]
    lxc_checkpoint.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 162
if hasattr(_libs['liblxc.so.0'], 'lxc_restart'):
    lxc_restart = _libs['liblxc.so.0'].lxc_restart
    lxc_restart.argtypes = [String, c_int, POINTER(struct_lxc_conf), c_int]
    lxc_restart.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 167
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'lxc_version'):
        continue
    lxc_version = _lib.lxc_version
    lxc_version.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        lxc_version.restype = ReturnString
    else:
        lxc_version.restype = String
        lxc_version.errcheck = ReturnString
    break

__pid_t = c_int # /usr/include/i386-linux-gnu/bits/types.h: 143

__time_t = c_long # /usr/include/i386-linux-gnu/bits/types.h: 149

__suseconds_t = c_long # /usr/include/i386-linux-gnu/bits/types.h: 151

pid_t = __pid_t # /usr/include/i386-linux-gnu/sys/types.h: 99

ushort = c_uint # /usr/include/i386-linux-gnu/sys/types.h: 152

uint = c_uint # /usr/include/i386-linux-gnu/sys/types.h: 153

# /usr/include/i386-linux-gnu/bits/sigset.h: 32
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    '__val',
]
struct_anon_5._fields_ = [
    ('__val', c_ulong * (1024 / (8 * sizeof(c_ulong)))),
]

__sigset_t = struct_anon_5 # /usr/include/i386-linux-gnu/bits/sigset.h: 32

sigset_t = __sigset_t # /usr/include/i386-linux-gnu/sys/select.h: 38

# /usr/include/i386-linux-gnu/bits/time.h: 31
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

in_addr_t = c_uint32 # /usr/include/netinet/in.h: 141

# /usr/include/netinet/in.h: 142
class struct_in_addr(Structure):
    pass

struct_in_addr.__slots__ = [
    's_addr',
]
struct_in_addr._fields_ = [
    ('s_addr', in_addr_t),
]

# /usr/include/netinet/in.h: 200
class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    '__u6_addr8',
    '__u6_addr16',
    '__u6_addr32',
]
union_anon_23._fields_ = [
    ('__u6_addr8', c_uint8 * 16),
    ('__u6_addr16', c_uint16 * 8),
    ('__u6_addr32', c_uint32 * 4),
]

# /usr/include/netinet/in.h: 198
class struct_in6_addr(Structure):
    pass

struct_in6_addr.__slots__ = [
    '__in6_u',
]
struct_in6_addr._fields_ = [
    ('__in6_u', union_anon_23),
]

# ../lxc/list.h: 4
class struct_lxc_list(Structure):
    pass

struct_lxc_list.__slots__ = [
    'elem',
    'next',
    'prev',
]
struct_lxc_list._fields_ = [
    ('elem', POINTER(None)),
    ('next', POINTER(struct_lxc_list)),
    ('prev', POINTER(struct_lxc_list)),
]

# ../lxc/list.h: 66
for _lib in _libs.values():
    try:
        next = (POINTER(struct_lxc_list)).in_dll(_lib, 'next')
        break
    except:
        pass

# ../lxc/list.h: 66
for _lib in _libs.values():
    try:
        prev = (POINTER(struct_lxc_list)).in_dll(_lib, 'prev')
        break
    except:
        pass

# ../lxc/start.h: 38
class struct_lxc_handler(Structure):
    pass

# ../lxc/start.h: 33
class struct_lxc_operations(Structure):
    pass

struct_lxc_operations.__slots__ = [
    'start',
    'post_start',
]
struct_lxc_operations._fields_ = [
    ('start', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_lxc_handler), POINTER(None))),
    ('post_start', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_lxc_handler), POINTER(None))),
]

struct_lxc_handler.__slots__ = [
    'pid',
    'name',
    'state',
    'sigfd',
    'oldmask',
    'conf',
    'ops',
    'data',
    'sv',
]
struct_lxc_handler._fields_ = [
    ('pid', pid_t),
    ('name', String),
    ('state', lxc_state_t),
    ('sigfd', c_int),
    ('oldmask', sigset_t),
    ('conf', POINTER(struct_lxc_conf)),
    ('ops', POINTER(struct_lxc_operations)),
    ('data', POINTER(None)),
    ('sv', c_int * 2),
]

enum_anon_24 = c_int # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_EMPTY = 0 # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_VETH = (LXC_NET_EMPTY + 1) # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_MACVLAN = (LXC_NET_VETH + 1) # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_PHYS = (LXC_NET_MACVLAN + 1) # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_VLAN = (LXC_NET_PHYS + 1) # /root/lxc-0.7.5/src/lxc/conf.h: 33

LXC_NET_MAXCONFTYPE = (LXC_NET_VLAN + 1) # /root/lxc-0.7.5/src/lxc/conf.h: 33

# /root/lxc-0.7.5/src/lxc/conf.h: 48
class struct_lxc_inetdev(Structure):
    pass

struct_lxc_inetdev.__slots__ = [
    'addr',
    'bcast',
    'prefix',
]
struct_lxc_inetdev._fields_ = [
    ('addr', struct_in_addr),
    ('bcast', struct_in_addr),
    ('prefix', c_int),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 54
class struct_lxc_route(Structure):
    pass

struct_lxc_route.__slots__ = [
    'addr',
]
struct_lxc_route._fields_ = [
    ('addr', struct_in_addr),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 65
class struct_lxc_inet6dev(Structure):
    pass

struct_lxc_inet6dev.__slots__ = [
    'addr',
    'mcast',
    'acast',
    'prefix',
]
struct_lxc_inet6dev._fields_ = [
    ('addr', struct_in6_addr),
    ('mcast', struct_in6_addr),
    ('acast', struct_in6_addr),
    ('prefix', c_int),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 72
class struct_lxc_route6(Structure):
    pass

struct_lxc_route6.__slots__ = [
    'addr',
]
struct_lxc_route6._fields_ = [
    ('addr', struct_in6_addr),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 76
class struct_ifla_veth(Structure):
    pass

struct_ifla_veth.__slots__ = [
    'pair',
]
struct_ifla_veth._fields_ = [
    ('pair', String),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 80
class struct_ifla_vlan(Structure):
    pass

struct_ifla_vlan.__slots__ = [
    'flags',
    'fmask',
    'vid',
    'pad',
]
struct_ifla_vlan._fields_ = [
    ('flags', uint),
    ('fmask', uint),
    ('vid', ushort),
    ('pad', ushort),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 87
class struct_ifla_macvlan(Structure):
    pass

struct_ifla_macvlan.__slots__ = [
    'mode',
]
struct_ifla_macvlan._fields_ = [
    ('mode', c_int),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 91
class union_netdev_p(Union):
    pass

union_netdev_p.__slots__ = [
    'veth_attr',
    'vlan_attr',
    'macvlan_attr',
]
union_netdev_p._fields_ = [
    ('veth_attr', struct_ifla_veth),
    ('vlan_attr', struct_ifla_vlan),
    ('macvlan_attr', struct_ifla_macvlan),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 106
class struct_lxc_netdev(Structure):
    pass

struct_lxc_netdev.__slots__ = [
    'type',
    'flags',
    'ifindex',
    'link',
    'name',
    'hwaddr',
    'mtu',
    'priv',
    'ipv4',
    'ipv6',
    'upscript',
]
struct_lxc_netdev._fields_ = [
    ('type', c_int),
    ('flags', c_int),
    ('ifindex', c_int),
    ('link', String),
    ('name', String),
    ('hwaddr', String),
    ('mtu', String),
    ('priv', union_netdev_p),
    ('ipv4', struct_lxc_list),
    ('ipv6', struct_lxc_list),
    ('upscript', String),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 126
class struct_lxc_cgroup(Structure):
    pass

struct_lxc_cgroup.__slots__ = [
    'subsystem',
    'value',
]
struct_lxc_cgroup._fields_ = [
    ('subsystem', String),
    ('value', String),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 138
class struct_lxc_pty_info(Structure):
    pass

struct_lxc_pty_info.__slots__ = [
    'name',
    'master',
    'slave',
    'busy',
]
struct_lxc_pty_info._fields_ = [
    ('name', c_char * 4096),
    ('master', c_int),
    ('slave', c_int),
    ('busy', c_int),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 150
class struct_lxc_tty_info(Structure):
    pass

struct_lxc_tty_info.__slots__ = [
    'nbtty',
    'pty_info',
]
struct_lxc_tty_info._fields_ = [
    ('nbtty', c_int),
    ('pty_info', POINTER(struct_lxc_pty_info)),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 166
class struct_termios(Structure):
    pass

# /root/lxc-0.7.5/src/lxc/conf.h: 160
class struct_lxc_console(Structure):
    pass

struct_lxc_console.__slots__ = [
    'slave',
    'master',
    'peer',
    'path',
    'name',
    'tios',
]
struct_lxc_console._fields_ = [
    ('slave', c_int),
    ('master', c_int),
    ('peer', c_int),
    ('path', String),
    ('name', c_char * 4096),
    ('tios', POINTER(struct_termios)),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 175
class struct_lxc_rootfs(Structure):
    pass

struct_lxc_rootfs.__slots__ = [
    'path',
    'mount',
    'pivot',
]
struct_lxc_rootfs._fields_ = [
    ('path', String),
    ('mount', String),
    ('pivot', String),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 205
class struct_utsname(Structure):
    pass

struct_lxc_conf.__slots__ = [
    'fstab',
    'tty',
    'pts',
    'reboot',
    'need_utmp_watch',
    'personality',
    'utsname',
    'cgroup',
    'network',
    'mount_list',
    'caps',
    'tty_info',
    'console',
    'rootfs',
    'ttydir',
    'close_all_fds',
    'aa_profile',
    'umount_proc',
]
struct_lxc_conf._fields_ = [
    ('fstab', String),
    ('tty', c_int),
    ('pts', c_int),
    ('reboot', c_int),
    ('need_utmp_watch', c_int),
    ('personality', c_int),
    ('utsname', POINTER(struct_utsname)),
    ('cgroup', struct_lxc_list),
    ('network', struct_lxc_list),
    ('mount_list', struct_lxc_list),
    ('caps', struct_lxc_list),
    ('tty_info', struct_lxc_tty_info),
    ('console', struct_lxc_console),
    ('rootfs', struct_lxc_rootfs),
    ('ttydir', String),
    ('close_all_fds', c_int),
    ('aa_profile', String),
    ('umount_proc', c_int),
]

# /root/lxc-0.7.5/src/lxc/conf.h: 222
if hasattr(_libs['liblxc.so.0'], 'lxc_conf_init'):
    lxc_conf_init = _libs['liblxc.so.0'].lxc_conf_init
    lxc_conf_init.argtypes = []
    lxc_conf_init.restype = POINTER(struct_lxc_conf)

# /root/lxc-0.7.5/src/lxc/conf.h: 224
if hasattr(_libs['liblxc.so.0'], 'pin_rootfs'):
    pin_rootfs = _libs['liblxc.so.0'].pin_rootfs
    pin_rootfs.argtypes = [String]
    pin_rootfs.restype = c_int

# /root/lxc-0.7.5/src/lxc/conf.h: 226
if hasattr(_libs['liblxc.so.0'], 'lxc_create_network'):
    lxc_create_network = _libs['liblxc.so.0'].lxc_create_network
    lxc_create_network.argtypes = [POINTER(struct_lxc_handler)]
    lxc_create_network.restype = c_int

# /root/lxc-0.7.5/src/lxc/conf.h: 227
if hasattr(_libs['liblxc.so.0'], 'lxc_delete_network'):
    lxc_delete_network = _libs['liblxc.so.0'].lxc_delete_network
    lxc_delete_network.argtypes = [POINTER(struct_lxc_list)]
    lxc_delete_network.restype = None

# /root/lxc-0.7.5/src/lxc/conf.h: 228
if hasattr(_libs['liblxc.so.0'], 'lxc_assign_network'):
    lxc_assign_network = _libs['liblxc.so.0'].lxc_assign_network
    lxc_assign_network.argtypes = [POINTER(struct_lxc_list), pid_t]
    lxc_assign_network.restype = c_int

# /root/lxc-0.7.5/src/lxc/conf.h: 230
if hasattr(_libs['liblxc.so.0'], 'lxc_create_tty'):
    lxc_create_tty = _libs['liblxc.so.0'].lxc_create_tty
    lxc_create_tty.argtypes = [String, POINTER(struct_lxc_conf)]
    lxc_create_tty.restype = c_int

# /root/lxc-0.7.5/src/lxc/conf.h: 231
if hasattr(_libs['liblxc.so.0'], 'lxc_delete_tty'):
    lxc_delete_tty = _libs['liblxc.so.0'].lxc_delete_tty
    lxc_delete_tty.argtypes = [POINTER(struct_lxc_tty_info)]
    lxc_delete_tty.restype = None

# /root/lxc-0.7.5/src/lxc/conf.h: 237
if hasattr(_libs['liblxc.so.0'], 'lxc_setup'):
    lxc_setup = _libs['liblxc.so.0'].lxc_setup
    lxc_setup.argtypes = [String, POINTER(struct_lxc_conf)]
    lxc_setup.restype = c_int

enum_anon_29 = c_int # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_TRACE = 0 # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_DEBUG = (LXC_LOG_PRIORITY_TRACE + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_INFO = (LXC_LOG_PRIORITY_DEBUG + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_NOTICE = (LXC_LOG_PRIORITY_INFO + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_WARN = (LXC_LOG_PRIORITY_NOTICE + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_ERROR = (LXC_LOG_PRIORITY_WARN + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_CRIT = (LXC_LOG_PRIORITY_ERROR + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_ALERT = (LXC_LOG_PRIORITY_CRIT + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_FATAL = (LXC_LOG_PRIORITY_ALERT + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

LXC_LOG_PRIORITY_NOTSET = (LXC_LOG_PRIORITY_FATAL + 1) # /root/lxc-0.7.5/src/lxc/log.h: 44

# /root/lxc-0.7.5/src/lxc/log.h: 58
class struct_lxc_log_locinfo(Structure):
    pass

struct_lxc_log_locinfo.__slots__ = [
    'file',
    'func',
    'line',
]
struct_lxc_log_locinfo._fields_ = [
    ('file', String),
    ('func', String),
    ('line', c_int),
]

# /root/lxc-0.7.5/src/lxc/log.h: 68
class struct_lxc_log_event(Structure):
    pass

struct_lxc_log_event.__slots__ = [
    'category',
    'priority',
    'timestamp',
    'locinfo',
    'fmt',
    'vap',
]
struct_lxc_log_event._fields_ = [
    ('category', String),
    ('priority', c_int),
    ('timestamp', struct_timeval),
    ('locinfo', POINTER(struct_lxc_log_locinfo)),
    ('fmt', String),
    ('vap', POINTER(c_void_p)),
]

# /root/lxc-0.7.5/src/lxc/log.h: 78
class struct_lxc_log_appender(Structure):
    pass

struct_lxc_log_appender.__slots__ = [
    'name',
    'append',
    'next',
]
struct_lxc_log_appender._fields_ = [
    ('name', String),
    ('append', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_lxc_log_appender), POINTER(struct_lxc_log_event))),
    ('next', POINTER(struct_lxc_log_appender)),
]

# /root/lxc-0.7.5/src/lxc/log.h: 89
class struct_lxc_log_category(Structure):
    pass

struct_lxc_log_category.__slots__ = [
    'name',
    'priority',
    'appender',
    'parent',
]
struct_lxc_log_category._fields_ = [
    ('name', String),
    ('priority', c_int),
    ('appender', POINTER(struct_lxc_log_appender)),
    ('parent', POINTER(struct_lxc_log_category)),
]

# /root/lxc-0.7.5/src/lxc/log.h: 152
for _lib in _libs.values():
    try:
        va = (c_void_p).in_dll(_lib, 'va')
        break
    except:
        pass

# /root/lxc-0.7.5/src/lxc/log.h: 152
for _lib in _libs.values():
    try:
        va_keep = (POINTER(c_void_p)).in_dll(_lib, 'va_keep')
        break
    except:
        pass

# /root/lxc-0.7.5/src/lxc/log.h: 235
try:
    lxc_log_category_lxc = (struct_lxc_log_category).in_dll(_libs['liblxc.so.0'], 'lxc_log_category_lxc')
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 288
try:
    lxc_log_fd = (c_int).in_dll(_libs['liblxc.so.0'], 'lxc_log_fd')
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 290
if hasattr(_libs['liblxc.so.0'], 'lxc_log_init'):
    lxc_log_init = _libs['liblxc.so.0'].lxc_log_init
    lxc_log_init.argtypes = [String, String, String, c_int]
    lxc_log_init.restype = c_int

# /root/lxc-0.7.5/src/lxc/log.h: 293
if hasattr(_libs['liblxc.so.0'], 'lxc_log_setprefix'):
    lxc_log_setprefix = _libs['liblxc.so.0'].lxc_log_setprefix
    lxc_log_setprefix.argtypes = [String]
    lxc_log_setprefix.restype = None

# /root/lxc-0.7.5/src/lxc/caps.h: 26
if hasattr(_libs['liblxc.so.0'], 'lxc_caps_reset'):
    lxc_caps_reset = _libs['liblxc.so.0'].lxc_caps_reset
    lxc_caps_reset.argtypes = []
    lxc_caps_reset.restype = c_int

# /root/lxc-0.7.5/src/lxc/caps.h: 27
if hasattr(_libs['liblxc.so.0'], 'lxc_caps_down'):
    lxc_caps_down = _libs['liblxc.so.0'].lxc_caps_down
    lxc_caps_down.argtypes = []
    lxc_caps_down.restype = c_int

# /root/lxc-0.7.5/src/lxc/caps.h: 28
if hasattr(_libs['liblxc.so.0'], 'lxc_caps_up'):
    lxc_caps_up = _libs['liblxc.so.0'].lxc_caps_up
    lxc_caps_up.argtypes = []
    lxc_caps_up.restype = c_int

# /root/lxc-0.7.5/src/lxc/caps.h: 29
if hasattr(_libs['liblxc.so.0'], 'lxc_caps_init'):
    lxc_caps_init = _libs['liblxc.so.0'].lxc_caps_init
    lxc_caps_init.argtypes = []
    lxc_caps_init.restype = c_int

# /root/lxc-0.7.5/src/lxc/caps.h: 30
if hasattr(_libs['liblxc.so.0'], 'lxc_caps_check'):
    lxc_caps_check = _libs['liblxc.so.0'].lxc_caps_check
    lxc_caps_check.argtypes = []
    lxc_caps_check.restype = c_int

# /root/lxc-0.7.5/src/lxc/confile.h: 27
if hasattr(_libs['liblxc.so.0'], 'lxc_config_read'):
    lxc_config_read = _libs['liblxc.so.0'].lxc_config_read
    lxc_config_read.argtypes = [String, POINTER(struct_lxc_conf)]
    lxc_config_read.restype = c_int

# /root/lxc-0.7.5/src/lxc/confile.h: 28
if hasattr(_libs['liblxc.so.0'], 'lxc_config_readline'):
    lxc_config_readline = _libs['liblxc.so.0'].lxc_config_readline
    lxc_config_readline.argtypes = [String, POINTER(struct_lxc_conf)]
    lxc_config_readline.restype = c_int

# /root/lxc-0.7.5/src/lxc/confile.h: 30
if hasattr(_libs['liblxc.so.0'], 'lxc_config_define_add'):
    lxc_config_define_add = _libs['liblxc.so.0'].lxc_config_define_add
    lxc_config_define_add.argtypes = [POINTER(struct_lxc_list), String]
    lxc_config_define_add.restype = c_int

# /root/lxc-0.7.5/src/lxc/confile.h: 31
if hasattr(_libs['liblxc.so.0'], 'lxc_config_define_load'):
    lxc_config_define_load = _libs['liblxc.so.0'].lxc_config_define_load
    lxc_config_define_load.argtypes = [POINTER(struct_lxc_list), POINTER(struct_lxc_conf)]
    lxc_config_define_load.restype = c_int

# /root/lxc-0.7.5/src/lxc/lxc.h: 151
try:
    LXC_FLAG_PAUSE = 1
except:
    pass

# /root/lxc-0.7.5/src/lxc/lxc.h: 152
try:
    LXC_FLAG_HALT = 2
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 33
try:
    O_CLOEXEC = 2000000
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 37
try:
    F_DUPFD_CLOEXEC = 1030
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 40
try:
    LXC_LOG_PREFIX_SIZE = 32
except:
    pass

# /root/lxc-0.7.5/src/lxc/log.h: 41
try:
    LXC_LOG_BUFFER_SIZE = 512
except:
    pass

lxc_msg = struct_lxc_msg # /root/lxc-0.7.5/src/lxc/lxc.h: 33

lxc_conf = struct_lxc_conf # /root/lxc-0.7.5/src/lxc/conf.h: 198

lxc_list = struct_lxc_list # ../lxc/list.h: 4

lxc_inetdev = struct_lxc_inetdev # /root/lxc-0.7.5/src/lxc/conf.h: 48

lxc_route = struct_lxc_route # /root/lxc-0.7.5/src/lxc/conf.h: 54

lxc_inet6dev = struct_lxc_inet6dev # /root/lxc-0.7.5/src/lxc/conf.h: 65

lxc_route6 = struct_lxc_route6 # /root/lxc-0.7.5/src/lxc/conf.h: 72

ifla_veth = struct_ifla_veth # /root/lxc-0.7.5/src/lxc/conf.h: 76

ifla_vlan = struct_ifla_vlan # /root/lxc-0.7.5/src/lxc/conf.h: 80

ifla_macvlan = struct_ifla_macvlan # /root/lxc-0.7.5/src/lxc/conf.h: 87

netdev_p = union_netdev_p # /root/lxc-0.7.5/src/lxc/conf.h: 91

lxc_netdev = struct_lxc_netdev # /root/lxc-0.7.5/src/lxc/conf.h: 106

lxc_cgroup = struct_lxc_cgroup # /root/lxc-0.7.5/src/lxc/conf.h: 126

lxc_pty_info = struct_lxc_pty_info # /root/lxc-0.7.5/src/lxc/conf.h: 138

lxc_tty_info = struct_lxc_tty_info # /root/lxc-0.7.5/src/lxc/conf.h: 150

termios = struct_termios # /root/lxc-0.7.5/src/lxc/conf.h: 166

lxc_console = struct_lxc_console # /root/lxc-0.7.5/src/lxc/conf.h: 160

lxc_rootfs = struct_lxc_rootfs # /root/lxc-0.7.5/src/lxc/conf.h: 175

utsname = struct_utsname # /root/lxc-0.7.5/src/lxc/conf.h: 205

lxc_log_locinfo = struct_lxc_log_locinfo # /root/lxc-0.7.5/src/lxc/log.h: 58

lxc_log_event = struct_lxc_log_event # /root/lxc-0.7.5/src/lxc/log.h: 68

lxc_log_appender = struct_lxc_log_appender # /root/lxc-0.7.5/src/lxc/log.h: 78

lxc_log_category = struct_lxc_log_category # /root/lxc-0.7.5/src/lxc/log.h: 89

# No inserted files

