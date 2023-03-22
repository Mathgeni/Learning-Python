import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, z):
        super().append(z)
        self.log(z)


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
