"""
pipe mixed with a fork

System Calls: pipe(2), socketpair(2), recv(2), send(2)
"""
import os


if __name__ == "__main__":
    fd_reader, fd_writer = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(fd_reader)
        for _ in range(10):
            os.write(fd_writer, "Another one bites the dust\n")
    else:
        os.close(fd_writer)
        # so we can read lines
        reader = os.fdopen(fd_reader)
        for line in reader:
            print line, # last comma is for skip the newline added by print
        # clean up zombies
        try:
            while True:
                os.wait()
        except OSError:
            pass
