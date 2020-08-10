'''
"Therefore, in simple terms: A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing".
'''

def outer():
    msg = 'hi'

    def inner():
        print(msg)

    # return inner() # calls inner() and returns None
    return inner # removing the parenthises -> returning function as an obj without execution (there is no call to the function)

outer()

def logger(msg):
    def log_msg():
        print("log: ", msg)
    return log_msg

log_hi = logger('hi')
log_hi()


def html_tag(tag):
    def html_content(content):
        print("<{0}>{1}</{0}>".format(tag, content))
    return html_content

h1_tag = html_tag("h1")
print(h1_tag("hello"))

"""
Long Storgy Short: 
    first class funcs: are functions treated as objects by ommiting the '()'
"""
