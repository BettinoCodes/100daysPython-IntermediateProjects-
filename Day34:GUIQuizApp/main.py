from tkinter import *
import requests
from question import Question
import random
# from quizbrain import QuizBrain

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
print(response)

data_questions = response.json()["results"]
print(data_questions)

current_question = Question(text=None, answer=None)

question_bank = []
for question in data_questions:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_quest = Question(text=question_text, answer=question_ans)
    question_bank.append(new_quest)

for questions in question_bank:
    print(questions.text, questions.answer)

def choose_question():
    global current_question
    current_question = random.choice(question_bank)
    canvas.itemconfig(quote_text, text=current_question.text)
    question_bank.remove(current_question)
    if len(question_bank) == 0:
        canvas.itemconfig(quote_text, text="That was all folks see you on the next one")


def correct_back_ground():
    canvas.configure(bg='green')
    canvas.after(1000, func=white_back_ground)


def incorrect_back_ground():
    canvas.configure(bg='red')
    canvas.after(1000, func=white_back_ground)


def white_back_ground():
    canvas.configure(bg='white')

def chose_true_ans():
    ans = "True"
    if ans == current_question.answer:
        correct_back_ground()
    else:
        incorrect_back_ground()
    choose_question()

def chose_false_ans():
    ans = "False"
    if ans == current_question.answer:
        correct_back_ground()
    else:
        incorrect_back_ground()
    choose_question()


window = Tk()
window.title("Quiz GUI by BGcodes")
window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=500)
background_img = PhotoImage(file="backgroundbart.png")
canvas.create_image(250, 250, image=background_img)
quote_text = canvas.create_text(250, 250, text="Questions GO HERE", width=400, font=("Arial", 30, "bold"), fill="grey")
canvas.grid(row=0, column=0, columnspan=3)

true_button = Button(text="TRUE", highlightthickness=0, width=15, font=("Arial", 20, "bold"), bg="green", command=chose_true_ans)
true_button.grid(row=1, column=0)

false_button = Button(text="FALSE", highlightthickness=0, width=15, font=("Arial", 20, "bold"), bg="red", command=chose_false_ans)
false_button.grid(row=1, column=2)

choose_question()

if len(question_bank) == 0:
    canvas.itemconfig(quote_text, text="That was all folks see you on the next one")

window.mainloop()
