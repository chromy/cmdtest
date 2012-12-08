from cmdtest import Program, File

touch = Program('touch')

@touch.test
def touch_should_create_file():
    touch('a_file')
    assert File(name='a_file').exists()

if __name__ == '__main__':
    touch.run()

