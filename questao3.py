import threading
import time

class Racer(threading.Thread):
    def __init__(self, racer_id):
        super().__init__()
        self.racer_id = racer_id

    def run(self):
        for _ in range(1000):
            print(f"Racer {self.racer_id} está correndo")
            time.sleep(0.001)
        print(f"Racer {self.racer_id} terminou a corrida")

        import threading

class Race:
    def __init__(self):
        self.racers = []

    def create_racers(self):
        for i in range(1, 11):
            racer = Racer(i)
            self.racers.append(racer)

    def start_race(self):
        odd_racers = []
        even_racers = []

        for racer in self.racers:
            if racer.racer_id % 2 == 0:
                even_racers.append(racer)
            else:
                odd_racers.append(racer)

        for odd_racer in odd_racers:
            odd_racer.start()

        for odd_racer in odd_racers:
            odd_racer.join()

        for even_racer in even_racers:
            even_racer.start()

        for even_racer in even_racers:
            even_racer.join()


# Criando e executando a corrida
race = Race()
race.create_racers()
race.start_race()

