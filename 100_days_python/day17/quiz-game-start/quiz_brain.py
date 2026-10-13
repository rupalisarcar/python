class QuizBrain:
    def __init__(self, q_list):
        self.q_number =0
        self.question_list = q_list
        self.score = 0

    def still_has_qustion(self):
        if self.q_number>=len(self.question_list):
            return False
        else:
            return True
         

    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number+=1
        user_answer = input(f"Q{self.q_number}: {current_question.text} (True/False)?:  ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, cqu):
        if user_answer == cqu:
            print("You got right!")
            self.score+=1
        else: 
            print("You got wrong")
        print(f"The correct answer was: {cqu}")
        print(f"You current score is: {self.score}/{self.q_number}")
        print("\n")
        print("\n")
        print("\n")