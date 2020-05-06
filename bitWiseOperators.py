Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ~12
-13
>>> bin(-13)
'-0b1101'
>>> 0011
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 1b0011
SyntaxError: invalid syntax
>>> 0b001
1
>>> 0b0011
3
>>> 12&13
12
>>> 12|13
13
>>> 25&31
25
>>> 12^13
1
>>> 10<<2
40
>>> 10<<3
80
>>> 10>>2
2
>>> 10>>3
1
>>> 10>>4
0
>>> 10>>5
0
>>> 