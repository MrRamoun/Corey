# py_tips

## To know functions available for an object

```python
dir(obj)
```

## To get help and info about a function or a class

```python
help(obj)
help(obj.method)
```

## To see the class of an object 

```python
type(str)
```

## To get the memory-address of an obj

```python
id(ojb) # returns it in decimal base
```

## How to choose a type for your number!!!

sometimes you want the numbers in your program to be stored as strings not ints/floats.But How to know when to do that?

> just check for the following:

1. is your number going to have arithmetic/comparison operations applied to it? then don't use strings.
1. is your number just there for display only? then use strings.

> Example:  
> Phone numbers -> strings  
> student id -> numeric  
> amount of money -> da!!

## General Tips while programming

- make sure to checkout the return value of each function/method you use.