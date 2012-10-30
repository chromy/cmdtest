import os
from functools import wraps
from subprocess import Popen, PIPE
from shutil import rmtree
from tempfile import mkdtemp, mkstemp
from contextlib import contextmanager
import shlex

# this one for us
import attest

# this one for our users
from attest import *


d = None


@contextmanager
def tempdir(*args, **kwargs):
    d = mkdtemp(*args, **kwargs)
    try:
        yield d
    finally:
        rmtree(d)


class File(object):
    def __init__(self, contents='', name=None):
        self.path = None
        self.name = name
        self.contents = contents

    def create(self):
        _, self.path = mkstemp(dir=d)
        print self.path
        with open(self.path, 'w') as f:
            f.write(self.contents)

    @property
    def argument(self):
        return self.path if self.path else ''

    def exists(self):
        try:
            f = open(os.path.join(d, self.name))
        except IOError:
            return False
        else:
            s = f.read()
            f.close()
            return s == self.contents

class NonExistentFile(object):
    def __init__(self):
        self.path = None

    @property
    def argument(self):
        return self.path if self.path else ''

    def exists(self):
        return False

    def create(self):
        self.path = 'not_a_file'


class Text(object):
    def __init__(self, text):
        self.argument = text

    def create(self):
        pass


class Result(object):
    def __init__(self, program, files):
        for f in files:
            f.create()
        arguments = [f.argument for f in files]
        cmd = shlex.split(program)+list(arguments)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=d)

        self.out, self.err = p.communicate()
        self.status = p.returncode


class Program(attest.Tests):
    def __init__(self, path, **kargs):
        attest.Tests.__init__(self, **kargs)
        self.path = path

    def __call__(self, *args):
        files = []
        for arg in args:
            if isinstance(arg, basestring):
                files.append(File(contents=arg))
            else:
                files.append(arg)
        return Result(self.path, files)

    def test(self, func):
        @wraps(func)
        def wrapper():
            global d
            with tempdir() as d:
                func()
        wrapper.__wrapped__ = func
        return super(Program, self).test(wrapper)

