from helpers.screen import clean_screen
from helpers.options import OPTION_QUIT

from activities.multiplications import normal_multiplications

OPTIONS = [
    {
        "text": "Basic Multiplications",
        "game": normal_multiplications.play_game,
    }
]


def show_game_menu():
    clean_screen()
    while True:
        print("Multiplication game.")
        show_menu()
        try:
            choice = int(input("Choose an option:\n"))

            if choice == OPTION_QUIT:
                return

            play_game(choice)

        except Exception:
            pass


def show_menu():
    print("Choose one option:")
    print(f"{OPTION_QUIT}. Quit menu.")

    for index in range(len(OPTIONS)):
        menu_option = index + 1
        print(f"{menu_option}. {OPTIONS[index]['text']}.")


def play_game(choice):
    index = choice - 1
    OPTIONS[index]["game"]()
