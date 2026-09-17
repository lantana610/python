# testing how python operator works
a = (2 + 2)
b = (2+3)* 6
c = 2 + 3*6
d = 48 * 57
e = 2**8
f = 23 / 7
g = 23 // 7
h = 23 % 7
i = (5-1) * ((7+1) / (3-1))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
# strings and strings concatenation
name = "alice" + "bob"
A = "Alice" * 6

print(A)
print(name)
print("hello world!")

# collecting  input

print("hello world!")
print("what is your name")
myName = input()
print("it good to meet you, " + myName)
print('the length of your name is:')
print(len(myName))
print('what is your age?')
myAge = input()
print('you will be ' + str(int(myAge) +1) + ' in a year.') 
