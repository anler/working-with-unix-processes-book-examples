"""
Outputs the current process pid and then sleeps for a while
"""
import os
import time

if __name__ == "__main__":
    print "My pid:", os.getpid()
    time.sleep(1000)
