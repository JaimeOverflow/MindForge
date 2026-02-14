from constants import main_menu

from helpers.menu import run_menu


def main():
    run_menu(main_menu.MENU_OPTIONS)
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
