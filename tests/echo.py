from cmdtest import Program, Text, assert_hook

echo = Program('echo')

@echo.test
def echo_string_should_output_string():
    assert echo(Text('foo')).out == 'foo\n'

if __name__ == '__main__':
    echo.run()
