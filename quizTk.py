import tkinter as tk

# Questions and options
question_bank = [
    {"text": "1. The ability of one class to acquire methods and attributes from another class is called _______", "answer": "A"},
    {"text": "2. Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "3. What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "4. What is the depth of multilevel inheritance in Python?", "answer": "C"},
    {"text": "5. What does MRO stand for?", "answer": "B"}
]

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
    ["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order", "D. Method Resolution Object"]
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
