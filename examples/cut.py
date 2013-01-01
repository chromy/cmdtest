#! /usr/bin/env python
from cmdtest import Program, assert_hook

cut = Program('cut')

@cut.test
def should_select_field():
    p = cut('-f', '1', _in='a\tb\n')
    assert p.out == 'a\n'

@cut.test
def should_select_multiple_fields():
    p = cut('-f', '1,3', _in='a\tb\tc\n')
    print p.out
    print p.err
    assert p.out == 'a\tc\n'

@cut.test
def should_understand_delimiter():
    p = cut('-f', '1', '-d', ',', _in='a,b\n')
    assert p.out == 'a\n'

if __name__ == '__main__':
    cut.run()

