"""
Any time that you open a resource in a running process it is assigned a file
descriptor number.
From Wikipedia: A file descriptor is an index for an entry in a
kernel-resident data structure containing the details of all open files
"""

if __name__ == "__main__":
    passwd = open("/etc/passwd")
    print passwd.fileno()

    hosts = open("/etc/hosts")
    print hosts.fileno()

    # Close the open passwd file. This frees up its file descriptor number to
    # be used by the next opened resource/file
    passwd.close()

    null = open("/dev/null")
    print null.fileno()
