import random
class Airport:
    def __init__(self, name: str):
        self.name = name
        self.cost = [0]
        self.number = 0

class AirportSystem:
    def __init__(self):
        self.airports = []
        self.size = 0

    def __getAirport(self, name: str):
        selectedAirport = None
        for airport in self.airports:
            if airport.name == name:
                selectedAirport = airport
        if not selectedAirport:
            print("Unexisted airport!!")
        return selectedAirport

    def insert(self, newAirport: Airport | str):
        if isinstance(newAirport, str):
            newAirport = Airport(newAirport)

        if self.airports:
            newAirport.number = self.size
            for i in range(self.size):
                # cost = int(input(f"Enter cost from {newAirport.name} to {self.airports[i].name}: "))
                cost = random.randint(0, 100)
                print(f"Enter cost from {newAirport.name} to {self.airports[i].name}: ", cost)
                self.airports[i].cost.append(cost)
                newAirport.cost.insert(i, cost)
            self.airports.append(newAirport)
        else:
            self.airports.append(newAirport)
        self.size += 1

    def delete(self, name: str):
        number = 0
        for airport in self.airports:
            if airport.name == name:
                number = airport.number
        self.airports.pop(number)
        self.size -= 1

        for i in range(self.size):
            self.airports[i].cost.pop(number)
            self.airports[i].number = i

    def update(self, name: str):
        airport = self.__getAirport(name)
        for i in range(self.size):
            if i != airport.number:
                cost = random.randint(0, 100)
                self.airports[i].cost[airport.number] = cost
                airport.cost[i] = cost 

    def display(self):
        space = 3
        matrix = self.__toMatrix()
        print(" " * (space), end=" ")
        for i in range(self.size):
            print(f" {self.airports[i].name.ljust(space)}", end= " ")
        print()

        for i in range(self.size):
            print(self.airports[i].name.ljust(space), end= "|")
            for j in range(self.size):
                print(f" {str(matrix[i][j]).ljust(space)}", end="|")
            
            print()

    def __toMatrix(self):
        matrix = []
        for item in self.airports:
            matrix.append(item.cost)

        return matrix

    def findPath(self):
        pass

def menu():
    pass

if __name__ == "__main__":
    system = AirportSystem()
    system.insert("a")
    system.insert("b")
    system.insert("c")
    system.insert("d")
    system.insert("e")
    system.display()