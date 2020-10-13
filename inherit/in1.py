class Base:
    def __init__(self):
        print("Base")


class Derived(Base):
    def __init__(self):
        super(Derived, self).__init__()
        print("Derived")

    @classmethod
    def new(cls, base):
        cls.__class__ = derived_class


if __name__ == "__main__":
    print("b = B(): ")
    b = B()
    print("d = D(): ")
    d = D()
    x = b
    print("x = b: type(x): {}".format(type(x)))
    print("x = Derived.new(): type(x): {}".format(type(x)))
    x = Derived.new(base)
