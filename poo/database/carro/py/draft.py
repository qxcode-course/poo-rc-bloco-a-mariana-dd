class car:
    def __init__(self):
        self.passengers = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
        self.km = 0

    def __str__(self) -> str:
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.passengers < self.passMax:
            self.passengers += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self) -> None:
        if self.passengers > 0:
            self.passengers -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount: int) -> None:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.passengers == 0:
            print("fail: nao ha ningue no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas < distance:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
            self.km += distance
            self.gas -= distance

def main() -> None:
    car = car()
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        if line.startswith("$"):
            print(line)
            cmd_line = line[1:].strip()
        else:
            print(f"${line}")
           cmd_line = line
        args = cmd_line.split()
        cmd = args[0] 
        if cmd == "end":
            break
        elif cmd == "show":
            print(car)
        elif cmd == "enter":
            car.enter()
        elif cmd == "leave":
            car.leave()
        elif cmd == "fuel":
            car.fuel(int(args[1]))
        elif cmd == "drive":
            car.drive(int(args[1]))

if __name__ == "__main__":
    main()