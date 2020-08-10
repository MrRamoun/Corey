class Rangy:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

if __name__ == "__main__":
    for i in Rangy(1,10):
        print(i)

    print(type(Rangy(1,2)))   
    print(list(Rangy(1,11)))
    print(dir(Rangy))

# the class Rangy is iterable because we can use it in a for loop but it is also an iterator because it has a __next__() method
