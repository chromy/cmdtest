from cmdtest import Program, NonExistentFile

cat = Program('cat')

@cat.test
def cat_should_echo_single_file():
    assert cat('hello').out == 'hello'

@cat.test
def cat_should_combine_files():
    assert cat('hello', 'world').out == 'helloworld'

@cat.test
def cat_should_not_write_to_stderr():
    assert cat('hello', 'world').err == ''

@cat.test
def cat_should_succeed():
    assert cat('hello').status == 0

@cat.test
def cat_should_fail_with_bad_files():
    result = cat(NonExistentFile())
    assert result.err != ''
    assert result.status != 0

if __name__ == '__main__':
    cat.run()

