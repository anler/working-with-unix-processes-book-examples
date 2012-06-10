
# Ignoring a signal

puts "My pid: #{Process.pid}"
trap(:INT, "IGNORE")
sleep 1000
