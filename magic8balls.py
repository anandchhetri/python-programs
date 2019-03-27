# magic 8 ball python program

import sys
import time
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question or Press enter to quit : ")

    answers = random.randint(1,8)

    if question =="":
        sys.exit()

    elif answers == 1:
         print ("Thinking....")
         time.sleep(5)
         print ("It is certain")

    elif answers == 2:
         print ("Thinking....")
         time.sleep(5)
         print ("Outlook good")

    elif answers == 3:
         print ("Thinking....")
         time.sleep(5)
         print ("You may rely on it")

    elif answers == 4:
         print ("Thinking....")
         time.sleep(5)
         print ("Ask again later")

    elif answers == 5:
         print ("Thinking....")
         time.sleep(5)
         print ("Concentrate and ask again")

    elif answers == 6:
         print ("Thinking....")
         time.sleep(5)
         print ("Reply hazy, try again")

    elif answers == 7:
         print ("Thinking....")
         time.sleep(5)
         print ("My reply is a No")

    elif answers == 8:
         print ("Thinking....")
         time.sleep(5)
         print ("My sources say No")
