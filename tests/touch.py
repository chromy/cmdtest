from cmdtest import Program, File, Text

touch = Program('touch')

@touch.test
def touch_should_create_file():
    from cmdtest import d
    print d
    touch(Text('a_file'))
    assert File(name='a_file').exists()

if __name__ == '__main__':
    touch.run()

