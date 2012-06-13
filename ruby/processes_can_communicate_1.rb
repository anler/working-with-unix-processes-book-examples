# simple pipe

reader, writer = IO.pipe
writer.write("Into the pipe I go...")
# Notice that I had to close the writer after I wrote the pipe because
# when the reader calls read it will continue trying to read data until
# it sees an EOF (end-of-file marker)
writer.close
puts reader.read
