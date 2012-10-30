cmdtest
=======

cmdtest is a simple way to test command line programs.

```python
from cmdtest import Program

cat = Program('cat')

@cat.test
def cat_should_echo_single_file():
    assert cat('hello').out == 'hello'

@cat.test
def cat_should_combine_files():
    assert cat('hello', 'world').out == 'helloworld'

if __name__ == '__main__':
    cat.run()
```
