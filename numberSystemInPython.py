Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=25
>>> binaryNumber=bin(x)
>>> binaryNumber
'0b11001'
>>> type(binaryNumber)
<class 'str'>
>>> 0b11001
25
>>> 0b101100
44
>>> oct(x)
'0o31'
>>> octN=oct(x)
>>> octN
'0o31'
>>> )0031
SyntaxError: unmatched ')'
>>> 0021
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> hexn=hex(x)
>>> hexn
'0x19'
>>> hex(octN)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    hex(octN)
TypeError: 'str' object cannot be interpreted as an integer
>>> 