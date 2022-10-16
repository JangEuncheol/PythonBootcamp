from resource import MENU, resources


class Order:
    ERROR_MESSAGE = "Incorrect input"

    def __init__(self):
        self.resource = resources
        self.menu_info = MENU
        menu = input("What would you like? (espresso/latte/cappuccino): ")
        self._serve_coffee(menu)

    def _enter_secret_word(self, answer):
        if answer == "off":
            quit()
        elif answer == "report":
            print(self.resource)
            self._refresh()
        else:
            pass

    def _check_resources_sufficient(self, menu):
        menu_info = self.menu_info.get(menu, self.ERROR_MESSAGE)
        menu_resource = menu_info.get("ingredients")

        if "milk" in menu_resource.keys():
            if menu_resource.get("milk") > self.resource.get("milk"):
                print("Sorry there is not enough milk")
                self._refresh()

        if menu_resource.get("water") > self.resource.get("water"):
            print("Sorry there is not enough water")
            self._refresh()

        elif menu_resource.get("coffee") > self.resource.get("coffee"):
            print("Sorry there is not enough coffee")
            self._refresh()

    def _refresh(self):
        menu = input("What would you like? (espresso/latte/cappuccino): ")
        self._serve_coffee(menu)

    def _serve_coffee(self, menu):
        self._enter_seret_word(menu)
        self._check_resources_sufficient(menu)


