"""
It's important to note that file descriptors keep track of open resources
only. Closed resoruces are not given a file descriptor number.
"""


if __name__ == "__main__":
    passwd = open("/etc/passwd")
    print passwd.fileno()
    passwd.close()
    print passwd.fileno()
