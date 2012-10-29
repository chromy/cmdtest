import os
from subprocess import Popen, PIPE
import shlex
import tempfile

# this one for us
import attest

# this one for our users
from attest import *


class File(object):
    def __init__(self, contents=''):
        self.path = None
        self.contents = contents

    def create(self):
        _, self.path = tempfile.mkstemp()
        with open(self.path, 'w') as f:
            f.write(self.contents)

    def __del__(self):
        if self.path:
            os.remove(self.path)


class NonExistentFile(object):
    def __init__(self):
        self.path = None

    def create(self):
        self.path = 'not_a_file'


class Result(object):
    def __init__(self, program, files):
        for f in files:
            f.create()
        paths = [f.path for f in files]
        cmd = shlex.split(program)+list(paths)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)

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

