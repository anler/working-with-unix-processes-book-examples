
require 'socket'

sockets = Socket.pair(:UNIX, :DGRAM, 0)

puts "Paired sockets: #{sockets}"
