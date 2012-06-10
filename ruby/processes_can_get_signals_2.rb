# Trapping SIGCHLD
#
# On posix-compliant platforms, SIGCHLD is the signal sent to a process when a
# child process terminates.
#
# Here's a rewrite of the code from processes_can_get_signals_1 that won't
# miss any child process deaths

child_processes = 3
dead_processes = 0

# we fork 3 child processes
child_processes.times do
  fork do
    sleep 3
  end
end

# Sync $stdout so the call to #puts in the CHLD handler isn't buffered. Can
# cause a ThreadError if a signal handler is interrupted after calling #puts.
# Always a good idea to do this if your handlers will be doing IO
$stdout.sync = true

# our parent process will be busy doing some intense math
# but still wants to know when one of its children exits
trap(:CHLD) do
  # since Process.wait queues up any data that it has for use we can ask for it
  # here, since we know that one of our child processes has exited

  # we loop over a non-blocking Process.wait to ensure that any dead child
  # processes are counted for
  begin
    while pid = Process.wait(-1, Process::WNOHANG)
      puts pid
      dead_processes += 1
      # we exit explicitly once all the child processes are accounted for
      exit if dead_processes == child_processes
    end
  rescue Errno::ECHILD
    # Process.wait will raise Errno::ECHILD if no child processes exist.
    # Since signals might arrive at any time it's possible for the last
    # CHLD signal to arrive after the previous CHLD handler has already called
    # Process.wait twice and gotten the last available status.
  end
end

# work it
loop do
  (Math.sqrt(rand(44)) ** 8).floor
  sleep 1
end
