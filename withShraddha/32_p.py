def evenNum():
    with open("practice.txt", 'r') as f:
        data = f.read()

    nums = data.split(", ")
    print(nums)

    count = 0

    for i in nums:
        if (int(i) % 2 == 0):
            count += 1

    return count


print(evenNum())
