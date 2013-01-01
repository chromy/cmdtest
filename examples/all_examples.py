#! /usr/bin/env python
from cmdtest import Tests
import cat
import head
import echo
import touch
import sleep
import cut

all_examples = Tests()
all_examples.register(cat.cat)
all_examples.register(head.head)
all_examples.register(echo.echo)
all_examples.register(touch.touch)
all_examples.register(sleep.sleep)
all_examples.register(cut.cut)

if __name__ == '__main__':
    all_examples.run()

