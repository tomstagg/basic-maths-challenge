import os
from type import Question


tick_icon = u"\U00002705"
cross_icon = u"\U0000274c"


def setup_game():
    os.system('clear')

    print("Maths Challenge \U0001F600")
    print('-' * 18)


# def render_question(x,y,setup):

def question_input(question: Question):
    question = f'{question.x} {question.operator} {question.y}'
    return input(f'{question:<8}= ')


def correct(answer_time):
    result = f"{tick_icon} {answer_time:.2f} seconds"
    display_result(result)


def wrong(answer_time):
    result = f"{cross_icon} {answer_time:.2f} seconds"
    display_result(result)


def display_result(result):
    print(f'\033[13C\033[1A {result}')


def results(correct_answers, total_questions, test_answer_time):
    print(
        f'You got {correct_answers}/{total_questions} correct in {test_answer_time:.2f} seconds')
    print(f'{test_answer_time/total_questions:.2f} average second per question')
