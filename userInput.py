x=input('Enter for the value x') #default it takes as string
a=int(x)
y=input('Enter for the value y')
b=int(y)
z=a+b
print('The value given for x is ',x)
print('The value given for y is ',y)
print('The addition of X adn Y is ',z)


#To reduce the number of lines
#x=int(input('Enter for the value x'))
#y=int(input('Enter for the value y'))
#z=x+y
#print('The value given for x is ',x)
#print('The value given for y is ',y)
#print('The addition of X adn Y is ',z)

#char/string as an input
#ch=input('enter a char')
#print(ch)

#Using eval
#ch=eval(input('enter a expression'))
#print(ch) //if the input is 2+6-1=> 7

#NOTE:
#1. argv - helps to accept the values from command promt, degault is string type
#2. import sys
#x=int(sys.argv[1])
#y=int(sys.argv[2])
# in cmd => python <fileName>.py 6 5
#fileName hold index 0 i.e, in reference to argv[indexNumber]
#6 holds index number 1
#2 holds index number 5
					