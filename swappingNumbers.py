a=6 #bits used 3 (Convert to binary)
b=5 #bits used 3 (Convert to binary)
print('The value of a before swapping', a)
print('The value of b before swapping', b)
#swapping variables using third variable
temp=a
a=b
b=temp
print('The value of a after swapping', a)
print('The value of b after swapping', b)

#swapping variables without using third variable
a=a+b #5+6=11 uses 4 bits (Convert to binary)
b=a-b #11-6=5
a=a-b #11-5=6

print('The value of a after swapping without using third variable ', a)
print('The value of b after swapping without using third variable', b)
#In the above method we waste one extra bit for the operation so in order to optimise we use XOR.
#Maintains initial variable bits and will not take rxtra bits.
a=a^b
b=a^b
a=a^b
print('The value of a after swapping with XOR', a)
print('The value of b after swapping with XOR', b)

#this below logic is unique to python and not in any other programming language
a,b=b,a #uses ROT_TWO() check n google, if you forgot
print(a)
print(b)