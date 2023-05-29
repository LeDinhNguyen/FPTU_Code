class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class CirclyLinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def insertFirst(self):
        pass

    def insertLast(self):
        pass

    def insertAfter(self):
        pass

    def removeFirst(self):
        pass

    def removeLast(self):
        pass

    def removeAfter(self):
        pass

    def checkValue(self, value: int) -> bool:
        temp = self.tail.next
        while temp != self.tail:
            temp = temp.next
            if temp.data == value:
                return True
        return False

    def display(self) -> None:
        temp = self.tail.next
        while temp != self.tail:
            temp = temp.next
            print(temp.value, end=" ")
            
    def search(self, value: int) -> True:
        temp = self.tail.next
        count = 0
        while temp != self.tail:
            if temp.value == value:
                print(count, end=" ")
            temp = temp.next
            count += 1


def main():
    pass

if __name__ == "__main__":
    main()
