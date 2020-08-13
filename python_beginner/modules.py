#%%
print("modules module was imported successfully.")

test = 'test string'

def find_index(l, target):
    for index, item in enumerate(l):
        if item == target:
            return index

    return -1

if __name__ == '__main__':
    print(find_index([1,2,3,4,5,6], 3))
    
    print(find_index([1,2,3,4,5,6], 20))


#%%
import random

hobbies = ('computers', 'computers', 'programming', 'art', 'science')

print(random.choice(hobbies))


#%%
import math

rads = math.radians(90)

print(rads)
print(math.sin(rads))


#%%
    import datetime
    import calendar

    todays_date = datetime.date.today()
    
    print(todays_date)
    print(calendar.isleap(2020))


#%%
    import os
    
    print(os.getcwd())


#%%
import os

print(os.__file__) # the dunder file attribute
