class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self)
		return self.items.pop()

	def size(self):
		return len(self.items)

假定队尾在列表中的位置为 0。这允许我们使用列表上的插入函数向队尾添加新元素。
弹出操作可用于删除队首的元素（列表的最后一个元素）,这也意味着入队为 O(n)，出队为 O(1)


def hotPotato(namelist,num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))





class ClassName(object):
 	"""docstring for ClassName"""
 	def __init__(self, arg):
 		super(ClassName, self).__init__()
 		self.arg = arg
 		 Printer: