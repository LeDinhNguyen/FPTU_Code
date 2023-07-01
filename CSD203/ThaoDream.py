class Airport:
    def __init__(self, name):
        self.name = name
        self.cost = [0]
        self.number = 0


class AirportSystem:
    def __init__(self):
        self.airports = []

    def insert(self, name: str, **destinations: dict):
        if name in self.airports:
            print("Existing airport")
        else:
            self.airports[name] = destinations

    def delete(self, name):
        if name not in self.airports:
            print("Unexisted airport")
        else:
            self.airports.pop(name)

    def update(self, name: str):
        if name not in self.airports:
            print("Unexisted airport")
        else:
            for item in self.airports[name]:
                updateAirport = input("Enter destination")
                cost = int(input(f"Enter cost of {updateAirport}"))
                self.airports[name][updateAirport] = cost
    def display(self):
        for i in self.airports:
            print(f"{i}: {self.airports[i]}")

    def __toMatrix(self):
        pass

    def findPath(self):
        pass

if __name__ == "__main__":
    a = AirportSystem()
    a.insert("A")
    a.insert("B")
    a.insert("C")
    a.delete("C")
    airports = {
        'A': {
            'B': 10, 
            'C': 20
        },
        'B': {
            "C": 10
        },
        'C': {
            "A": 30
        }
    }
    a.insert(airports)
    a.display()