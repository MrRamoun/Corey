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