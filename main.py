#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts years of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since Facebook data breach.")

#Introduces breach
print("Would you like to learn about the Facebook 2019 data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Facebook faced a data breach where personal information, including phone numbers, names, locations, and email addresses, of over 530 million users was posted on a hacking forum. The breach occurred due to exploitation of a vulnerability in a discontinued feature that enabled users to search for each other using phone numbers.")
  
  elif topic.lower() == "b":
    print("Facebook found and fixed a data breach issue in August 2019 but stated that they have no plans to individually notify the affected users due to uncertainties and the fact that the leaked information was publicly available and not something users could fix themselves. Therefore, they did not provide specific actions for the affected users to take.")
  
  elif topic.lower() == "c":
   break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")



#Introduces my take
print("I'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The Facebook 2019 data breach compromised personal information of millions of Facebook users, including phone numbers, names, locations, and email addresses. This breach violated the confidentiality of the users' personal data, as it was accessed and made publicly available without their consent.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because I believe that Facebook should have informed the affected users about the breach in order for them to be alert and take necessary precautions.")
  
  elif topic.lower() == "c":
   print("I would convince victims to take immediate action by emphasizing the potential risks of identity theft and credit card fraud that can arise from the unauthorized exposure of their personal information. My advice would be to take necessary actions such as changing passwords, monitoring financial accounts, and being cautious of potential identity theft attempts.")

  elif topic.lower() == "d":
   break
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")