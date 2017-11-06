class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items ==[]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



s=Stack()
s.push(1)


##简单括号匹配
def parChecker(symbolString):
	s = Stack()
	balanced=True
	index=0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

## 多种形式的括号的匹配
def parChecker(symbolString):
	s = stack()
	balanced = True
	index = 0
	while index < len(symbolString):
		symbol = symbolString[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top,symbol):
					balanced = False
		index += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open,close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

##二进制的转换(10->2)
def divideBy2(decNumber):
	s = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		s.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not s.isEmpty():
		binString = binString + str(s.pop())

	return binString



##十进制和2-16进制之间的任意转换
def baseConverter(decNumber,base):
	digits="0123456789ABCDEF"
	s = Stack()
	while decNumber > 0:
		rem = decNumber % base
		s.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not s.isEmpty():
		newString = newString + digits[s.pop()]
	return newString


##中缀表达式转后缀表达式
def midTopost(expr):
	prec={}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	
	opstack = Stack() # 用于保存符号
	postfixList = [] # 保存最终的表达式

	tokenList = expr.split()
	for token in tokenList:
		if token in  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			topToken = opstack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
				postfixList.append(opstack.pop())
			opstack.push(token)


	while not opstack.isEmpty():
		postfixList.append(opstack.pop())

	return " ".join(postfixList)

## 后缀表达式求值
def postfixEval(expr):
	operandStack = Stack()
	tokenList = expr.split()

	for token in tokenList:
		if token in "0123456789":
			operandStack.push(token)
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(operand1,operand2,token)
			operandStack.push(result)
	return operandStack.pop

def doMath(op1,op2,op):
	if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2




##中缀表达式转前缀表达式
def midTopost(expr):
/*
和后缀表达式求值不一样在于：
1 从右向左读，第一个reverse
2 最后还要再reverse一下
3 栈中的元素的优先级必须大于表达式中的元素才能出栈，后缀是大于等于
4 加入栈中的是),因为是从右向左扫
*/
	prec={}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	
	opstack = Stack() # 用于保存符号
	postfixList = [] # 保存最终的表达式


	tokenList = expr.split()
	tokenList.reverse()
	for token in tokenList:
		if token in  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == ')':
			opstack.push(token)
		elif token == '(':
			topToken = opstack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()] > prec[token]):
				postfixList.append(opstack.pop())
			opstack.push(token)


	while not opstack.isEmpty():
		postfixList.append(opstack.pop())

	postfixList.reverse()
	return " ".join(postfixList)





## 前缀表达式求值
/*
和后缀表达式求值不一样在于两点：
1 从右向左读
2 先出栈的元素在操作符前
*/
def postfixEval(expr):
	operandStack = Stack()

	tokenList = expr.split()
	tokenList.reverse()
	for token in tokenList:
		if token in "0123456789":
			operandStack.push(token)
		else:
			operand1 = operandStack.pop()
			operand2 = operandStack.pop()
			result = doMath(operand1,operand2,token)
			operandStack.push(result)
	return operandStack.pop

def doMath(op1,op2,op):
	if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

