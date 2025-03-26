class Shirt:
    def __init__(self, color, picture, size):
        self.color = color
        self.picture = picture
        self.size = size


class Shirt_list:
    def __init__ (self, colors: list):
        self.wardrobe = colors
    def add_shirt(self, shirt):
        self.wardrobe.append(shirt)
    def add_multiple_shirts(self, shirts: list):
        self.wardrobe.extend(shirts)
    def remove_shirt(self, shirt):
        self.wardrobe.remove(shirt)
    def get_shirts(self):
        return self.wardrobe


class Pant:
    def __init__(self, color, picture, size):
        self.color = color
        self.picture = picture
        self.size = size


class Pant_list:
    def __init__ (self, colors: list):
        self.wardrobe = colors
    def add_pant(self, pant):
        self.wardrobe.append(pant)
    def add_multiple_pants(self, pants: list):
        self.wardrobe.extend(pants)
    def remove_pant(self, pant):
        self.wardrobe.remove(pant)
    def get_pants(self):
        return self.wardrobe


class History:
    def __init__ (self):
        self.history = []
    def wear_outfit(self, outfit: tuple):
        if len(self.history) >= 7:
            self.history.pop(0)  
        self.history.append(outfit)
    def print_history(self):
        for i, (shirt, pant) in enumerate(self.history, 1):
            print(f"Outfit {i}: Shirt({shirt.color}, {shirt.picture}) - Pant({pant.color}, {pant.picture})")