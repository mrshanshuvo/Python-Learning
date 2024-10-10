    speeds = map(int, input().split())

    speeds = (sorted(speeds, reverse=True))

    a = speeds[0]

    if (a >= 20):
        print(3)
    elif (a < 10):
        print(1)
    else:
        print(2)
