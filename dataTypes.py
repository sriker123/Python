Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=None
>>> num
>>> num is None
True
>>> num=''
>>> num
''
>>> num is None
False
>>> nume=2.5
>>> type(nume)
<class 'float'>
>>> nume=2
>>> type(nume)
<class 'int'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> a=5.6
>>> a=int(a)
>>> type(a)
<class 'int'>
>>> b=float(a)
>>> b
5.0
>>> c=complex(a,b)
>>> c
(5+5j)
>>> b=6
>>> c=complex(a,b)
>>> c
(5+6j)
>>> b<a
False
>>> a<b
True
>>> bool =a<b
>>> type(bool)
<class 'bool'>
>>> bool
True
>>> int(True)
1
>>> int(False)
0
>>> lst=[1,4,5,3,1,8]
>>> type(lst)
<class 'list'>
>>> s={3,6,3,7,8,1,5)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s={3,6,3,7,8,1,5}
>>> s
{1, 3, 5, 6, 7, 8}
>>> type(s)
<class 'set'>
>>> t=(2,4,6,2)
>>> t
(2, 4, 6, 2)
>>> type(t)
<class 'tuple'>
>>> str='sriker'
>>> st='s'
>>> type(str)
<class 'str'>
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lst2=list(range(2,11,2))
>>> lst2
[2, 4, 6, 8, 10]
>>> type(lst2)
<class 'list'>
>>> d={'sriker':'one plus', 'kumar':'MI','sandy':'Iphone'}
>>> d
{'sriker': 'one plus', 'kumar': 'MI', 'sandy': 'Iphone'}
>>> d.keys()
dict_keys(['sriker', 'kumar', 'sandy'])
>>> d.values()
dict_values(['one plus', 'MI', 'Iphone'])
>>> d['sriker']
'one plus'
>>> d.get('sriker')
'one plus'
>>> 