import tkinter as tk
from tkinter import messagebox

class QuizMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Maker")
        self.root.geometry("400x500")

        self.questions = []
        self.current_question_index = 0

        # Frames
        self.main_frame = tk.Frame(root)
        self.quiz_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Main Menu
        self.title_label = tk.Label(self.main_frame, text="Quiz Maker", font=("Arial", 20))
        self.title_label.pack(pady=20)

        self.create_button = tk.Button(self.main_frame, text="Create Quiz", command=self.create_quiz)
        self.create_button.pack(pady=10)

        self.view_button = tk.Button(self.main_frame, text="View Quiz", command=self.view_quiz)
        self.view_button.pack(pady=10)

        self.take_button = tk.Button(self.main_frame, text="Take Quiz", command=self.take_quiz)
        self.take_button.pack(pady=10)

        # Create Quiz Widgets
        self.question_entry = tk.Entry(self.main_frame, width=40)
        self.option_entries = [tk.Entry(self.main_frame, width=40) for _ in range(4)]
        self.correct_answer_var = tk.IntVar()

        self.add_question_button = tk.Button(self.main_frame, text="Add Question", command=self.add_question)
        self.save_quiz_button = tk.Button(self.main_frame, text="Save Quiz", command=self.save_quiz)

        # Take Quiz Widgets
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16))
        self.option_vars = [tk.StringVar() for _ in range(4)]
        self.radio_buttons = [tk.Radiobutton(self.quiz_frame, text="", variable=self.option_vars[i], value=i) for i in range(4)]
        self.next_button = tk.Button(self.quiz_frame, text="Next Question", command=self.next_question)
        self.score = 0

    def create_quiz(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Enter Question").pack(pady=5)
        self.question_entry.pack(pady=5)

        for i in range(4):
            tk.Label(self.main_frame, text=f"Option {i+1}").pack(pady=2)
            self.option_entries[i].pack(pady=2)

        tk.Label(self.main_frame, text="Correct Answer (1-4)").pack(pady=5)
        tk.Entry(self.main_frame, textvariable=self.correct_answer_var).pack(pady=5)

        self.add_question_button.pack(pady=10)
        self.save_quiz_button.pack(pady=5)

    def add_question(self):
        question = self.question_entry.get()
        options = [entry.get() for entry in self.option_entries]
        correct_answer = self.correct_answer_var.get() - 1

        if question and all(options) and 0 <= correct_answer < 4:
            self.questions.append({
                "question": question,
                "options": options,
                "answer": correct_answer
            })
            messagebox.showinfo("Quiz Maker", "Question added successfully!")
            self.clear_inputs()
        else:
            messagebox.showwarning("Quiz Maker", "Please fill out all fields correctly.")

    def save_quiz(self):
        if self.questions:
            messagebox.showinfo("Quiz Maker", "Quiz saved successfully!")
            self.clear_frame(self.main_frame)
            self.__init__(self.root)
        else:
            messagebox.showwarning("Quiz Maker", "No questions to save.")

    def view_quiz(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Quiz Questions", font=("Arial", 16)).pack(pady=10)

        for i, question in enumerate(self.questions):
            question_text = f"Q{i+1}. {question['question']} \nOptions: {', '.join(question['options'])} \nAnswer: Option {question['answer'] + 1}"
            tk.Label(self.main_frame, text=question_text, justify="left", wraplength=300).pack(pady=5)

    def take_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.clear_frame(self.main_frame)
        self.quiz_frame.pack(fill="both", expand=True)
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])
            self.question_label.pack(pady=10)

            for i, option in enumerate(question_data['options']):
                self.radio_buttons[i].config(text=option)
                self.radio_buttons[i].pack(pady=5)

            self.next_button.pack(pady=20)
        else:
            self.show_score()

    def next_question(self):
        selected_answer = -1
        for i, radio in enumerate(self.radio_buttons):
            if radio.cget("text") == self.option_vars[i].get():
                selected_answer = i

        correct_answer = self.questions[self.current_question_index]['answer']
        if selected_answer == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Maker", f"Your score: {self.score} / {len(self.questions)}")
        self.clear_frame(self.quiz_frame)
        self.__init__(self.root)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def clear_inputs(self):
        self.question_entry.delete(0, tk.END)
        for entry in self.option_entries:
            entry.delete(0, tk.END)
        self.correct_answer_var.set(0)

# Run the application
root = tk.Tk()
app = QuizMaker(root)
root.mainloop()
def create_quiz(self):
    # Clear any existing widgets in the main frame to start fresh
    self.clear_frame(self.main_frame)
    
    # Add the widgets for creating a quiz question
    tk.Label(self.main_frame, text="Enter Question").pack(pady=5)
    self.question_entry = tk.Entry(self.main_frame, width=40)
    self.question_entry.pack(pady=5)
    
    self.option_entries = [tk.Entry(self.main_frame, width=40) for _ in range(4)]
    for i, entry in enumerate(self.option_entries):
        tk.Label(self.main_frame, text=f"Option {i+1}").pack(pady=2)
        entry.pack(pady=2)

    tk.Label(self.main_frame, text="Correct Answer (1-4)").pack(pady=5)
    self.correct_answer_var = tk.IntVar()  # Reset this variable each time
    tk.Entry(self.main_frame, textvariable=self.correct_answer_var).pack(pady=5)

    self.add_question_button = tk.Button(self.main_frame, text="Add Question", command=self.add_question)
    self.add_question_button.pack(pady=10)
    self.save_quiz_button = tk.Button(self.main_frame, text="Save Quiz", command=self.save_quiz)
    self.save_quiz_button.pack(pady=5)

def clear_inputs(self):
    # Ensure each entry field is cleared without causing reference issues
    if hasattr(self, 'question_entry'):
        self.question_entry.delete(0, tk.END)
    if hasattr(self, 'option_entries'):
        for entry in self.option_entries:
            entry.delete(0, tk.END)
    self.correct_answer_var.set(0)
