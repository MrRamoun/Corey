# things to remember about Generators:
# 1. the for loop know how to handle the StopIteration Exception.
# 2. 

def sqnum(nums):
    result = []
    for n in nums:
        result.append(n*n)
    return result

def sqnum_trying_to_be_smart(nums):
    for n in nums:
        return n

def i_am_the_real_smart_cus_i_am_a_generator_function(nums):
    for n in nums:
        yield n*n

sqdnums = sqnum([1,2,3,4,5,6])
sqdnums_trying = sqnum_trying_to_be_smart([1,2,3,4,5,6])
finally_the_smart_guy = i_am_the_real_smart_cus_i_am_a_generator_function([1,2,3,4,5,6])


print(sqdnums)
print(sqdnums_trying)
print(dir(finally_the_smart_guy))
print("*"*20)

for i in finally_the_smart_guy:
    print(i)

###################################

# using the list comprehension

sqrdnums = [x*x for x in [1,2,3,4,5,6,7]]
print(sqrdnums)

sqrdnums = (x*x for x in [1,2,3,4,56]) # using comprehensed generators
print(sqrdnums)


for n in sqrdnums:
    print(n)









