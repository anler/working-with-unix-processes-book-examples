"""
Print the pid of the parent process of the current process

os.getppid() maps to getppid(2)
"""
import os


if __name__ == "__main__":
    print "My parent pid:", os.getppid()
