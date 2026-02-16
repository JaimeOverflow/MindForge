from activities.multiplications import normal_multiplications

from helpers.exceptions import MenuInvalidInputError, MenuOutOfBoundsError
from helpers.screen import clean_screen
from helpers.options import OPTION_QUIT

OPTIONS = [
    {
        "text": "Basic Multiplications",
        "game": normal_multiplications.play_game,
    }
]


def run_menu(menu_options):
    clean_screen()
    while True:
        show_main_menu(menu_options)
        menu_choice = get_menu_choice(menu_options)

        if menu_choice == OPTION_QUIT:
            return

        show_game_menu(menu_options, menu_choice)
        clean_screen()


def get_menu_choice(menu_options):
    while True:
        try:
            try:
                menu_choice = int(input("Enter a number:\n"))
            except ValueError:
                raise MenuInvalidInputError("Input has to be a valid number.")

            if menu_choice < OPTION_QUIT or menu_choice > len(OPTIONS):
                raise MenuOutOfBoundsError("Menu choice out of bounds.")

            return menu_choice
        except (MenuInvalidInputError, MenuOutOfBoundsError) as error:
            clean_screen()
            print(f"Error. {error}\n")
            show_main_menu(menu_options)


def show_main_menu(menu_options):
    print("Choose one game:")
    print(f"{OPTION_QUIT}. Quit menu.")

    for index in range(len(menu_options)):
        menu_option = index + 1
        print(f"{menu_option}. {menu_options[index]['text']}.")


def show_game_menu(menu_options, menu_choice: int) -> None:
    index = menu_choice - 1
    menu_item = menu_options[index]

    has_menu = "menu" in menu_item
    has_game = "game" in menu_item
    if has_menu:
        run_menu(menu_item["menu"])
    elif has_game:
        menu_item["game"]()
