
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0): # if the ingredients to make the sandiwch is greater than the resources
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########