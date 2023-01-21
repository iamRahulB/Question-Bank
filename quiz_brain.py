class Brain:
	def __init__(self,question,answer,i):
		self.question=question
		self.answer=answer
		self.i=i
	
	def check_answer(self):
		self.i+=1
		user_answer=input(f"Q.{self.i} {self.question} (True\False) :\n")
		if user_answer==self.answer:
			return self.answer
		else:
			print("sorry u are not Rahul to answer everything .. hahahaha")
			return False
			
			