# from StudentManagement import Student
class Student:
    def __init__(self, id: str, name: str, mark: int) -> None:
        self.__id: str = id
        self.__name: str = name
        self.__mark: int = mark

    def setID(self, id: str):
        self.__id = id

    def getID(self):
        return self.__id

    def setName(self, name: str):
        self.__name = name

    def getName(self):
        return self.__name

    def setMark(self, mark: int):
        self.__mark = mark

    def getMark(self):
        return self.__mark
    
    def create(self):
        id = input("Enter new student ID: ")
        name = input("Enter new student name: ")
        mark = int(input("Enter new student mark: "))


class Node:
    def __init__(self, stu):
        self.__value = stu
        self.__next = None

    def getNext(self):
        return self.__next
    
    def setNext(self, newNode):
        self.__next = newNode
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value: int):
        self.__value = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0
        self.__tail = 0

    def getSize(self):
        return self.__size

    def __insertFirst(self, value: int):
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        else:
            newNode.setNext(self.__head)
            self.__head = newNode
        self.__size += 1
        return True

    def append(self, value: int):
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        else:
            temp = self.__head
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(newNode)
        self.__size += 1
        return True

    def insertion(self, value: int, index: int):
        if self.__size == 0:
            return self.append(value)
        elif index > self.__size or index < 0:
            print("Index is out of linked list!!!")
            return False
        elif index == 0:
            return self.__insertFirst(value)
        elif index == self.__size:
            return self.append(value)
        else:
            temp = self.__head
            newNode = Node(value)
            while index > 1:
                temp = temp.getNext()
                index -= 1
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)
            self.__size += 1

    def __deleteFirst(self):
        if self.__head is None:
            print("There is no element in the linked list to remove!!!")
            return False
        else:
            temp = self.__head
            self.__head = self.__head.getNext()
            temp = None
            self.__size -= 1
        return True

    def __deleteLast(self):
        if self.__head is None:
            print("There is no element in the linked list to remove!!!")
        else:
            temp = self.__head
            last = temp.getNext()
            while last.getNext() is not None:
                temp = temp.getNext()
                last = last.getNext()
            temp.setNext(None)
            self.__size -= 1
        return True

    def deletion(self, index: int):
        if self.__head == None and index >= self.__size:
            return False
        elif index == 0:
            return self.__deleteFirst()
        elif index == self.__size - 1:
            return self.__deleteLast()
        else:
            temp = self.__head
            while index > 1:
                temp = temp.getNext()
                index -= 1
            deleteNode = temp.getNext()
            temp.setNext(deleteNode.getNext())
            deleteNode.getNext()
            self.__size -= 1
        return True

    def update(self, value: int, index: int):
        if index >= self.__size:
            print("Index is out of linked list!!!")
        else:
            count = 0
            temp = self.__head
            while temp != None:
                temp = temp.__next
                count += 1
                if (count == index):
                    temp.setValue(value)
                    return 1
            return -1

    def searchByValue(self, value: int) -> int:
        index = 0
        p = self.__head
        while p:
            if p.getValue() == value:
                return index
            p = p.getNext()
            index += 1
        return 0
    
    def searchByIndex(self, index: int):
        if index >= self.__size:
            print("Index is out of linked list!!!")
            return False
        else:
            temp = self.__head
            for i in range(index):
                temp = temp.getNext()
            print(temp.getValue())
        return True
    

    def show(self):
        p = self.__head
        while p != None:
            print(p.getValue(), end=" ")
            p = p.getNext()
        print("")
        return True

def main():
    linkedArray = SinglyLinkedList() # create linked list
    linkedArray.append(1)
    linkedArray.append(2)
    linkedArray.append(3)
    linkedArray.append(4)
    linkedArray.insertion(5, 3)
    linkedArray.deletion(3)
    linkedArray.searchByIndex(3)
    
    linkedArray.show() # print linked list
    size = linkedArray.getSize()
    print("size: ",size)

if __name__ == "__main__":
    main()