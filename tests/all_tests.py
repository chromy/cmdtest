from cmdtest import Tests
import cat
import head

all_tests = Tests()
all_tests.register(cat.cat)
all_tests.register(head.head)

if __name__ == '__main__':
    all_tests.run()

