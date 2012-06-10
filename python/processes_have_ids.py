"""
Print the pid of the current process

os.getpid() mapts to getpid(2)
"""
import os

if __name__ == "__main__":
    print "My pid:", os.getpid()
