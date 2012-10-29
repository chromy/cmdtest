import subprocess
import tempfile

class Program(object):
    def __init__(self, path):
        pass

    def __call__(self, *args):
        files, names = zip(*[tempfile.mkstemp() for arg in args])
        for name, txt in zip(names, args):
            with open(name, 'w') as f:
                f.write(txt)
        return subprocess.check_output(['cat']+list(names))
