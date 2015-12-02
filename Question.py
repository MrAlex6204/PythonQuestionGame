import ast

#This load all questions from the specified file
def loadQuestionsFromFile(fileFullName):
	questionsLst = []
	fs = open(fileFullName,"rt")
	while True:
		line = fs.readline()
		if len(line) > 0:
			#Unserialize the string into a dictionary object
			iElement = ast.literal_eval(line)
			#Create a new AskQuestion object
			iQuestion = AskQuestion(iElement["strQuestion"],iElement["lstOptions"],iElement["oAnswer"])
			iQuestion.isRight = iElement["isRight"]
			iQuestion.oUsrAnswer = iElement["oUsrAnswer"]
			#Add question object to the list
			questionsLst.append(iQuestion)			
		else:
			break
	#Return list		
	return questionsLst	
	

class AskQuestion:
	
	def __init__(self,strQuestion,lstOptions,oRightAnswer):
		self.strQuestion = strQuestion
		self.lstOptions = lstOptions
		self.oAnswer = oRightAnswer
		self.isRight = False
		self.oUsrAnswer = ""
	
	#Overrides the method and return a dictrionary as string	
	def __str__(self):
		#Create dictionary
		serializeQuestion= {}
		#Fill add to the dictionary each property of AskQuestion
		serializeQuestion["strQuestion"] = self.strQuestion
		serializeQuestion["lstOptions"] = self.lstOptions
		serializeQuestion["oAnswer"] = self.oAnswer
		serializeQuestion["oUsrAnswer"] = self.oUsrAnswer
		serializeQuestion["isRight"] = self.isRight		
		return str(serializeQuestion)
	
	#This method ask to the user to answer the question	
	def ask(self):
		
		#Show the question
		print(self.strQuestion)
		
		#Loop int each option from the list
		for strOption in self.lstOptions:
			#Print the option
			print(strOption)
		
		#Wait for user answer	
		self.oUsrAnswer = raw_input("Choose your answer>")
		#Check if the answered question is right	
		if self.oUsrAnswer==self.oAnswer:
			self.isRight=True
			
	#Display the evaluation of the question		
	def showRightAnswer(self):
		if self.isRight:
			print("""
			Question:
				%s
			Options
				%s
			Answered:%s
			The answer is Ok		
			"""%(self.strQuestion," ".join(self.lstOptions),self.oUsrAnswer))		
		else:
			print("""
			Question:
				%s
			Options:
				%s
			Answered: %s
			Right answer is %s		
			"""%(self.strQuestion," ".join(self.lstOptions),self.oUsrAnswer,self.oAnswer))
			
	def save(self,fileFullName,mode):
		fs = open(fileFullName,mode)
		fs.write(("%s\n"%self))
		fs.flush()
		fs.close()
