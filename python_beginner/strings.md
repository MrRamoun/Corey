# strings

<br>

## single vs double

it really depends on the textual-content. If text containt single qoute -> then better use double quote and vice-versa.

> **Note**: python also supports triple quotes.

```python
string = 'martin's quote'
# no you can see the problem -> python thinks that the second single quote is the terminating quote.
```

> **quick-fix**: use escape character (`'\'`).

```python
string = 'martin\'s world'
# as you can see works as charm
```
> [!**IMPORTANT**]
>: it is considered best practice to user dobule quotes instead to fix that problem. For more Python Best Practices [click](https://www.google.com/search?q=python+best+practices&oq=python+best+practices&aqs=chrome..69i57j0l7.3861j0j9&sourceid=chrome&ie=UTF-8 "on google").

```python
string = "ramoun's code"
# no you can see
```

>**or**

```python
string = '''ramoun's world is "awesome"'''
# as you can see triple quotes works for both cases.
```

> **Note**: another feature that triple quotes provide is that it allows spanning string on multiple lines.

```python
some_multi_line_string = """this is line 1
and this is line 2 as you can see
and this is line 3
"""
'''
the output:
this is line 1
and this is line 2 as you can see
and this is line 3
'''
```

> **Note**: if you notice, triple quotes can be used as multiline comments too. Actually they are alos used for *python code documentation* and they are called **doc strings**.

<br>

## Indexing & slicing

basically strings are strings (`list`s) of characters.

And python provides us with an arsenal to deal with strings (doing operations and such...). This Arsenal is called **slicing**.


    string[start:end:step]
        

```python
string = 'hello'
print(string[0]) # output: 'h'
print(string[4]) # output: 'o'
print(len(string)) # output: 5 , the length (number of letters in a string)
print(string[1:3]) # output: 'el' , because start pos is inclusive but end pos is exclusive
print(string[1:]) # output: 'ello' , because leaving the (start/end) pos empty means (from begining/to end)
print(string[:3]) # output: 'hel'
print(string[:]) # output: 'hello'
print(string[::2]) # output: 'hlo'
print(string[::-1]) # output: 'olleh'
print(string[::-2]) # output: 'olh'
```
    >>=>> remember: these slicing techniques can be used with lists too.

> **Note**: if the step is **-ve** then that will reverse the order of character.:confused::worried:



|<u>*index*</u>  |0  |1  |2  |
|---------|---------|---------|---------|
|<u>**_chars_**</u>| r| u| n|
|<u>**_negative-index_**</u>| -3| -2| -1|


## string methods

**Methods**: are functions that belong to an object.

> **Note**: to see all methods available for a `string` object use:

```python
dir(str)
```

Here is some of the most used methods:

```python
msg = 'hello wOrLd'
print(msg.upper()) # output: HELLO WORLD
print(msg.lower()) # output: hello world
print(msg.capitalize()) # output: Hello world
print(msg.count('o')) # output: 2
```

And more about the **`find`** method:

```python
msg = 'hello WoRlD'
print(msg.find('W')) # output: 6 , it returns the index of the letter we are looking for.
print(msg.find('WoRlD')) # output: 6, it returns the index of the first letter of the word we are looking for.
print(msg.find('something')) # output: -1, if it doesn't find the word we are looking for it returns -1.
print(msg.find('z')) # output: -1
```

The **`replace`** method:

```python
msg = 'hello world'
msg.replace('world', 'ramoun') 
print(msg) # output 'hello world' , because it is not making the replacement in place -> it is returning new string with those values replaced.

# we need to caputer the returned value with a variable
new_msg = msg.replace('world', 'ramoun') 
print(new_msg) # output: 'hello ramoun'
```
<br>

## String Formatting

### 1. concatenation:

pretty basic and easy to understand but really tidious because it is hard to keep track of all the plus signs espcially with long strings

```python
name = 'ramoun'
age = '25' # wait a minute!!..don't worry will be explained later.

print(name + ' is a ' + age + ' years old programmer.')
# output: 'ramoun is a 25 years old programmer.'
```

### 2. .format():

strings in python has a very userful and important method called the .format method.

it is used for fromating strings easily in a readable way.

```python
name = 'ramoun'
age = '25' # wait a minute!!..don't worry will be explained later.

print('{} is a {} years old programmer.'.format(name,age))
# output: 'ramoun is a 25 years old programmer.'
```

> **or**

```python
print('{0} is a {1} years old programmer.'.format(name,age))
# output: 'ramoun is a 25 years old programmer.'
```

> **or**

```python
print('{name} is a {age} years old programmer.'.format(name=name, age=age))
# output: 'ramoun is a 25 years old programmer.'
```

### 3. fstrings:

> [!CAUTION]
> fstrings are only available in python 3.6+ 

basically the idea behind fstrings is to make string formatting as easy and simple as possible.

```python
print(f'{name} is a {age} years old programmer.')
# output: 'ramoun is a 25 years old programmer.'
```

> **Note**: `fstrings` have very awesome feature too. You can actually write code within the placeholder.

```python
print(f"{name.replace('o', '#')} loves computers so much!.")
```
