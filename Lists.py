# Односвязный список
class LinkedList:
    head = None
    length = 0

    class Node: # Класс - узел списка
        element = None
        nextNode = None
        def __init__(self, argElement, argNextNode = None):
            self.element = argElement
            self.nextNode = argNextNode

    def append(self, argElement):
        if not self.head:
            self.head = self.Node(argElement)
            self.length += 1
            return argElement
        tmpNode = self.head
        while tmpNode.nextNode:
            tmpNode = tmpNode.nextNode
        tmpNode.nextNode = self.Node(argElement)
        self.length += 1
        return argElement

    def output(self):
        i = 0
        tmpNode = self.head
        while tmpNode.nextNode:
            print(f"Index -> {i}; Value -> {tmpNode.element};")
            tmpNode = tmpNode.nextNode
            i += 1
        print(f"Index -> {i}; Value -> {tmpNode.element};")

    def insert(self, argElement, argIndex):
        i = 0
        prvNode = tmpNode = self.head
        while  i < argIndex:
            prvNode = tmpNode
            tmpNode = tmpNode.nextNode
            i += 1
        prvNode.nextNode = self.Node(argElement, argNextNode=tmpNode)
        self.length += 1
        return argElement

    def __getitem__(self, argIndex):
        i = 0
        prvNode = tmpNode = self.head
        while  i < argIndex:
            prvNode = tmpNode
            tmpNode = tmpNode.nextNode
            i += 1
        return prvNode.element

    def __setitem__(self, argIndex, argElement):
        i = 0
        prvNode = tmpNode = self.head
        while  i < argIndex:
            prvNode = tmpNode
            tmpNode = tmpNode.nextNode
            i += 1
        tmpNode.element = argElement

    def remove(self, argIndex):
        prvNode = tmpNode = self.head
        i = 0
        while i < argIndex:
            prvNode = tmpNode
            tmpNode = tmpNode.nextNode
            i += 1
        prvNode.nextNode = tmpNode.nextNode
        delElement = tmpNode.element
        del tmpNode
        return delElement

    def __len__(self):
        return self.length