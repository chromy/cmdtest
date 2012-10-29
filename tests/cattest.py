from cmdtest import Program

cat = Program('cat')
assert cat('hello') == 'hello'
assert cat('hello', 'world') == 'helloworld'

