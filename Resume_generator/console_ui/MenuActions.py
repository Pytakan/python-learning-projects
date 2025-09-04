from Resume_generator.console_ui.Menu import Menu
from Resume_generator.console_ui.MenuItems import MenuItem
from Resume_generator.format_convertor.Format import Format
from Resume_generator.user_info_module.Persone import Persone
from Resume_generator.console_ui.Actions import person_generator, path_generator, person_creator
from Resume_generator.console_ui.utils import clear_screen


class MenuActions:
    def __init__(self, menu: Menu=None, previous_menu:Menu=None):
        self.person = None  # Инициализируем person по умолчанию
        self.previous_menu = previous_menu
        self.menu = menu if menu else self.build_main_menu()
        
    def build_main_menu(self):
        self.previous_menu = None
        items = []
        # Добавляем пункт удаления резюме только если есть созданное резюме
        if self.person is not None:
            items.append(MenuItem("View Resume", self.go_view_resume))
            items.append(MenuItem("Convert Resume to PDF", self.go_resume_to_pdf))
            items.append(MenuItem("Delete Resume", self.go_delete_resume))
        else:
            items.append(MenuItem("Generate Example Resume", self.go_generate_example))
            items.append(MenuItem("Create Resume", self.go_create_resume))
        return Menu(items)
    
    def build_creation_menu(self):
        self.previous_menu = self.menu
        return Menu(items=[
            MenuItem("New Resume", self.create_resume_interactive),
            MenuItem("Edit Resume", self.go_void_action),
        ])

    def create_resume_interactive(self):
        self.person = person_creator()
        self.menu = self.build_main_menu()
    
    def go_back(self):
        if self.previous_menu is not None:
            self.menu = self.previous_menu
            self.previous_menu = None
        else:
            self.menu = self.build_main_menu()

    def go_void_action(self):
        pass
    def go_generate_example(self):
        self.person = None
        self.person = person_generator()
        self.menu = self.build_main_menu()

    def go_create_resume(self):
        self.previous_menu = self.menu
        self.menu = self.build_creation_menu()
        
    def go_resume_to_pdf(self):
        try:
            if self.person is None:
                print("No resume data available to convert.")
                return
            output_path = path_generator(self.person.get_name())
            print(f"Saving PDF to: {output_path}")  # Debug info
            pdf = Format('pdf')
            pdf.transform(path=output_path, persone=self.person)
            print("PDF file created successfully.")
        except Exception as e:
            print(f"Error creating PDF: {e}")
        finally:
            print("\nPress Enter to return to the previous menu.")
            input()
            self.go_back()

    def go_delete_resume(self):
        self.person = None
        self.menu = self.build_main_menu()
    
    def go_view_resume(self):
        #print("\033[H\033[J", end="")
        self.previous_menu = self.menu
        if self.person is not None:
            self.person.show_info()
            print("\nPress Enter to return to the previous menu.")
            input()
            clear_screen()
           # print("\033[H\033[J", end="")
            self.go_back()
        else:
            print("No resume available to view.")

    def run(self):
        while True:
            clear_screen()
            self.menu.display()
            choice = self.menu.get_selection()
           # print(f"DEBUG: choice={choice}, menu_items={[item.name for item in self.menu.items]}")
            if choice is not None:
                selected_item = self.menu.select_item(choice)
                if selected_item:
                    selected_item.select()
                elif choice != -1:
                    print("Invalid selection. Please try again.")
                    continue
            if choice == -1:
                self.go_back()
