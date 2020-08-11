# numerics

python has 3 numeric data type.

<br>

## Integers (<class 'int'>)

Theses are integer numbers. Whole numbers with no decimal point.

> **Note**: python is a dynamic PL. So, number that are in range (-2<sup>31</sup> : 2<sup>31</sup>) take about 4 bytes in memory. While numbers beyond that range take more space :).

<br>

## Floats (<class 'float'>)

These are decimal point numbers.

<br>

## Arithmetic Operations on Numerics

    # Arithmetic Expressions:
    # Addition:        3 + 2    
    # Subtraction:     3 - 2
    # Multiplication:  3 * 2
    # Division:        3 / 2
    # Floor Division:  3 // 2
    # Exponent:        3 ** 2
    # Modulus:         3 % 2

> **Note**: arithmetic operations follow the normal mathematical *order of operations*.

> **Note**: The `'()'` are the crown that has the ability to change order of operations.

<br>

## Expressions 

There is 2 types of Expressions in python: **arithmetic** Expressions and **Boolean** Expressions.

> **Note**: Expressions are automatically evaulted into one value in python. Whenever an Expression is encoutnered it's evaluated immediatly. 

> **Note**: Expressions can be part of a statement.

<br>


## Assignment Statements

**`=`** : this symbol is the most important symbol in programming

```python
x = x + 1 # (x+1) is an arithmetic expressions that gets evaluated first then assigned to the x variable on the left side.
```
> **Note**: variables are considred expressions (single-value expressions). Evaluation of variables is their contained `value`.

> **Note**: The order of operations in the last assignment statement statement is as follows:  

    1. (x+1) experssions is evaluated first.
    2. right-side 'x' is evaluated to a value.
    3. the vlaue of 'x' is replaced and the expression (x+1) is evaluated to a value.
    4. the assignment satement is executed lastly (assigning the value of (x+1) expression to the x variable).

> **Note**: That assignment statement has a shortcut -> `x += 1`

<br>

## Built-in Python function to Deal with Numbers

1. `round()`:
    ```python
    print(round(33.3)) # output: 33
    print(round(33.4)) # output: 33
    print(round(33.5)) # output: 34
    print(round(33.6)) # output: 34
    ```
    you can alos control the rounding method specificly to how many digits after decimal point

    ```python
    print(round(33.3, 4)) # output: 33.3
    print(round(33.3, 2)) # output: 33.3
    print(round(33.3, 3)) # output: 33.3
    print(round(33.3, -1)) # output: 30.0
    ```


1. `abs()`
    ```python
    print(abs(10)) # ouput: 10
    print(abs(-10)) # ouput: 10
    print(abs(-100)) # ouput: 100
    print(abs(-10.33)) # ouput: 10.33
    ```

<br>
    
## Comparison Operations on Numerics

    # Comparisons:
    # Equal:             3 == 2
    # Not Equal:         3 != 2
    # Greater Than:      3 > 2
    # Less Than:         3 < 2
    # Greater or Equal:  3 >= 2
    # Less or Equal:     3 <= 2

> **Note**: The Comparisons are boolean Expressions that return only one of 2 values either `True` or `False`.

<br>

## Casting

Casting is simply explicit conversion of one data type to another.

**case**: maybe you got some numbers from a text file or from a webpage. Theses numbers are of type `<class 'str'>`.

```python
# problem: number read from a textfile/webpage
number1 = '200'
number2 = '300'
print(number1 + number2) # output: '200300'

# solving problem by casting
number1 = int('200')
number2 = int('300')
print(number1 + number2) # output: 500
```
