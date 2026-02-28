Bunch is a library for operations on bananas.

example:
''
from Bunch import Bunch as b
if __name__ == "__main__":
    string = ")()()()()()())"
    rotated = b.brot(string)
    aligned = b.balign(string)
    print(rotated, aligned)
''