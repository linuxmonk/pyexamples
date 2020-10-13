n = 1000


def firsttest(input, n):
    ans = 0
    try:
        ans = n / input
    except:
        print("oops there as an error")
    finally:
        print("finally block")

    print(f"answer is {ans}")


def secondtest(input, n):
    ans = 0
    try:
        x = int(input)
        ans = n / x
    except:
        print("oops there as an error")
    finally:
        print("finally block")

    print(f"answer is {ans}")


if __name__ == "__main__":
    userinput = input("Enter a number: ")
    print("--- first test ---")
    firsttest(userinput, n)
    print("--- second test ---")
    secondtest(userinput, n)
