def inf_gen(start):
    current = start
    while True:
        yield current
        current += 1

nums = inf_gen(10)
# print(type(nums))


for n in nums:
    print(n)

