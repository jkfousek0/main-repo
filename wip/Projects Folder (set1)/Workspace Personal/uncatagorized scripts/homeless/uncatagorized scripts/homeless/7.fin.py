Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 1
>>> b = 2
>>> print('\nVariable a Is:','one',if(a == 1)else 'not one')
SyntaxError: invalid syntax
>>> print('\nVariable a Is:','one'if(a == 1)else 'not one')

Variable a Is: one
>>> print( 'Variable b is :','even'if(b % 2 == 0)else 'odd')
Variable b is : even
>>> print('\nVariable a Is:','one'if(a % 2 == 0)else 'not one')

Variable a Is: not one
>>> print('\nVariable b Is:','one'if(b == 1)else 'not one')

Variable b Is: not one
>>> max_py = a if (a > b) else b
>>> print('\nGreater Value Is:',max_py)

Greater Value Is: 2
