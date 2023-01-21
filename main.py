from data import question_data
from quiz_brain import Brain
length=len(question_data)



correct=True

print("Coded By iamRahul")
for i in range(len(question_data)):
	while correct:
		question=question_data[i]["text"]
		answer=question_data[i]["answer"]
		brain=Brain(question,answer,i)
		correct=brain.check_answer()
		break
		
