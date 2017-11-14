#!/usr/bin/env python

import ast
import pickle



class AskQuestion:
	savingQuestionEventHanlder = None
	
	@staticmethod #Se this method as static
	def loadQuestionsLstFromFile(fileFullName,loadingQuestionEventHanler=None):
		"""This load all questions from the specified file"""
		questionsLst = []
		fs = open(fileFullName,"rt")
		while True:
			line = fs.readline()
			if len(line) > 0:
				#Unserialize the string into a dictionary object
				questionValues = ast.literal_eval(line)
				#Create a new AskQuestion object
				iQuestion = AskQuestion(questionValues["Question"],questionValues["OptionLst"],questionValues["RigthAswer"])			
				iQuestion.IsRight = questionValues["IsRight"]
				iQuestion.UserAnswer = questionValues["UserAnswer"]
				if not loadingQuestionEventHanler == None:
					#Calling loadingQuestionEventHanler
					loadingQuestionEventHanler(iQuestion,questionValues)
				#Add question object to the list
				questionsLst.append(iQuestion)			
			else:
				break
		fs.close()
		#Return list		
		return questionsLst	
		
	def __init__(self,Question,OptionLst,RightAnswer):
		self.Question = Question
		self.OptionLst = OptionLst
		self.RigthAswer = RightAnswer
		self.IsRight = False
		self.UserAnswer = ""
	
	#Overrides the method and return a dictrionary as string	
	def __str__(self):
		#Create dictionary
		questionValues= {}
		#Fill add to the dictionary each property of AskQuestion
		questionValues["Question"] = self.Question
		questionValues["OptionLst"] = self.OptionLst
		questionValues["RigthAswer"] = self.RigthAswer
		questionValues["UserAnswer"] = self.UserAnswer
		questionValues["IsRight"] = self.IsRight
		if not self.savingQuestionEventHanlder == None:
				#Raising event handler
				self.savingQuestionEventHanlder(self,questionValues)	
		return str(questionValues)
	
	#This method ask to the user to answer the question	
	def ask(self):
		
		#Show the question
		print(self.Question)
		
		#Loop int each option from the list
		for strOption in self.OptionLst:
			#Print the option
			print(strOption)
		
		#Wait for user answer	
		self.UserAnswer = raw_input("Choose your answer>")
		#Check if the answered question is right	
		if self.UserAnswer==self.RigthAswer:
			self.IsRight=True
			
	#Display the evaluation of the question		
	def showRightAnswer(self):
		if self.IsRight:
			print("""
			Question:
				%s
			Options
				%s
			Answered:%s
			The answer is Ok		
			"""%(self.Question," ".join(self.OptionLst),self.UserAnswer))		
		else:
			print("""
			Question:
				%s
			Options:
				%s
			Answered: %s
			Right answer is %s		
			"""%(self.Question," ".join(self.OptionLst),self.UserAnswer,self.RigthAswer))

	#Save current question content into a file		
	def save(self,fileFullName):
		fs = open(fileFullName,"at")
		#Write the content returned by the method __str__ calling self
		fs.write(("%s\n"%self))
		fs.flush()
		fs.close()


if __name__=="__main__":
	import os
	counter = 0
	def savingQuestionEvent(sender,questionValues):
		sender.id = (counter+1)
		questionValues["id"] = sender.id
	def loadingQuestionEvent(question,questionValues):
		question.id = questionValues["id"]
			
	print("""
		**************
		* DEBUG MODE *
		**************
	""")
	
	print("File path:{0}".format(os.path.dirname(os.path.realpath("__file__"))))
	question = AskQuestion("Is 6 > -6 ?",["a) Yes","b) No"],"b")
	question.savingQuestionEventHanlder = savingQuestionEvent
	question.ask()
	question.save("question")
	
	questionsLst = AskQuestion.loadQuestionsLstFromFile("question",loadingQuestionEvent)
	
	print("The question id is %s"%questionsLst[0].id)
	
	
	
	
	