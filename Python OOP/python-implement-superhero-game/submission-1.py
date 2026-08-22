class Hero:
    def __init__(self, name: str, power_level: int, health: int) -> None:
        self.name = name
        self.power_level = power_level
        self.health = health

    def use_power(self) -> str:
        return f"{self.name} uses their power!"


class FlightHero(Hero):
    def __init__(self, flight_speed: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.flight_speed = flight_speed

    def use_power(self) -> str:
        return f"{self.name} flies at {self.flight_speed} mph!"


class StrengthHero(Hero):
    def __init__(self, lifting_capacity: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.lifting_capacity = lifting_capacity

    def use_power(self) -> str:
        return f"{self.name} lifts {self.lifting_capacity} pounds!"


flight_hero = FlightHero(name="Superman", power_level=10, health=100, flight_speed=1000)
strength_hero = StrengthHero(name="Hulk", power_level=10, health=100, lifting_capacity=1000)

print(flight_hero.name)
print(flight_hero.power_level)
print(flight_hero.health)
print(flight_hero.flight_speed)
print(flight_hero.use_power())

print(strength_hero.name)
print(strength_hero.power_level)
print(strength_hero.health)
print(strength_hero.lifting_capacity)
print(strength_hero.use_power())
