#!
#-*-encoding:utf-8-*-

from Question import AskQuestion, loadQuestionsFromFile

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
	#Get if the answer given by the user is right
	if iQuestion.isRight:
		#Sum a point if the answer given is right
		answered +=1
	#Save current question into a text file as append mode
	iQuestion.save("TestResults","at")
	
print("You answered %i of %i"%(answered,len(testQuestions)))

print("""
    ** QUESTIONS EVALUATION **
""")

#Load the answered questions from the file 
answeredQuestions = loadQuestionsFromFile("TestResults")

#Display each question and the corresponding answer
for iQuestion in answeredQuestions:
	iQuestion.showRightAnswer()
