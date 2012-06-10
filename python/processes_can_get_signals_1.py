"""
Trapping SIGCHLD

On posix-compliant platforms, SIGCHLD is the signal sent to a process when a
child process terminates.

I must mention a caveat. signal delivery is unreliable. by
this I mean that if your code is handling a CHLD signal while another proces
dies you may or may not receive a second CHLD signal. This can lead to
inconsistent results with the code snippet below
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
    os.wait()
    dead_processes += 1
    if dead_processes == child_processes:
        print "All children are dead"
        sys.exit()

signal.signal(signal.SIGCHLD, wait_children)

# work it
while True:
    math.floor(math.sqrt(random.randint(1, 44) ** 8))
    time.sleep(1)
