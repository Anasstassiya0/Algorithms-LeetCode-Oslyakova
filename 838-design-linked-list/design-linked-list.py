class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  #ссылка на следующий узел

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0  

    def get(self, index: int) -> int:
        #проверка на корректность индекса
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        #доходим до нужного элемента
        for _ in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head 
        self.head = new_node #обновляем head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        #если список пуст
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node  #добавляем в конец
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #если индекс больше размера
        if index > self.size:
            return
        
        #добавление в начало
        if index == 0:
            self.addAtHead(val)
            return
        
        new_node = Node(val)
        cur = self.head
        
        #доходим до позиции перед вставкой
        for _ in range(index - 1):
            cur = cur.next
        
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        #проверка индекса
        if index < 0 or index >= self.size:
            return
        
        if index == 0:  #удаление первого элемента
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            
            cur.next = cur.next.next
        
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)