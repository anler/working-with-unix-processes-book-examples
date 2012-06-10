# Any time that you open a resource in a running process it is assigned a file
# descriptor number.
# From Wikipedia: A file descriptor is an index for an entry in a
# kernel-resident data structure containing the details of all open files

passwd = File.open("/etc/passwd")
puts passwd.fileno

hosts = File.open("/etc/hosts")
puts hosts.fileno

# Close the open passwd file. This frees up its file descriptor number to be
# used by the next opened resource/file
passwd.close

null = File.open("/dev/null")
puts null.fileno
