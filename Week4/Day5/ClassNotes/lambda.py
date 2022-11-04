# a=[num for num in range(0,10)]

# print[a]

# def multiply(a):
#     return a **2

# print(multiply(2))

#function name lambda <parameter> : <what to return>
multiply= lambda a:a**2

print(multiply(2))

#another example
even= lambda n: n if n %2 == 0 else None

print(even(3))
