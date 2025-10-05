class Calculadora:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, value: int):
        self.battery = min(self.battery + value, self.batteryMax)

    def useBattery(self) -> bool:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return False
        self.battery -= 1
        return True

    def sum(self, a: float, b: float):
        if self.useBattery():
            self.display = a + b

    def div(self, a: float, b: float):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return       
        self.battery -= 1

        if b == 0:
            print("fail: divisao por zero")
            return

        self.display = a / b



def main():
    calc = None
    while True:
        try:
            line = input().strip()
            if not line:
                continue

            print(f"${line}")
            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break
            elif cmd == "init":
                calc = Calculadora(int(parts[1]))
            elif cmd == "show":
                print(calc)
            elif cmd == "charge":
                if calc is not None:
                   calc.charge(int(parts[1]))
            elif cmd == "sum":
                if calc is not None:
                   calc.sum(float(parts[1]), float(parts[2]))
            elif cmd == "div":
                if calc is not None:
                   calc.div(float(parts[1]), float(parts[2]))
        except EOFError:
            break

if __name__ == "__main__":
      main()

      