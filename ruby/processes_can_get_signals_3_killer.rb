
# Sends a SIGINT signal to the process with the pid passed as an argument

begin
  pid = Integer(ARGV[0] || "")
rescue ArgumentError
  puts "Usage: ruby program.rb pid_of_a_process"
else
  Process.kill(:INT, pid)
end
