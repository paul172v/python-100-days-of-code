class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, actual_answer):
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.actual_answer = actual_answer
        self.is_correct = False

    def ask_question(self):
        given_answer = input(
            f"{self.question}\n1. {self.answer_1}?\n2. {self.answer_2}?\n3. {self.answer_3}?\n"
        )

        if given_answer == self.actual_answer:
            self.is_correct = True
            print("Correct")

        else:
            print("false")


def ask_all_questions():
    score = 0
    for el in questions_arr:
        el.ask_question()
        if el.is_correct == True:
            score += 1
    print(f"Final score is.... {score}")


q1 = Question("What is the capitol of England?", "London", "Paris", "Rome", "1")
q2 = Question("Which color is in the American flag?", "Green", "Red", "Purple", "2")
q3 = Question("Which is a programming language?", "Windows", "Apple", "Python", "3")

questions_arr = [q1, q2, q3]


ask_all_questions()
