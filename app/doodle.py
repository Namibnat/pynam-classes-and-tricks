"""Random stuff"""


class Button:

    def __init__(self, color, label, mode):
        self.color = color
        self.label = label
        self.mode = mode

    def action(self, foo):
        return foo()

    def turn_on(self):
        self.mode = True

    def turn_off(self):
        self.mode = False


def add():
    return 2 + 2

def sub():
    return 2 - 1


def main():

    B = Button('purple', "Add", True)
    print(B.action(add))

    A = Button('green', 'Subtract', True)
    print(A.color)
    


if __name__ == '__main__':
    main()