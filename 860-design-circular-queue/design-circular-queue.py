class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k # массив фиксированного размера
        self.k = k
        self.front = 0       
        self.rear = 0 # индекс, куда будем вставлять следующий
        self.count = 0 # текущее количество элементов

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False # очередь заполнена
        
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k # двигаемся по кругу
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False # очередь пустая
        
        self.front = (self.front + 1) % self.k # сдвигаем начало
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.q[self.front] # первый элемент

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        # последний добавленный элемент
        return self.q[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()