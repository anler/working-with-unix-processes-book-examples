# Trapping SIGCHLD
#
# On posix-compliant platforms, SIGCHLD is the signal sent to a process when a
# child process terminates.
#
# before we go on I must mention a caveat. signal delivery is unreliable. by
# this I mean that if your code is handling a CHLD signal while another process
# dies you may or may not receive a second CHLD signal. This can lead to
# inconsistent results with the code snippet below


child_processes = 3
dead_processes = 0

# we fork 3 child processes
child_processes.times do
  fork do
    sleep 3
  end
end

# our parent process will be busy doing some intense math
# but still wants to know when one of its children exits
trap(:CHLD) do
  # since Process.wait queues up any data that it has for use we can ask for it
  # here, since we know that one of our child processes has exited
  puts Process.wait
  dead_processes += 1
  # we exit explicitly once all the child processes are accounted for
  exit if dead_processes == child_processes
end

# work it
loop do
  (Math.sqrt(rand(44)) ** 8).floor
  sleep 1
end
