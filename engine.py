import render
import config
import calc
from time import perf_counter

render.setup_game()

user = 'eva'
setup = config.load_config(user)

total_questions = setup['totalQuestions']
question_no = 1
correct_answers = 0

test_start_time = perf_counter()

while question_no <= total_questions:
    question = calc.get_digits(setup)
    start_time = perf_counter()
    guess = render.question_input(question)
    answer_time = perf_counter() - start_time

    if guess.isnumeric() and int(guess) == calc.get_result(question.x, question.y, setup['challenge']):
        correct_answers += 1
        render.correct(answer_time)
    else:
        render.wrong(answer_time)
    question_no += 1
test_answer_time = perf_counter() - test_start_time
render.results(correct_answers, total_questions, test_answer_time)
