class Animal:
    def __init__(self, especie: str, som: str):
        self.especie: str = especie
        self.som: str = som
        self.idade: int = 0

    def __str__(self) -> str:
        return f"{self.especie}:{self.idade}:{self.som}"

    def ageBy(self, incremento: int) -> None:
        if self.idade == 4:
            print(f"warning: {self.especie} morreu")
            return
        self.idade += incremento
        if self.idade >= 4:
            self.idade = 4
            print(f"warning: {self.especie} morreu")

    def makeSound(self):
        if self.idade == 0:
            return "---"
        if self.idade == 4:
            return "RIP"
        return self.som


def main() -> None:
    animal: Animal | None = None
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        line = line.strip()
        if not line:
            continue
        if line.startswith("$"):
            print(line)
            cmd_line = line[1:].lstrip()
        else:
            print(f"${line}")
            cmd_line = line
        args = cmd_line.split()
        if len(args) == 0:
            continue
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "init":
            if len(args) >= 3:
                especie, som = args[1], args[2]
                animal = Animal(especie, som)
        elif cmd == "show":
            if animal:
                print(animal)
        elif cmd == "grow":
            if animal and len(args) >= 2:
                try:
                    incremento = int(args[1])
                except ValueError:
                    incremento = 0
                animal.ageBy(incremento)
        elif cmd == "noise":
            if animal:
                print(animal.makeSound())


if __name__ == "__main__":
    main()