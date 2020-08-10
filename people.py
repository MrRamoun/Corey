import random
import time

names = ['john', 'ramoun', 'omar', 'aya', 'angry', 'man']
majors = ['Math', 'Engineering', "Computer", 'Economy']

# memory usage profile goes here

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                'id': i,
                'name': random.choice(names),
                'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
                'id': i,
                'name': random.choice(names),
                'major': random.choice(majors)
                }
        yield person

t1 = time.time()
# people = people_list(1000000)
people = people_generator(1000000)
t2 = time.time()


print(t1)
print(t2)
