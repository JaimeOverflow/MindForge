from helpers.exceptions import MenuInvalidInputError, MenuOutOfBoundsError
from helpers.screen import clean_screen
from helpers.options import OPTION_QUIT

from activities.multiplications import menu as multiplications_menu

OPTIONS = [{"text": "Multiplications", "menu": multiplications_menu.show_game_menu}]


def main():
    clean_screen()
    while True:
        show_main_menu()
        menu_choice = get_menu_choice()

        if menu_choice == OPTION_QUIT:
            quit_game()

        show_game_menu(menu_choice)
        clean_screen()


def get_menu_choice():
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
            show_main_menu()


def quit_game():
    print("Thank you for playing")
    exit()


def show_main_menu():
    print("Choose one game:")
    print(f"{OPTION_QUIT}. Quit menu.")

    for index in range(len(OPTIONS)):
        menu_option = index + 1
        print(f"{menu_option}. {OPTIONS[index]['text']}.")


def show_game_menu(menu_choice: int) -> None:
    index = menu_choice - 1
    OPTIONS[index]["menu"]()


if __name__ == "__main__":
    main()
