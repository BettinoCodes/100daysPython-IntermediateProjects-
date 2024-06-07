from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


# def add_to_bank():
#     n = int(input("How many questions do you want to add: "))
#     for i in range(n):
#         question = input(f"Enter question{i} here: ")
#         answer = input(f"Enter answer{i} here: ")
#         question_bank.append({"text": question, "answer": answer})
#     question_data.append(question_bank)


# print(f"This: {question_data["results"][0]["question"]}")
# print(f"This: {question_data["results"][0]["correct_answer"]}")

i = 0
for question in question_data["results"]:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_quest = Question(text=question_text, answer=question_ans)
    question_bank.append(new_quest)
    i += 1

print(question_bank)
qlist = QuizBrain(question_bank)

while qlist.still_has_questions():
    question = qlist.next_question()
    qlist.question_number += 1

print(f"Your Final Score is: {qlist.score}/{len(question_bank)}")
