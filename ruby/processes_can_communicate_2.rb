#
# pipe mixed with a fork
# System Calls: pipe(2), socketpair(2), recv(2), send(2)
#
reader, writer = IO.pipe

fork do
  reader.close

  10.times do
    # heavy lifting
    writer.puts "Another one bites the dust"
  end
end

writer.close
while message = reader.gets
  $stdout.puts message
end

# clean up zombies
begin
  loop do
    pid = Process.wait
  end
rescue
end
