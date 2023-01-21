from data import question_data
from quiz_brain import Brain
length=len(question_data)


score=0
correct=True

print("Coded By iamRahul")
for i in range(len(question_data)):
	while correct:
		question=question_data[i]["text"]
		answer=question_data[i]["answer"]
		brain=Brain(question,answer,i,score)
		correct,nscore=brain.check_answer()
		score=nscore
		print(f"score is {nscore}")
		break
		
