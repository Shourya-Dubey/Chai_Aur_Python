f  = open('chai.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("Chia is here")\n'
>>> f.readline()
'\n'
>>> f.readline()
'username = "hitesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''


################
f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("Chia is here")\n'
>>> f.__next__()
'username = "hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^                                                   
StopIteration





for line in open('chai.py'):
...     print(line)
...     
import time

print("Chia is here")

username = "hitesh"

print(username)
>>> 
>>> for line in open('chai.py'):
...     print(line, end='')
...     
import time
print("Chia is here")
username = "hitesh"





f = open('chai.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end=' ')
...     
...     
import time
 print("Chia is here")
 username = "hitesh"
>>> nt(username) 




test = "hites"
>>> if not test:
...     print('chia')
...     
>>> 
>>> test = ""
>>> if not test:
...     print("chai")
...     
chai






myList = [1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x0000020B54DB7C40>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000020B54DB7C40>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-36>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration





 f = open("chai.py")
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True





myNewList = [1,2,3]
>>> iter(myNewList) is myNewList
False







myList = [1,2,3,4]
>>> D = {'a':1, 'b':2}
>>> for key in D.keys():
...     print(key)
...     
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000020B54DB0FE0>                    
>>> I.__next__()
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<python-input-56>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 





range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> iter(R)
<range_iterator object at 0x0000020B54D8DB50>
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-67>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration