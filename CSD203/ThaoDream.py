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
                cost = random.randint(0, 200)
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

    def showMatrix(self):
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

    def showAirports(self):
        print("All airports: ", end=" ")
        for airport in self.airports:
            print(airport.name, end=" ")
        print()

    def __toMatrix(self):
        matrix = []
        for item in self.airports:
            matrix.append(item.cost)

        return matrix

    def __dijkstra(self, start, end):
        numNodes = self.size
        distances = {node: float("inf") for node in range(numNodes)}
        distances[start] = 0 # itself weight = 0 
        visited = set() # directed path
        previous = {}
        
        while len(visited) <  numNodes:
            # tim khoang cach nho nhat
            min_distance = float("inf")
            u = None
            for i in range(numNodes):
                if i not in visited and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            # print(u)

            # meet the end node
            if u == end:
                break

            visited.add(u)
            # Relaxation: d[v] = min(d[v], d[u] + (v, u))
            # update weight for all adjency node
            for v in range(numNodes):
                w = self.__toMatrix()[u][v]
                if v not in visited and w > 0:
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        # print(distances[v])
                        previous[v] = u 

        print("Here")
        path = []
        curr = end
        while curr in previous:
            path.append(curr)
            curr = previous[curr]
        path.append(start)
        path.reverse()

        return path, distances[end]
    
    def showPath(self, start, end):
        path, d = self.__dijkstra(start, end)
        print(f"Path: {path[0]}", end=" ")
        for i in range(1, len(path)):
            print("--> ", end=f"{i} ")
        print("")
        print(f"Total cost: {d}")

def menu():
    print("""
        1. Add an airport
        2. Remove an airport
        3. Edit information of airport
        4. Show all airports
    """)

def main():
    system = AirportSystem()
    while True:
        menu()
        option = int(input("Enter option: "))
        if option == 1:
            name = input("Enter name of an airport: ")
            airport = Airport(name)
            system.insert(airport)
        elif option == 2:
            name = input("Enter airport to remove: ")
            system.delete(name)
        elif option == 3:
            name = input("Enter airport to edit information: ")
            system.update(name)
        elif option == 4:
            for airport in system.airports:
                print(airport.name, end=" ")
        elif option == 5:
            break
        else:
            print("Unvalid option!!!")
            continue

if __name__ == "__main__":
    system = AirportSystem()
    for i in range(300):
        system.insert(Airport(str(i)))
    system.showPath(0, 50)
    system.showAirports()

