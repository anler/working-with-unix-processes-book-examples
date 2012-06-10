
# This process won't exit when it receives an INT signal so in orther to stop
# it you have to issue preferably a signal that cannot be trapped, blocked or
# ignored: KILL and STOP

puts "My pid: #{Process.pid}"
trap(:INT) { puts "Na na na, you can't get me" }
sleep 1000
