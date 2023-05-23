import threading
import time

class Racer(threading.Thread):
    def __init__(self, racer_id):
        super().__init__()
        self.racer_id = racer_id

    def run(self):
        print(f"Racer {self.racer_id} começou a corrida")
        time.sleep(1)
        print(f"Racer {self.racer_id} terminou a corrida")


class Race:
    def __init__(self):
        self.racers = []

    def create_racers(self):
        for i in range(1, 11):
            racer = Racer(i)
            self.racers.append(racer)

    def start_race(self):
        for racer in self.racers:
            racer.start()

        for racer in self.racers:
            racer.join()


# Criando e executando a corrida
race = Race()
race.create_racers()
race.start_race()


# Alternativa A: quando o codigo foi executado sem usar um tempo de espera, o comportamento foram imprevisiveis,
# como as threads são executadas simutaneamente os prints podem aparecer fora de ordem. 

# Alternativa B: Quando foiadicionado um tempo de espera usando o método time.sleep(), o comportamento do sistema foi
# alterado. O tempo de espera fez com que cada corredor fique inativo por um segundo antes de terminar a corrida. 

# Alternativa C: O Python não possui um método setPriority como o Java, por isso usamos o módulo threading do Python
# para controlar a execução das threads usando semáforos, bloqueios ou condições, com isso não haverá mudanças na execução relacionadas
# ao uso do método setPriority do Java.
