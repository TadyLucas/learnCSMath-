import random
import tkinter as tk

def dec_to_bin(n):
    return bin(n)[2:]

def dec_to_hex(n):
    return hex(n)[2:]

def bin_to_dec(b):
    return str(int(b, 2))

def hex_to_dec(h):
    return str(int(h, 16))

class NumberConversionQuiz:
    def __init__(self, master):
        self.master = master
        master.title("Number Conversion Quiz")
        master.geometry("400x400")
        master.resizable(False, False)

        self.score = 0
        self.total_questions = 0
        self.max_value = 255  # Adjust difficulty here

        self.conversions = [
            ("Decimal → Binary", dec_to_bin, "decimal", "binary"),
            ("Decimal → Hexadecimal", dec_to_hex, "decimal", "hex"),
            ("Binary → Decimal", bin_to_dec, "binary", "decimal"),
            ("Hexadecimal → Decimal", hex_to_dec, "hex", "decimal"),
        ]

        self.frame = tk.Frame(master, padx=20, pady=20)
        self.frame.pack(expand=True, fill='both')

        self.score_label = tk.Label(self.frame, text="Score: 0 / 0", font=("Helvetica", 12))
        self.score_label.pack(anchor='ne')

        self.question_label = tk.Label(self.frame, text="", font=("Helvetica", 16, "bold"), wraplength=360, justify="center")
        self.question_label.pack(pady=(20,10))

        self.input_entry = tk.Entry(self.frame, font=("Helvetica", 16), justify='center')
        self.input_entry.pack(pady=10)
        self.input_entry.bind('<Return>', lambda event: self.check_answer())

        self.submit_button = tk.Button(self.frame, text="Submit", font=("Helvetica", 14), command=self.check_answer, bg="#4CAF50", fg="white", activebackground="#45a049")
        self.submit_button.pack(pady=(5, 10), ipadx=10, ipady=5)

        self.feedback_label = tk.Label(self.frame, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=5)

        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=10, fill='x')

        self.skip_button = tk.Button(button_frame, text="Skip Question", font=("Helvetica", 12), command=self.skip_question, bg="#FF9800", fg="white", activebackground="#e68a00")
        self.skip_button.pack(side="left", expand=True, fill='x', padx=(0, 5), ipadx=10, ipady=5)

        self.quit_button = tk.Button(button_frame, text="Quit", font=("Helvetica", 12), command=master.quit, bg="#f44336", fg="white", activebackground="#da190b")
        self.quit_button.pack(side="left", expand=True, fill='x', padx=(5, 0), ipadx=10, ipady=5)

        self.new_question()

    def new_question(self):
        self.feedback_label.config(text="")
        self.input_entry.config(state='normal')
        self.input_entry.delete(0, tk.END)
        self.submit_button.config(state='normal')
        self.input_entry.focus_set()

        self.conv_name, self.func, self.from_type, self.to_type = random.choice(self.conversions)

        if self.from_type == "decimal":
            self.value = random.randint(1, self.max_value)
            self.display_value = str(self.value)
        elif self.from_type == "binary":
            self.value = random.randint(1, self.max_value)
            self.display_value = bin(self.value)[2:]
        else:  # hex
            self.value = random.randint(1, self.max_value)
            self.display_value = hex(self.value)[2:]

        self.question_label.config(
            text=f"{self.conv_name}\n\nInput: {self.display_value}"
        )

    def check_answer(self):
        user_answer = self.input_entry.get().lower().strip()
        if not user_answer:
            self.feedback_label.config(text="⚠️ Please enter an answer.", fg="orange")
            return

        # Pass correct input type to function
        if self.from_type == "decimal":
            correct_answer = self.func(self.value)
        else:
            correct_answer = self.func(self.display_value)

        self.total_questions += 1

        if user_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
            self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")

            self.input_entry.config(state='disabled')
            self.submit_button.config(state='disabled')

            self.master.after(1000, self.new_question)

        else:
            self.feedback_label.config(text=f"❌ Wrong! Try again.", fg="red")
            self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")

    def skip_question(self):
        self.feedback_label.config(text="⏭️ Question skipped!", fg="blue")
        self.total_questions += 1  # Count skipped questions in total attempts
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")
        self.input_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.new_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberConversionQuiz(root)
    root.mainloop()
