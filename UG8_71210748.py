class CircularQueue:

    def __init__(self,capacity):
        self.data = list()
        self.size = 0
        self.front = -1
        self.capacity = capacity
    
    def enqueue(self,d):
        if self.size < self.capacity:
            self.data.append(d)
            self.size += 1
            self.front = 0
    
    def dequeue(self):
        if self.size > 0:
            hasil = self.data[self.front]
            self.data.pop(self.front)
            self.size -= 1
            print("data ",hasil,"terhapus!")
        else:
            print("kosong!")
        return hasil

    def __len__(self):
        return self.size

    def front(self):
        return self.data[self.front]

    def display(self):
        if self.size < self.capacity:
            antrian = list()
            for d in self.data:
                antrian.append(d)
            print("Yang ada pada antrian adalah: ",end='')
        else:
            print("Yang pada antrian circular adalah: ",end='')
            for d in self.data:
                print(d, " ",end='')
                print("Antrian penuh")

circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print("Data yang dihapus adalah = ", circularQueue.dequeue())
print("Data yang dihapus adalah = ", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()