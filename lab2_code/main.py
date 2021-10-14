from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 20, 19)
    c = Circle("зеленого", 20)
    s = Square("красного", 20)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()