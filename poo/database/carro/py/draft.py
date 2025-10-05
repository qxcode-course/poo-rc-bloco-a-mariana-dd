class Carro:
    def __init__(self):
        self.passageiros: int = 0
        self.passMax: int = 2
        self.gasolina: int = 0
        self.gasolinaMax: int = 100
        self.km: int = 0

    def __str__(self):
        return f"pass: {self.passageiros}, gas: {self.gasolina}, km: {self.km}"

    def entrar(self):
        if self.passageiros < self.passMax:
            self.passageiros += 1
            return True
        print("fail: limite de pessoas atingido")
        return False

    def sair(self):
        if self.passageiros > 0:
            self.passageiros -= 1
            return True
        print("fail: nao ha ninguem no carro")
        return False

    def fuel(self, quantidade: int) -> bool:
        self.gasolina = min(self.gasolina + quantidade, self.gasolinaMax)
        return True

    def drive(self, distancia: int) -> bool:
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return False

        if self.gasolina == 0:
            print("fail: tanque vazio")
            return False

        if self.gasolina >= distancia:
            self.gasolina -= distancia
            self.km += distancia
            return True
        else:
            km_rodado: int = self.gasolina
            self.km += km_rodado
            self.gasolina = 0

            if km_rodado > 0:
                print(f"fail: tanque vazio apos andar {km_rodado} km")
            else:
                print("fail: tanque vazio")
            return False


def main():
    carro = Carro()

    try:
        while True:
            line = input()
            line = line.strip()

            if not line:
                continue

            print(f"${line}")

            parts = line.split()
            cmd = parts[0]

            if cmd == "show":
                print(carro)
            elif cmd == "enter":
                carro.entrar()
            elif cmd == "leave":
                carro.sair()
            elif cmd == "fuel":
                if len(parts) > 1:
                    try:
                        quantidade = int(parts[1])
                        carro.fuel(quantidade)
                    except ValueError:
                        pass
            elif cmd == "drive":
                if len(parts) > 1:
                    try:
                        distancia = int(parts[1])
                        carro.drive(distancia)
                    except ValueError:
                        pass
            elif cmd == "end":
                break
    except EOFError:
        pass
    except:
        pass


if __name__ == "__main__":
    main()