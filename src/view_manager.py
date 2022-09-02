import os

class ViewManager:

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self, text):
        print(text)
