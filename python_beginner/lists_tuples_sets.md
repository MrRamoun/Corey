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

<!-- ### sorting a list -->