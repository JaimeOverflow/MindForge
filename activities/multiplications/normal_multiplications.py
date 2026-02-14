import time
import random

from helpers.screen import clean_screen


def play_game():
    clean_screen()
    should_try_again = True
    while should_try_again:
        start_time = time.time()
        number_correct_answers = run_game()
        show_results(number_correct_answers, start_time)
        should_try_again = get_should_try_again()
        clean_screen()


def run_game():
    correct_answers = 0
    tries = 0
    MAX_TRIES = 10
    while tries < MAX_TRIES:
        first_number = random.randint(2, 9)
        second_number = random.randint(2, 9)

        expected_result = first_number * second_number

        print(f"Question {tries + 1}/{MAX_TRIES}")
        text = f"{first_number} x {second_number} = "
        try:
            result = int(input(f"{text} \n"))
        except Exception:
            result = None

        if result is not None and result == expected_result:
            correct_answers += 1
            clean_screen()
        else:
            print("Mistake")
            print(f"{text}{expected_result}")
            print(f"Your result: {result}\n")

        tries += 1

    return correct_answers


def show_results(correct_answers, start_time):
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Time in seconds: {result_time}")
    print(f"Points: {correct_answers}\n")


def get_should_try_again() -> bool:
    try_again = input("Try again? (y/n)\n")
    return try_again == "y"
