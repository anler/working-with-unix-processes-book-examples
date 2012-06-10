"""
Ignoring a signal
"""
import os
import signal
import time


if __name__ == "__main__":
    print "My pid:", os.getpid()
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    time.sleep(1000)
