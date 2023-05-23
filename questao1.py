import threading

class Racer(threading.Thread):
    def __init__(self, racer_number):
        threading.Thread.__init__(self)
        self.racer_number = racer_number
    
    def run(self):
        while True:
            print("Racer {} - imprimindo".format(self.racer_number))

racer_thread = Racer(1)
racer_thread.start()
