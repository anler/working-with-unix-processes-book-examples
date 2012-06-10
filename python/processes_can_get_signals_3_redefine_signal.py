"""
This process won't exit when it receives an INT signal so in orther to stop
it you have to issue preferably a signal that cannot be trapped, blocked or
ignored: KILL and STOP
"""
import sys
import os
import signal
import time


def interrupt_handler(signum, frame):
    print "Na na na, you can't get me"


if __name__ == "__main__":
    print "My pid:", os.getpid()
    signal.signal(signal.SIGINT, interrupt_handler)
    # here we are using an infinite loop because otherwise the signal
    # interrupts the sleep function and finish the script
    while True:
        time.sleep(1000)
