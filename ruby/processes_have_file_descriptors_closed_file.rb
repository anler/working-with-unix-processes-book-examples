# It's important to note that file descriptors keep track of open resources
# only. Closed resources are not given a file descriptor number.

passwd = File.open("/etc/passwd")
puts passwd.fileno
passwd.close
puts passwd.fileno
