import os
import sys


# Ensure package imports work when running this script directly
SCRIPT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from Resume_generator.console_ui.MenuActions import MenuActions
def main():
    try:
        menu_actions = MenuActions()
        menu_actions.run()
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()
