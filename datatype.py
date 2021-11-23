#int
a=10 #a is an integer, there is no limit for size of int, int can take very large integer also 
print(a)
print(type(a))

#float
num=10.5 #num is float
print(num)
print(type(num))
"""
Floating point can also be return in scientific notation where we usr 'e' or 'E'
to represent the power of 10
e or E represents exponentiation
2.5 x 10^4 is return as 2.5E^4 
"""
num = 22.55e3
print(num)

#complex
'''
Complex number that written in the form of a+bj
a is real part and b is imaginary part
real - real part. If real is omitted, it defaults to 0.
imag - imaginary part. If imag is omitted, it defaults to 0.
'''
a = 2+3j
print(a)
print(type(a))

#program for adding two variable
c1=2.5+2.5J
c2=3.0-0.5j
c3=c1+c2
print(c3)

#converting Data type Explicitly
x=15.5
print(x)#print value of x as float 
print(int(x))#print value of x as int
print(x)#print the value of x int(x) will not change the value it will print float value
int(x) # event this also do the same convert to int 
print(x) # print actual value of x ie float

num=15# integer value
float(num)#convert int to float

n=10
complex(n)
print(n)
print(complex(n))

#program to convert 
n1=0o17 #octal number
n2=0B1110010 #binary number
n3=0x1c2 #hexadecimal number

print(n1)
print(int(n1))
print(n2)
print(int(n2))
print(n3)
print(int(n3))

str = '1c2'#string str contains hexadecimal number
n=int(str,16) #hence base is 16 convert str to int
print(n)#this will print 450

s1='17'
s2='1110010'
s3='1c2'

n=int(s1,8)
print('octal 17 =',n)

n=int(s2,2)
print('Binary 1110010 =',n)

n=int(s3,16)
print('Hexadecimal 1c2 =',n)

#bool data type

a=10
b=20
if(a<b):
    print("hello") # condition a<b is true and hence print hello

a=10>5 # a will be treated as bool type
print(a) # print true

a=5>10
print(a) # print false







