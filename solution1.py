class MyException(Exception):
	def __init__(self,v):
		self.v=v
	def __str__(self):
		return str(self.v)
def xyz(x,y):
	total=x+y
	if(total<150):
		raise MyException("Custom Exception Occured")
	else:
		print(total)
x=int(input())
y=int(input())

xyz(x,y)
