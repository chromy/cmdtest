from cmdtest import Tests
import cat
import head
import echo
import touch

all_tests = Tests()
all_tests.register(cat.cat)
all_tests.register(head.head)
all_tests.register(echo.echo)
all_tests.register(touch.touch)

if __name__ == '__main__':
    all_tests.run()

