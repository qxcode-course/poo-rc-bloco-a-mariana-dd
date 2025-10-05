class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        else:
            return 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            self.wetness = self.getMaxWetness()
            print("toalha encharcada")

    def wringOut(self):
        self.wetness = 0

    def isDry(self):
        return self.wetness == 0

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"


def main():
    towel = None
    while True:
        try:
            line = input()
            if not line:
                continue

            print(f"${line}")  # Mostra o comando como o verificador espera
            parts = line.strip().split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "criar":
                if len(parts) < 3:
                    print("Uso: criar <cor> <tamanho>")
                    continue
                color = parts[1]
                size = parts[2]
                if size not in ["P", "M", "G"]:
                    print("Tamanho inválido. Use P, M ou G.")
                    continue
                towel = Towel(color, size)

            elif cmd == "mostrar":
                if towel:
                    print(towel)
                else:
                    print("Nenhuma toalha criada.")

            elif cmd == "seca":
                if towel:
                    print("sim" if towel.isDry() else "nao")
                else:
                    print("Nenhuma toalha criada.")

            elif cmd == "torcer":
                if towel:
                    towel.wringOut()
                else:
                    print("Nenhuma toalha criada.")

            elif cmd in ["secar", "enxugar"]:
                if towel:
                    if len(parts) < 2:
                        print(f"Uso: {cmd} <quantidade>")
                        continue
                    try:
                        amount = int(parts[1])
                        towel.dry(amount)
                    except ValueError:
                        print("Quantidade inválida.")
                else:
                    print("Nenhuma toalha criada.")

            else:
                print("Comando inválido")

        except EOFError:
            break


if __name__ == "__main__":
    main()