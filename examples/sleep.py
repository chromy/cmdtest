#! /usr/bin/env python
from cmdtest import Program, raises, TimeoutError

sleep = Program('sleep')

@sleep.test
def should_eventully_raise_timeout():
    with raises(TimeoutError) as error:
        sleep('4')

@sleep.test
def can_set_time_out():
   assert sleep('0', _timeout=0.5).status == 0

if __name__ == '__main__':
    sleep.run()

