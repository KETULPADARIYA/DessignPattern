import os


class MenuBuilder:
    """Responsible for building a command line menu system for MenuItems"""

    def __init__(self,*args):
        self.__menu = list()

        for item in args:
            self.__menu.append(item)

    def add(self,menu_item=None,menu_items=None):
        if menu_item is not None:
            self.__menu.extend(menu_items)

        if menu_items is not None:
            self.__menu.append(menu_item)

    def show(self):

        # clear the console
        os.system("cls" if os.name == "nt" else "clear")

        for index,menu_item in enumerate(self.__menu):
            try:
                print("{}. {}".format(index+1,menu_item.prompt))

            except AttributeError:
                raise AttributeError("Could not display the prompt for the current menu item {}".format(str(menu_item)))

        try:
            choice = int(input(">> "))

            for menu_item in self.__menu:
                if choice == self.__menu.index(menu_item) + 1:
                    menu_item.action()

        except KeyboardInterrupt:
            exit()

        except ValueError:
            pass
        self.show()
