//Q1: WWPD: Control
//1. 
def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin")

>>> how_big(7)

>>> print(how_big(7))
big

>>> how_big(12)
huge

>>> how_big(1)
small

>>> how_big(-1)
nothin

//2. 
n = 3
while n >= 0:
    n -= 1
    print(n)
2
1
0
-1

//3. 
positive = 28
while positive:
   print("positive?")
   positive -= 3
INFINITY Loop
[While] This repeatedly tests the expression and, if it is true, executes the first suite;
Non-zero values are True. Zero is false.

//4. 
positive = -9
negative = -12
while negative:
   if positive:
       print(negative)
   positive += 3
   negative += 3
-12
-9
-6

//Q2: WWPD: Veritasiness

//Boolean Operations — and, or, not
//x OR y  if x is false, then y, else x
//x AND y  if x is false, then x, else y
//not x  if x is false, then True, else False


>>> True and 13
13

>>> False and 13
False

>>> False or 0
0

>>> not 10
False

>>> not None
True

>>> print((2>3) and 13)
False

>>> print(False or (2>3))
False




>>> True and 1 / 0 and False
ERROR 

>>> True or 1 / 0 or False
True

>>> True and 0
0

>>> False or 1
1

>>> 1 and 3 and 6 and 10 and 15    
15

>>> -1 and 1 > 0
True

>>> 0 or False or 2 or 1 / 0    
2


>>> not 0
Ture

>>> (1 + 1) and 1
1

>>> 1/0 or True
ZeroDivisionError: division by zero

>>> (True or False) and False
Flase


>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
10
foo

>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)
______
1
29

>>> bake(1, "mashed potatoes")
______
mashed potatoes

