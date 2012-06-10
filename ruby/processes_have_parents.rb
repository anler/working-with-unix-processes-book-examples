# Print the pid of the parent process of the current process
# Process.ppid maps to getppid(2)

puts "My parent pid: #{Process.ppid}"
