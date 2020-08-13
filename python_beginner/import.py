#%%
import modules as finder
from modules import test, find_index
from modules import test as t, find_index as fi
# from modules import *

hobbies = ['computers', 'computers', 'python', 'ruby']

print(fi(hobbies, 'computer'))
print(fi(hobbies, 'computers'))

print(t)



#%%
import sys

print(sys.path)
sys.path.append('/home/ramoun')


#%%
import antigravity