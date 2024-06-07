class QuizBrain:
    def __init__(self, question_l):
        self.question_number = 0
        self.question_list = question_l
        self.score = 0

    def next_question(self):
        curr_num = self.question_number
        question = self.question_list[curr_num]
        curr_num += 1
        user_in = input(f"Q.{curr_num}: {question.text} (True/False)?: ").lower()
        while user_in != 'true' and user_in != 'false':
            user_in = input(f"Q.{curr_num}: {question.text} (True/False)?: ").lower()
        self.check_answer(user_in, question.answer)


    def check_answer(self,user_in, answer):
        curr_num = self.question_number + 1
        if answer.lower() == user_in:
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
            print(f"Correct Answer: {answer}")
        print(f"Your score is: {self.score}/{curr_num}")
        print("\n")



    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

