# Loops


> **Note**:the indentation in python to indicate that a block of code is part of another structure/statement.


zip(): creates a list of tuples.

enumrate(l, start=1): creates a list of tuples of values & their indicies.

## For

The for loop used to loop through iterables.

> **Note**: the for loop variable can be anything you want. It is not a keywork it is created new variable and you can name it what you want.

```python
nums = [1,2,3,4,5,6]

for num in nums:
    if num == 4:
        print("found it")
        break
    print(num)
else:
    print('not found')
```

> **Note**: nested loops used to get different possible combinations.

```python
for i in range(3):
    for l in 'abc':
        print(i, l)
```

<u>**For Loops iterates through a certain number of values**</u>

<u>**While Loops keeps going until a certain condition is met or until we hit a break.**</u>

## while

```python
x = 0 
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
```

> **Tip**: sometimes you want to create an infinite loop when you want the loop to to never end until we get some input or get some value.

```python
x = 0 
while True:
    if x == 5:
        break
    print(x)
    x += 1
```

> **Tip**: to interupt an infinite loop, `ctrl + c`.