import random
import os
from time import perf_counter
import config
# from playsound import playsound
os.system('clear')

print(u"Maths Challenge \U0001F600")
print('-' * 18)

user = 'eva'

setup = config.load_config(user)

digit_two_options = [2, 5, 10]

total_questions = setup['totalQuestions']
question_no = 1
correct_answers = 0

tick_icon = u"\U00002705"
cross_icon = u"\U0000274c"

test_start_time = perf_counter()

while question_no <= total_questions:

    digit_one = random.randint(0, 12)
    digit_two = random.choice(digit_two_options)

    question = f'{digit_one} x {digit_two}'
    start_time = perf_counter()
    guess = input(f'{question:<8}= ')
    answer_time = perf_counter() - start_time

    if (int(guess) == (digit_one * digit_two)):
        result = f"{tick_icon} {answer_time:.2f} seconds"  # correct
        correct_answers += 1
    else:
        result = f"{cross_icon} {answer_time:.2f} seconds"  # wrong

    print(f'\033[13C\033[1A {result}')
    question_no += 1

test_answer_time = perf_counter() - test_start_time
print(
    f'You got {correct_answers}/{total_questions} correct in {test_answer_time:.2f} seconds')
print(f'{test_answer_time/total_questions:.2f} average second per question')
