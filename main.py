class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")


class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.__gadgets = gadgets  # private attribute

    def show_gadgets(self):
        print(f"{self.name}'s gadgets: {', '.join(self.__gadgets)}")

    def use_power(self):
        print(f"{self.name} deploys {self.power} using high-tech gear!")

superman = FlyingHero("Superman", "Super Strength", "Krypton", 3000)
ironman = TechHero("Iron Man", "Repulsor Beams", "Earth", ["Suit", "AI", "Missiles"])

superman.introduce()
superman.use_power()

ironman.show_gadgets()
