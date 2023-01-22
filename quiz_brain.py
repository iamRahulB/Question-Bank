class Brain:
	def __init__(self,question,answer,i,pscore):
		self.question=question
		self.answer=answer
		self.i=i
		self.score=pscore
	
	def check_answer(self):
		self.i+=1
		user_answer=input(f"Q.{self.i} {self.question} (True\False) :\n").capitalize()
		score_user=self.scorew()
		
		self.answer,score_user=self.check_ans(user_answer,score_user)
		return self.answer,score_user;
			
	def scorew(self):
		self.score+=1
		return self.score
	def check_ans(self,user_answer,score_user):
		if user_answer==self.answer:
			print("correct")
		elif user_answer!=self.answer:
			self.answer=False
			score_user-=1
		return self.answer,score_user;	
