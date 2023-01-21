class Brain:
	def __init__(self,question,answer,i,pscore):
		self.question=question
		self.answer=answer
		self.i=i
		self.score=pscore
	
	def check_answer(self):
		self.i+=1
		user_answer=input(f"Q.{self.i} {self.question} (True\False) :\n")
		score_user=self.scorew()
		if user_answer==self.answer:
			
			return self.answer,score_user;
			
		else:
			print("sorry u are not Rahul to answer everything .. hahahaha")
			return False
			
	def scorew(self):
		self.score+=1
		return self.score
		
