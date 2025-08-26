# Quizz game where you ask user to questions and give results at the end, with some basics codings

print("Welcome to my game")

result = 0
selection = input("Do you wanna play: yes / no :").lower()

if selection != "yes":
    print("Goodbye")
    quit()

if selection == 'yes':
    answer = input("What does CPU stand for: ")
    if answer.lower() == "central processing unit":
        print("Correct")
        result += 1
    else:
        print("Incorrect")

    answer = input("What does RAM stand for: ")
    if answer.lower() == "random access memory":
        print("Correct")
        result += 1

    else:
        print("Incorrect")

    answer = input("What does GPU stand for: ")
    if answer.lower() == "graphics processing unit":
        print("Correct")
        result += 1

    else:
        print("Incorrect")

    answer = input("What does SPU stand for: ")
    if answer.lower() == "supply unit":
        print("Correct")
        result += 1

    else:
        print("Incorrect")


print("End of the game\n\n")
print(f"you have got {result} out of 4\n\n")
print("**********************")
print("**Thanks for Playing**")
print("**********************")






