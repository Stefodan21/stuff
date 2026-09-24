class Room:
    def __init__(self, name: str, color: str, width: float, length: float, temperature: float):
        self.name = name
        self.color = color
        self.width = width
        self.length = length
        self.temperature = temperature

    def area(self) -> float:
        return self.width * self.length

    def setColor(self, color: str) -> None:
        self.color = color

    def getColor(self) -> str:
        return self.color

    def setTemperature(self, temperature: float) -> None:
        self.temperature = temperature

    def getTemperature(self) -> float:
        return self.temperature


kitchen = Room("kitchen", "Blue", 10.5, 12.0, 77.0)

area: float = kitchen.area()

kitchen.setColor("blue")

new_temp: float = kitchen.getTemperature() + 3.0
kitchen.setTemperature(new_temp)

print(f"Color: {kitchen.getColor()}  Area: {area:.2f}  Temp: {kitchen.getTemperature():.2f}")
