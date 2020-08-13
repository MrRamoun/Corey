# Modules

The imported module must be in the same directory or in the python directory (depends on the os).

## adding my own dir

using the sys library you can add the directory that contains other modules to your python file and that way you can import theses moudles easily

when we import a module, python checks multiple locations and the locations that it checks are present in a list that we can access using `sys.path`.

directories are added in this order:

    1. first the directory containing the script that we are running.
    1. next the python path envrionment variable.
    1. after that, the standard library directories.
    1. lastly, the site-packages directory for 3rd party packages.
```python
# checking the paths that python looks in when trying to find an imported moodule

import sys
print(sys.path)
```

> **Note**: `sys.path` as a variable that holds a list of 

you can use any path you want by adding the path to the sys.path list.Or modify the python path environment variable.

```bash
export PYTHONPATH="/the/path/to/module"
```
> **Note**: if you have a problem with python path environment variable due to using specific ide or editor. You can google `<editor> python path`

## modules got different names

moudles are: python files, python scrips.

libraries: are a group of modules

packages: are 3rd party libraries

## wild cards

are not recommended to use because we can't tell what came from what imported module and it can cause conflicts if 2 modules have the same functions/vars identifiers.

## The standard Library

the standard library is very userful because if you are performing a common task, most likely someone has written the functionality and it's written by the best programmers in the world + it has been optimized to be as performent as possible.

Examples to show how standard library modules are very useful

> **Tip**: try to use the standard library whenever possible because its modules are the most optimized. If the functionality you are looking for is not in the standard library then you can use a 3rd party package.

### Important modules from the standard library:

- for random operations

    ```python
    import random
    
        hobbies = ('computers', 'computers', 'programming', 'art', 'science')
    
    print(random.choice(hobbies))
    ```

- python's math library is the best

    ```python
    import math
    
    rads = math.radians(90)
    
    print(rads)
    print(math.sin(rads))
    ```

- for date and time calculations

    ```python
    import datetime
    import calendar

    todays_date = datetime.date.today()
    
    print(todays_date)
    print(calendar.isleap(2020))
    ```

- want acces for the underline operating system

    ```python
    # printing the current working directory of the current script
    import os
    
    print(os.getcwd())
    ```

### final thoughts about standard library modules:

These modules are just other python scripts and you can view the location of these scripts using the `__file__` attribute.

```python
import os

print(os.__file__) # the dunder file attribute
```

> **Remember**: The standard library provides you with a ton of functionality that might be tricky or could take you forever to wirte yourself.

> **Tip**: don't be afraid to go to the standard library and look around how different things are done, it is a great way to learn. There is diffenitly some complicated code in there but you are gonna be surprised how much you can understand if you just poke around with it.