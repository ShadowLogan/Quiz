from Question import Question
multiple_choice = [
    "Are leaves purple?\n(y)Yes\n(n)No\n\n",
    "Is the sky blue?\n(y)Yes\n(n)No\n\n",
    "Are carrots green?\n(y)Yes\n(n)No\n\n",
    "Is Poland in Europe?\n(y)Yes\n(n)No\n\n"
]

questions = [
    Question(multiple_choice[0], "n"),
    Question(multiple_choice[1], "y"),
    Question(multiple_choice[2], "n"),
    Question(multiple_choice[3], "y")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/4 questions correct!")

run_test(questions)