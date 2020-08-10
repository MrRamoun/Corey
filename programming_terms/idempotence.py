"""
Idempotence:
    is the property of certain operations in mathematics and computer science, that can be applied multiple times without changing the result beyond the initial application.    

Defination:
    $ f(f(x)) = f(x)

Good tip from Microsoft:
    Idempotent systems, like the elevator, result in the same outcome no matter how many times identical commands are issued.    
"""

#%%
# Not Idempotent

## doesn't follow the difenation
def add_ten(n):
    return n + 10

print(add_ten(10)) # f(10) = 20
print(add_ten(add_ten(10))) # f(f(10)) = 30 

# %%

# Idemptent funcs

print(abs(-10)) # f(-10) = 10
print(abs(abs(-10))) # f(f(-10)) = 10

# %%
a = 10 # idempotent statement

# %%
# Believe it or not : Http methods are idempotent

GET  <url>/users/123 # if you tried to load the url/userpage of one user no-matter how many times you reload the page and reload it, it is gonna give the same result everytime.
PUT  # consider the scienario of setting the user name of my account on fb to the same username over and over again -> that is considered idempotence
POST # is not considered idempotent -> consider a site traffic counter -> each time you try to reload the page the counter will change -> so no idempotent
DELETE # is considered idempotent -> no matter how many times you call the delete function it is not gonna change anything (just the first time only - and that is considered normatl like the abs(-10)).


# %%
# Microsoft
'''
When it comes to building applications, consider the following scenarios:

- What happens if your inventory control application tries to delete the same product more than once?
- How does your human resource application behave if there is more than one request to create an employee record for the same person?
- Where does the money go if your banking app gets 100 requests to make the same withdrawal?
- There are many contexts where requests to a function may receive identical commands. Some situations include:

- Retry policies sending the same request many times.
- Cached commands replayed to the application.
- Application errors sending multiple identical requests.

To protect data integrity and system health, an idempotent application contains logic that may contain the following behaviors:

- Verifying of the existence of data before trying to execute a delete.
- Checking to see if data already exists before trying to execute a create action.
- Reconciling logic that creates eventual consistency in data.
- Concurrency controls.
- Duplication detection.
- Data freshness validation.
- Guard logic to verify input data.

Ultimately idempotency is achieved by ensuring a given action is possible and is only executed once.

Long Story Short: trying to make sure that when a function (action) is called more than once -> the same result should be obtained (and functions/actions that have this property are called 'idempotent')
'''
# %%
# str is also an idempotent function !enjoy!

str(str(str(str(str(str(str("mark")))))))