class NPC:
    def __init__(self, name, level, health, strength, faction):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.faction = faction

    def __repr__(self):
        return f"{self.name} | lvl:{self.level} | hp:{self.health} | str:{self.strength} | {self.faction}"

    def __eq__(self, other):
        if not isinstance(other, NPC):
            return False
        return (
            self.name == other.name and
            self.level == other.level and
            self.health == other.health and
            self.strength == other.strength and
            self.faction == other.faction
        )


def main():

    npcs = [
        NPC("Aragorn", 10, 150.5, 80, "Warrior"),
        NPC("Gandalf", 20, 100.0, 95, "Mage"),
        NPC("Legolas", 15, 120.0, 70, "Archer"),
        NPC("Gimli", 15, 200.0, 85, "Warrior"),
        NPC("Frodo", 5, 80.0, 30, "Hobbit")
    ]

    print("Початковий масив:")
    for npc in npcs:
        print(npc)
    npcs_sorted = sorted(npcs, key=lambda x: (x.level, -x.health))

    print("\nВідсортований масив (level ↑, health ↓):")
    for npc in npcs_sorted:
        print(npc)
    target = NPC("Gandalf", 20, 100.0, 95, "Mage")

    found = False
    for npc in npcs_sorted:
        if npc == target:
            print("\nЗнайдено ідентичний об'єкт:")
            print(npc)
            found = True
            break

    if not found:
        print("\nІдентичний об'єкт не знайдено")


if __name__ == "__main__":
    main()
