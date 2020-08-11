# Lists, Tuples, and Sets

## Lists

just as the name implies, it allows us to work with lists of values.

### creating a list:

```python
l = [1,3,2,3]
l = list((1,2,3,4))
l = []
l = list()
```

### indexing:

same as string [indexing/slicing](https://github.com/MrRamoun/Corey/blob/master/python_beginner/strings.md "strings lesson on github")

### adding items to the list:

- adding an item to the end of the list

    ```python
    l = ['hi', 1, 2]
    l.append(300)
    print(l) # output: ['hi', 1, 2, 300]
    ```

- adding an item to a specific index (pos) in the list

    ```python
    l = ['hello', 1, 2.3]
    l.insert(1, 'python')
    print(l) # output: ['hello', 'python', 1, 2.3]
    ```
- adding multiple items at once
    ```python
    l = ['hello', 1, 2.3]
    l2 = ['i','luv','programming']
    l.extend(l2)
    print(l) # output: ['hello', 1, 2.3, 'i', 'luv', 'programming']
    ```

    > **Tip**: try using `.insert(l2)` & .`append(l2)` and see what's gonna happen.

> **Note**: lists in python can contain other lists.

### removing items from a list:

- removing item by value

    ```python
    l = [1,2,3]
    l.remove(2)
    print(l) # output: [1, 3]
    ```

- removing last item of a list

    ```python
    l = [1,2,3]
    l.pop()
    print(l) # output: [1, 2]
    ```
    > **Note**: `pop()` returns the removed item.
    > **Note**: `pop()` is very useful for creating a stack/queue.

- removing items by index

    ```python
    l = [1,2,3]
    l.pop(1)
    print(l) #output: [1, 3]
    ```

### sorting a list:

- strings are sorted alphabetically (by default)

    ```python
    names = ['michael', 'john', 'josh', 'david']
    names.sort()
    print(names) # output: ['david', 'john', 'josh', 'michael']
    ```

- numbers are sorted in ascending order

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.sort()
    print(numbers) # output: [1, 2, 3, 11, 33, 55, 12231]
    ```

- if i want to sort in reverse order

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.sort(reverse=True)
    print(numbers) # output: [12231, 55, 33, 11, 3, 2, 1]

    names = ['michael', 'john', 'josh', 'david']
    names.sort(reverse=True)
    print(names) # output: ['michael', 'josh', 'john', 'david']
    ```

    > **Note**: i could use `numbers.sort().reverse()`. but it is considered good practice to use the `reverse` parameter of the `.sort()` method.

- sorting without altering the original list

    ```python
    names = ['michael', 'john', 'josh', 'david']
    numbers = [3, 33, 55, 11, 2, 12231, 1]

    sorted_names = sorted(names)
    sorted_numbers = sorted(numbers)

    print(names)
    print(sorted_names)
    ```

    > **Note**: `sorted()` returns a sorted copy of the passed list.

### useful list methods:

- reversing a list
    
    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.reverse()
    print(numbers) # output: [1, 12231, 2, 11, 55, 33, 3]
    ```    

- minimum value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(min(numbers)) # output: 1
    ```    
- maximum value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(max(numbers)) # output: 12231
    ```    
- sum of values of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(sum(numbers)) # output: 112336
    ```   

- index of a value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(numbers.index(12231)) # output: 5
    ```   
    > **Tip**: try to find out the index of a value of a non-existing element.

- check if a value in a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print('ramoun' in numbers) # output: False
    ```
   
> **Tip**: try to apply these methods to the `names` list and checkout the results you'll get.

### converting lists into strings & vice versa:

- conversion of lists into strings

    ```python
    l = ['a','b','c']
    str_l = ', '.join(l)
    print(str_l) # output: a, b, c   
    ```

- conversion of strings into lists

    ```python
    l = str_l.split(', ')
    print(l) # output: ['a', 'b', 'c']
    ```

