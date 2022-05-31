counter = 0

class N:
	def __init__(self):
		global counter
		self.i = 1
		counter += 1
	
		
	def hi(self):
		print('Hi!')

	def rep(self):
		print(f'Усього {counter}')


n = N()
n2 = N()
k = N()
l = N()
l2 = N()

n.rep()

