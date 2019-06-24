Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(keywords)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                

help> 
================== RESTART: /home/bmsce/pythonprogs/fgkj.py ==================
Bhoomika
>>> 
================== RESTART: /home/bmsce/pythonprogs/name.py ==================
Bhoomika
>>> a=5
>>> b="hello"
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a*b)
hellohellohellohellohello
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> help(a)

>>> x=2
>>> y=3
>>> if x<y:
	print(x)
	elif x>y:
		
SyntaxError: invalid syntax
>>> 
=============== RESTART: /home/bmsce/pythonprogs/lessgreat.py ===============
2
>>> 
=============== RESTART: /home/bmsce/pythonprogs/lessgreat.py ===============
2
>>> i=0
>>> while i<10:
	print(i)
	i+=1
print(i)
SyntaxError: invalid syntax
>>> while i<10:
	print(i)
	i+=1

0
1
2
3
4
5
6
7
8
9
>>> print(i)
10
>>> while i<10:
	print(i)
	i+=1

	
>>> mylist=[1,2,"hello"]
>>> mylist[0]
1
>>> dir(mylist)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(mylist)

>>> mylist[2:3]
['hello']
>>> mylist+=mylist
>>> mylist += mylist
>>> mylist*4
[1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello']
>>> 2 in mylist
True
>>> mylist.pop()
'hello'
>>> mylist[::-1]
[2, 1, 'hello', 2, 1, 'hello', 2, 1, 'hello', 2, 1]
>>> mylist[::1]
[1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2]
>>> mylist.__add__(2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    mylist.__add__(2)
TypeError: can only concatenate list (not "int") to list
>>> mylist.__len__
<method-wrapper '__len__' of list object at 0x7fc13e7ca088>
>>> mylist.__getitem__
<built-in method __getitem__ of list object at 0x7fc13e7ca088>
>>> mylist.__sizeof__
<built-in method __sizeof__ of list object at 0x7fc13e7ca088>
>>> for i in mylist:
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in mylist:
	print (i)

	
1
2
hello
1
2
hello
1
2
hello
1
2
>>> for i in range(10):
	print (i)

	
0
1
2
3
4
5
6
7
8
9
>>> mylist=[1,2,"hello',[1,2,3]]
	    
SyntaxError: EOL while scanning string literal
>>> mylist=[1,2,"hello",[1,2,3]]
	    
>>> for i in mylist:
	    print(i)

	    
1
2
hello
[1, 2, 3]
>>> for i in range(10):
	    print(i)

	    
0
1
2
3
4
5
6
7
8
9
>>> range(10)
	    
range(0, 10)
>>> x=range(10)
	    
>>> dir(x)
	    
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
>>> iterator=iter(x)
	    
>>> dir(iterator)
	    
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> iterator.__next__()
	    
0
>>> iterator.__next__()
	    
1
>>> iterator.__next__()
	    
2
>>> iterator.__next__()
	    
3
>>> iterator.__next__()
	    
4
>>> iterator.__next__()
	    
5
>>> iterator.__next__()
	    
6
>>> iterator.__next__()
	    
7
>>> iterator.__next__()
	    
8
>>> iterator.__next__()
	    
9
>>> iterator.__next__()
	    
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    iterator.__next__()
StopIteration
>>> iterator.__reduce__()
	    
(<built-in function iter>, (range(0, 10),), 10)
>>> 
	    
>>> for i in range(-9)
	    
SyntaxError: invalid syntax
>>> for i in range(-9):
	    print(i)

	    
>>> 
	    
>>> x=range(9 , 1)
	    
>>> 
	    
>>> for i in range(x):
	    print(i)

	    
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    for i in range(x):
TypeError: 'range' object cannot be interpreted as an integer
>>> help()
	    

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> range
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> mylist=[]
	    
>>> for i in range(9, 1[,-1]):
	    
SyntaxError: invalid syntax
>>> for i in range(9, 1[,1]):
	    
SyntaxError: invalid syntax
>>> for i in range(9, 1,[-1]):
	    print(i)

	    
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    for i in range(9, 1,[-1]):
TypeError: 'list' object cannot be interpreted as an integer
>>> mylist=[]
	    
>>> for i in range(10):
	    mylist.append(i*i)

	    
>>> 
	    
>>> mylist=[i*i for i in range(10)]
	    
>>> 
	    
>>> print(mylist)
	    
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> mylist=[i*i for i in range(10) if i%2]
	    
>>> print(mylist)
	    
[1, 9, 25, 49, 81]
>>> mylist=[i*i for i in range(10) if i%2==0]
	    
>>> 
	    
>>> print(mylist)
	    
[0, 4, 16, 36, 64]
>>> mylist=[i*i for i in range(10) if i%2!=0]
	    
>>> print(mylist)
	    
[1, 9, 25, 49, 81]
>>> a={1:"hello",2:"world"}
	    
>>> a.keys()
	    
dict_keys([1, 2])
>>> a.values()
	    
dict_values(['hello', 'world'])
>>> a.items()
	    
dict_items([(1, 'hello'), (2, 'world')])
>>> a={"hello":"world"}
	    
>>> a{"hello"}
	    
SyntaxError: invalid syntax
>>> a["hello"]
	    
'world'
>>> del(a["hello"])
	    
>>> a
	    
{}
>>> mytuple=(1,2,3)
	    
>>> mytuple[0]=1
	    
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    mytuple[0]=1
TypeError: 'tuple' object does not support item assignment
>>> s = input('--> ')
	    
--> 1
>>> s
	    
'1'
>>> type(s)
	    
<class 'str'>
>>> s=int(s)
	    
>>> s
	    
1
>>> def input():
	    a=int(input("Enter a"))
	    b=int(input("Enter b"))
	    return a,b

	    
>>> x,y=input()
	    
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    x,y=input()
  File "<pyshell#131>", line 2, in input
    a=int(input("Enter a"))
TypeError: input() takes 0 positional arguments but 1 was given
>>> def myinput():
	    a=int(input("Enter a"))
	    b=int(input("Enter b"))
	    return a,b

	    
>>> x,y=myinput()
	    
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    x,y=myinput()
  File "<pyshell#134>", line 2, in myinput
    a=int(input("Enter a"))
TypeError: input() takes 0 positional arguments but 1 was given
>>> delete(input)
	    
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    delete(input)
NameError: name 'delete' is not defined
>>> del(input)
	    
>>> def myinput():
	    a=int(input("Enter a"))
	    b=int(input("Enter b"))
	    return a,b

	    
>>> x,y=myinput()
	    
Enter a1`
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    x,y=myinput()
  File "<pyshell#139>", line 2, in myinput
    a=int(input("Enter a"))
ValueError: invalid literal for int() with base 10: '1`'
>>> x,y=myinput()
	    
Enter a1
Enter b2
>>> x,y
	    
(1, 2)
>>> def add(a,b):
	    return a+b

	    
>>> def myprint(a,b,mysum):
	    print("%d +%d=%d"%mysum)

	    
>>> def main():
	    a,b=myinput()
	    s=add(a,b)
	    myprint(a,b,s)

	    
>>> main()
	    
Enter a1
Enter b2
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    main()
  File "<pyshell#153>", line 4, in main
    myprint(a,b,s)
  File "<pyshell#148>", line 2, in myprint
    print("%d +%d=%d"%mysum)
TypeError: not enough arguments for format string
>>> def myprint(a,b,mysum):
	    print("%d +%d=%d"%(a,b,mysum))

	    
>>> main()
	    
Enter a1
Enter b2
1 +2=3
>>> 
================== RESTART: /home/bmsce/pythonprogs/add.py ==================
Enter a2
Enter b3
>>> 
	    
>>> 
	    
>>> 
================== RESTART: /home/bmsce/pythonprogs/add.py ==================
>>> main()
	    
Enter a1
Enter b2
1 + 2 = 3
>>> 
