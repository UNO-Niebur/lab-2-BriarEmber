#Magic8Ball.py
#Name:Devyn Conaway
#Date:2/01/2026
#Assignment:Lab 2
#Purpose:Variable and Arithmetic

#We will need random for this program, import to use this package.
import random

def main(random):
  #Create a list of your responses.
  
  print("Magic 8 Ball")
  
  #Prompt the user for their question.
  answers = ("Yes", "No", "Try again later", "could be", "probably at one time or another", 
             "Try not doing that", "Have you considered another way?", "Not likely", 
             "The possibilities are endless", "Go for a walk", "Only you can answer that", 
             "You need chocolate", "Use GPS", " Don't do that", "More thought is required", 
             "That's not your color", "Be prepared", "Knowledge is valuable", 
             "Don't underestimate yourself", "Concentrate on the important things")
  
  input("Ask your question to determine your fate.")
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length
  r = int(r)
  
  response = answers[r]
  print(response)

if __name__ == '__main__':
  main(random)
