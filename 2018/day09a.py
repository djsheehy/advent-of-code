players = [0] * 447
last_marble = 7151000
turn = 0

class Marble:
    def __init__(self, value):
        self.value = value
        self.prev = self
        self.next = self
    
    def insert(self, value):
        m = Marble(value)
        a = self.prev
        b = self
        m.prev = a
        m.next = b
        a.next = m
        b.prev = m
        return m
    
    def remove(self):
        a = self.prev
        b = self.next
        a.next = b
        b.prev = a
        return b

m = Marble(0)
for i in range(1,last_marble+1):
    if i % 23 != 0:
        m = m.next
        m = m.next
        m = m.insert(i)
    else:
        players[turn] += i
        for j in range(7):
            m = m.prev
        players[turn] += m.value
        m = m.remove()
    turn = (turn + 1) % len(players)
print(max(players))