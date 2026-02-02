#FutureTime.py
#Name:Devyn Conaway
#Date:2/01/26
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  
  currentHour =  now.hour
  currentMinute = now.minute
  
  #print (currentHour, currentMinute) #this is just for checking, we should delete it later
    
  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreHours = int(input("How many hours in the future would you like to see?"))
  moreMins = int(input("How many minutes in the future would you like to see?"))

  futureMins = (currentMinute + moreMins) % 60 
  extraHour = (currentMinute + moreMins) // 60
  futureHours = (currentHour + moreHours + extraHour) % 24
  extraHours = (currentHour + moreHours + extraHour) // 24
  
  print(f'The future time will be {futureHours:02}:{futureMins:02}.')
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
