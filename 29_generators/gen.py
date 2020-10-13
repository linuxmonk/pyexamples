def times_four(n):
    print("=== in times_four ===")
    for i in range(n):
        print(f"=== before yield: loop i={i}, n={n}")
        yield i * 4
        print(f"=== after  yield: loop i={i}, n={n}")


for i in times_four(10):
    print(i)
