

def write_log(message):
    f = open('C:\Users\loridcon\AppData\Roaming\Ableton\Live 8.3\Preferences\log.txt','a')
    f.write(message)
    f.write("\n")
    f.close()
