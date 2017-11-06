class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

---------------------------------------

def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)

	equal=True

	while chardeque.size() > 1 and equal:
		first = chardeque.removeRear()
		last = chardeque.removeFront()
		if first == last:
			equal = False

	return equal

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))



------------------------------------------

