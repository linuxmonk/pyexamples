def addto(original_func):
    print("===in addto===", original_func)

    def wrapper():
        print("===in wrapper===")
        l = [1, 2, 3, 4, 5]
        items = original_func()
        print(f"input items: {items}")
        l.append(items)
        print(f"returning new list {l}")
        return l

    print("===returning wrapper===")
    return wrapper


@addto
def newlist():
    print("in newlist")
    return [10, 12, 14, 16]


def main():
    print("=== main ===")
    nl = newlist()
    print(nl)


if __name__ == "__main__":
    main()
