def Solution(s1,s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i])-ord('a')
		c1[pos] += 1

	for i in range(len(s2)):
		pos = ord(s2[i])-ord('a')
		c2[pos] += 1
	

	j=0
	Is = True
	while j < 26 and Is:
		if c1[j] == c2[j]:
			j += 1
		else:
			Is = False

	return Is


def Solution(s1,s2):
	l1 = list(s1)
	l2 = list(s2)
	l1.sort()
	l2.sort()

	pos = 0
	match = True

	while pos < len(s1) and match:
		if l1[pos] == l2[pos]:
			pos++
		else:
			match = False
	return match


	