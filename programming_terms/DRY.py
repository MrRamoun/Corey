'''
DRY:
    Don't Repeat Yourself. A principle of software development, aimed at reducing repetition of information of all kinds.

- consider this scinario:
    your boss walks in and says: hey, our code base is a mess and the first thing i want you to do is to make this code DRY.    
'''

#%%

def navbar():
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

def footer():
    print('<div class="footer">')
    navbar()

def header():
    print('<div class="header">')
    navbar()
    
def homepage():
    header()
    print('<p>welcome</p>')
    footer()

def aboutpage():
    header()
    print('<p>welcome</p>')
    footer()

def contactpage():
    header()
    print('<p>welcome</p>')
    footer()

homepage()