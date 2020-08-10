from iterators_and_iterables import Rangy
import sys

# 010 - 01907742
try:
    arg = sys.argv[1]
except:
    sys.exit("please, make sure you are followinng the guide corrently for setting arguemnts for the script")

isp_keys = {
        'voda': '010', 
        'etslt': '011', 
        'orng': '012', 
        'we': '015'
        }

# part1 = 0000 - 9999
# part2 = 0000 - 9999


if arg not in isp_keys.keys():        
    sys.exit("sorry, not a valid argument")

for part1 in Rangy(0, 10000):
    for part2 in Rangy(0, 10000):
        print(isp_keys[arg] + "%.4d"%(part1) + "%.4d"%(part2))
        
print(arg + ", have finished successfuly.")


