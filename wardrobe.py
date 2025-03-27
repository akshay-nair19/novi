class Clothing:
    def __init__(self, color, picture, size):
        self.color = color
        self.picture = picture
        self.size = size


class Shirt(Clothing):
    def __init__(self, color, picture, size):
        super().__init__(color, picture, size)


class Pant(Clothing):
    def __init__(self, color, picture, size):
        super().__init__(color, picture, size)


class Wardrobe:
    def __init__(self, items: list):
        self.wardrobe = items

    def add_item(self, item):
        self.wardrobe.append(item)

    def add_multiple_items(self, items: list):
        self.wardrobe.extend(items)

    def remove_item(self, item):
        self.wardrobe.remove(item)

    def get_items(self):
        return self.wardrobe


class Shirt_list(Wardrobe):
    def __init__(self, shirts: list):
        super().__init__(shirts)


class Pant_list(Wardrobe):
    def __init__(self, pants: list):
        super().__init__(pants)


class History:
    def __init__(self):
        self.history = []

    def wear_outfit(self, outfit: tuple):
        if len(self.history) >= 7:
            self.history.pop(0)
        self.history.append(outfit)

    def print_history(self):
        for i, (shirt, pant) in enumerate(self.history, 1):
            print(f"Outfit {i}: Shirt({shirt.color}, {shirt.picture}) - Pant({pant.color}, {pant.picture})")




if __name__ == '__main__':
    print('hello')