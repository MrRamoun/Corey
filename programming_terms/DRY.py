'''
DRY:
    Don't Repeat Yourself. A principle of software development, aimed at reducing repetition of information of all kinds.

- consider this scinario:
    your boss walks in and says: hey, our code base is a mess and the first thing i want you to do is to make this code DRY.    
'''

#%%
def homepage():
    print('<div class="header">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

    print('<p>welcome</p>')

    print('<div class="footer">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

def aboutpage():
    print('<div class="header">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

    print('<p>welcome</p>')

    print('<div class="footer">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

def contactpage():
    print('<div class="header">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

    print('<p>welcome</p>')

    print('<div class="footer">')
    print('<a href="#">home</a>')
    print('<a href="#">about</a>')
    print('<a href="#">contact</a>')
    print('</div>')

homepage()