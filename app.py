print("***********************")
print("welcome to my quiz..!!")
question_bank=[
    {"text":"1.the ability of one class to aquire methods and attributes from another class is called_______","answer":"A"},
    {"text":"2.which of the following is a type of inheritance?","answer":"D"},
    {"text":"3.what type of inheritance has multiple subclasses to a single superclass?","answer":"C"},
    {"text":"4.what is the depth of multilevel inheritance in python?","answer":"C"},
    {"text":"5.what does MRO stands for?","answer":"B"},
    {"text": "6. Number of keywords in python are _________", "answer": "A"},
    {"text": "7. What is the output of print(type([]))?", "answer": "C"},
    {"text": "8. Which of the following is immutable in Python?", "answer": "B"},
    {"text": "9. What is the default return type of input() in Python?", "answer": "A"},
    {"text": "10. Which module in Python is used for regular expressions?", "answer": "C"}
]
options=[["A. Inheritance","B. Abstraction","c. Polymorphism","D. Objects"],
         ["A. Single","B. Double","C. Multiple","D. Both A and c"],     
         ["A. Multiple Inheritance","B. Multilevel Inheritance","C. Hierarchical Inheritance","D. None of these"],
         ["A. Two level","B Three level","C. Any level","D. None of these"],
         ["A. Method Recursive Object","B. Method Resolution Order","C. Main Resolution Order","D. Method Resolution Object"],
         ["A. 35", "B. 30", "C. 40", "D. 45"],
         ["A. <class 'tuple'>", "B. <class 'set'>", "C. <class 'list'>", "D. <class 'dict'>"],
         ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
         ["A. str", "B. int", "C. float", "D. bool"],
         ["A. os", "B. sys", "C. re", "D. regex"]
]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("*******************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess=input("enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        score+=1
        print("correct answer.")
    else:
        print("incorrect answer.")
        print(f"the correct answer is {question_bank[question_num][answer]}") # type: ignore
    print(f"your current score is {score}/{question_num+1}.")
print(f"your final score is {score}.")
print(f"your score is {score/len(question_bank)+100}%")