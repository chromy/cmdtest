from attest import Tests
from cmdtest import Program, File

head = Program('head -n10')

@head.test
def head_should_output_small_file():
    f = File(text='hello')
    assert head(f).out == 'hello'

@head.test
def head_should_output_10_lines_of_big_file():
    f = File(text='abc\n'*1000)
    output = head(f).out
    assert output.count('\n') == 10
    assert output == f.text[:len(output)]

if __name__ == '__main__':
    head.run()

