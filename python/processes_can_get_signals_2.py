"""
Trapping SIGCHLD

On posix-compliant platforms, SIGCHLD is the signal sent to a process when a
child process terminates.

Here's a rewrite of the code from processes_can_get_signals_1 that won't
miss any child process deaths
"""
import os
import sys
import signal
import time
import math
import random

child_processes = 3
dead_processes = 0

def do_work():
    time.sleep(3)

# we fork 3 child processes
for _ in range(child_processes):
    pid = os.fork()
    if pid == 0:
        do_work()
        os._exit(0)
    else:
        print "Spawned child with pid", pid

# our parent process will be busy doing some intense math
# but still wants to know when one of its children exits
def wait_children(signum, frame):
    global dead_processes
    print "A child has died"
    try:
        while True:
            pid, exit_status = os.waitpid(-1, os.WNOHANG)
            if pid:
                dead_processes += 1
            else:
                break
            if dead_processes == child_processes:
                print "All children are dead"
                sys.exit()
    except OSError:
        # Process.wait will raise Errno::ECHILD if no child processes exist.
        # Since signals might arrive at any time it's possible for the last
        # SIGCHLD signal to arrive after the previous CHLD handler has already
        # called Process.wait twice and gotten the last available status.
        pass

signal.signal(signal.SIGCHLD, wait_children)

# work it
while True:
    math.floor(math.sqrt(random.randint(1, 44) ** 8))
    time.sleep(1)
