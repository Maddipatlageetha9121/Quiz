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
    {"text": "10. Which module in Python is used for regular expressions?", "answer": "C"},
    {"text": "11. Which keyword is used to define a function in Python?", "answer": "C"},
    {"text": "12. Which of the following is used to define a block of code in Python?", "answer": "D"},
    {"text": "13. What is the output of 2 ** 3 in Python?", "answer": "A"},
    {"text": "14. Which built-in function returns the length of an object?", "answer": "B"},
    {"text": "15. Which of these is a Python tuple?", "answer": "A"},
    {"text": "16. Which operator is used for floor division in Python?", "answer": "C"},
    {"text": "17. What is the output of bool(0)?", "answer": "B"},
    {"text": "18. Which of these is NOT a Python data type?", "answer": "D"},
    {"text": "19. Which statement is used to exit a loop in Python?", "answer": "C"},
    {"text": "20. Which of the following is the correct file extension for Python files?", "answer": "A"},
    {"text": "21. Which function is used to display output in Python?", "answer": "B"},
    {"text": "22. What is the output of len('Python')?", "answer": "C"},
    {"text": "23. Which of these is used to handle exceptions in Python?", "answer": "A"},
    {"text": "24. Which of the following is a Python Boolean literal?", "answer": "B"}
]
options=[
    ["A. Inheritance","B. Abstraction","c. Polymorphism","D. Objects"],
    ["A. Single","B. Double","C. Multiple","D. Both A and c"],     
    ["A. Multiple Inheritance","B. Multilevel Inheritance","C. Hierarchical Inheritance","D. None of these"],
    ["A. Two level","B Three level","C. Any level","D. None of these"],
    ["A. Method Recursive Object","B. Method Resolution Order","C. Main Resolution Order","D. Method Resolution Object"],
    ["A. 35", "B. 30", "C. 40", "D. 45"],
    ["A. <class 'tuple'>", "B. <class 'set'>", "C. <class 'list'>", "D. <class 'dict'>"],
    ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
    ["A. str", "B. int", "C. float", "D. bool"],
    ["A. os", "B. sys", "C. re", "D. regex"],
    ["A. fun", "B. define", "C. def", "D. function"],
    ["A. Brackets {}", "B. Parentheses ()", "C. Semicolon ;", "D. Indentation"],
    ["A. 8", "B. 6", "C. 9", "D. 5"],
    ["A. size()", "B. len()", "C. length()", "D. count()"],
    ["A. (1, 2, 3)", "B. [1, 2, 3]", "C. {1, 2, 3}", "D. {{1:2}}"],
    ["A. /", "B. %", "C. //", "D. **"],
    ["A. True", "B. False", "C. 0", "D. Error"],
    ["A. List", "B. Set", "C. Tuple", "D. ArrayList"],
    ["A. stop", "B. exit", "C. break", "D. quit"],
    ["A. .py", "B. .pyt", "C. .pt", "D. .python"],
    ["A. printt()", "B. print()", "C. echo()", "D. display()"],
    ["A. 5", "B. 8", "C. 6", "D. 7"],
    ["A. try-except", "B. do-catch", "C. throw-catch", "D. handle-error"],
    ["A. true", "B. True", "C. TRUE", "D. yes"]
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