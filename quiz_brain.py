class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def num_questions(self):
        return len(self.question_list)

    def still_has_questions(self):
        return self.question_number < self.num_questions()

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
        else:
            self.current_question = None

    def is_correct(self, user_answer):
        correct_answer = self.current_question.answer
        # print(f"Q{self.question_number} Correct answer = {correct_answer} user answer = {user_answer}")
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
