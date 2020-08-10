def gen_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = gen_range(1,10)

print(next(nums))

# works exactly as Rangy class but it more readable than the class
