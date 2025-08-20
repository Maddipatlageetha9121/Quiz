import tkinter as tk

# Questions and options
question_bank = [
    {"text": "1. The ability of one class to acquire methods and attributes from another class is called _______", "answer": "A"},
    {"text": "2. Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "3. What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "4. What is the depth of multilevel inheritance in Python?", "answer": "C"},
    {"text": "5. What does MRO stand for?", "answer": "B"},
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

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
    ["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order", "D. Method Resolution Object"],
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

# Globals
current_question = 0
score = 0

# Tkinter window
root = tk.Tk()
root.title("Python Quiz Game")
root.geometry("600x400")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, justify="left")
question_label.pack(pady=20)

# Option buttons
var = tk.StringVar()
radio_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=var, value="", font=("Arial", 14))
    btn.pack(anchor="w")
    radio_buttons.append(btn)

# Feedback label
feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
feedback_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Load a question
def load_question():
    global current_question
    question_label.config(text=question_bank[current_question]["text"])
    var.set(None)
    feedback_label.config(text="")  # Clear feedback
    for i in range(4):
        radio_buttons[i].config(text=options[current_question][i], value=options[current_question][i][0])

# Next question logic
def next_question():
    global current_question, score
    selected = var.get()
    if not selected:
        feedback_label.config(text="Please select an answer.", fg="red")
        return
    correct = question_bank[current_question]["answer"]
    if selected == correct:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect. Correct Answer: {correct}", fg="red")
    score_label.config(text=f"Score: {score}")
    
    # Move to next question after short delay
    current_question += 1
    if current_question < len(question_bank):
        root.after(1000, load_question)
    else:
        feedback_label.config(text=f"Quiz Completed! Final Score: {score}/{len(question_bank)}", fg="blue")
        next_button.config(state="disabled")

# Next button
next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12), bg="#4CAF50", fg="white")
next_button.pack(pady=20)

# Start
load_question()
root.mainloop()
