from cmdtest import Program, NonExistentFile, File

cat = Program('cat')

@cat.test
def cat_should_echo_single_file():
    a = File(text='hello')
    assert cat(a).out == 'hello'

@cat.test
def cat_should_combine_files():
    a = File(text='hello')
    b = File(text='world')
    assert cat(a, b).out == 'helloworld'

@cat.test
def cat_should_not_write_to_stderr():
    a = File(text='hello')
    b = File(text='world')
    assert cat(a, b).err == ''

@cat.test
def cat_should_succeed():
    a = File(text='hello')
    assert cat(a).status == 0

@cat.test
def cat_should_fail_with_bad_files():
    result = cat(NonExistentFile())
    assert result.err != ''
    assert result.status != 0

if __name__ == '__main__':
    cat.run()

