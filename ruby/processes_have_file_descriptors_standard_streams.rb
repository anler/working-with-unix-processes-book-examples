# Every Unix process comes with three open resources:
# The standard input (stdin)
# The standard output (stdout)
# The standard error (stderr)
# Before these existed your program had to include a keyboard driver for all
# the keyboards it wanted to support, and if it wanted to print something to
# the screen it had to know how to manipulate the pixels required to do so
# System calls
# open(2), close(2), read(2), write(2), pipe(2), fsync(2), stat(2)

puts STDIN.fileno
puts STDOUT.fileno
puts STDERR.fileno
