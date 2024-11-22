Class Character:
    def __init__(self, name, health, energy, weapon):
        self.name = name
        self.health = health
        self.energy = energy
        self.weapon = weapon

    def attack(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} attacks {self.weapon}. energy decreased!")
        else:
            print("not enough energy!")

    def take_damdage(self, damage):
        self.health -=take_damdage
        if self.health <= 0
            print(f"character {self.character}, died. (NAUUURR)")
        elde:
        print(f"{self.name} got {damage}, current health {self.health}")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equiped new weapon, {self.weapon}")

    def get_status(self):
        return f"character {self.name}: Health = {self.health}, Energy = {self.energy}, Weapon = {self.weapon}"

character = Character("Dabloon-cat", 100, 50, "sword")

print(character.get_status())

character.attack()

character.take_damage(30)

character.equip_weapon(bow)

print(character.get_status())

character.attack()

character.take_damage(120)

# +120 dabloons for reading this <3