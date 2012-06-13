"""
Simple pipe
"""
import os


if __name__ == "__main__":
    file_descriptor_reader, file_descriptor_writer = os.pipe()
    reader = os.fdopen(file_descriptor_reader)
    writer = os.fdopen(file_descriptor_writer, "w")
    writer.write("Into the pipe I go...")
    # Notice that I had to close the writer after I wrote the pipe because
    # when the reader calls read() it will continue trying to read data until
    # it sees an EOF (end-of-file marker)
    writer.close()
    print reader.read()

    # Also you can work with the file descriptors directly
    # os.write(file_descriptor_writer, "Into the pipe I go...")
    # os.close(file_descriptor_writer)
    # while True:
    #     data = os.read(file_descriptor_reader, 255)
    #     if not data: # EOF
    #         break
    #     print data

