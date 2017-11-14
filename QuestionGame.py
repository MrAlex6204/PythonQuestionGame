#!
#-*-encoding:utf-8-*-

from Question import AskQuestion

answered = 0
#Create a list of AskQuestion objects
testQuestions = [
	#Create a AskQuestion objects. Add the question and then a list of choice options fallowed by the right answer
	AskQuestion("4+x+1 = 10 which value is x ?",
		["a) 3","b) 5","c) 0"],
		"b"
	),
	AskQuestion("Is 6 > -6 ?",
		["1) Yes","2) No"],
		"1"
	),
	AskQuestion("Wich programing language inherits from C",
		["a) C++","b) Java","c) C#","d) none"],
		"d"
	),
	AskQuestion("""
	Resolve x and y value
	(y*y)*2 = 200""",
		["a) 1","b) 10","c) 0","d) none"],
		"d"
	)
]

#Loop each item from the list
for iQuestion in testQuestions:
	#Call ask method from the AskQuestion class
	iQuestion.ask()	
	iQuestion.save("TestResults")

#Loop Calculate how many questions are Ok from the Qestion List
#Loop through to all question list and filter only the those that are Ok.
answered = len([ok for ok in testQuestions if ok.IsRight])
	
print("You answered %i of %i"%(answered,len(testQuestions)))

print("""
    ** QUESTIONS EVALUATION **
""")

#Load the answered questions from the file 
answeredQuestions = AskQuestion.loadQuestionsLstFromFile("TestResults")

#Display each question and the corresponding answer
for iQuestion in answeredQuestions:
	iQuestion.showRightAnswer()
