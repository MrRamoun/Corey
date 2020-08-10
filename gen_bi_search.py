nums = (n for n in range(10000000))
print(nums)

def bi(n, nums):
    
    head = nums[0]
    tail = nums[-1]
    middle = (head + tail) / 2

    if n > middle:
        nums = nums[middle:]
        bi(n, nums)
    elif n < middle:
        nums = nums[:middle]
        bi(n, nums)
    elif n == middle:
        return "Found it"
    
print(bi(1000, nums))



