# A computer quiz game

print("Welcome to my kehinde's quiz")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
    
print("Okay! Let's play 😊 ")
score = 0

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Ooops...incorrect!")
    
answer = input("What does API stands for? ").lower()
if answer == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Ooops...incorrect!")
    
answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Ooops...incorrect!")
    
answer = input("What does GUI stands for? ").lower()
if answer == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Ooops...incorrect!")
    
answer = input("What does QA stands for? ").lower()
if answer == "quality assurance":
    print("Correct!")
    score += 1
else:
    print("Ooops...incorrect!")
    
print(f"You got {score} questions correct!")
if score >=3:
    print(f"Awesome! \nGreat job!! \nYour final score is {(score/5) * 100}%!!! 🥳")
else:
    print(f"Oopsie! \nBetter luck next time!! \nYour final score is {(score/5) * 100}%!!! 🌝")