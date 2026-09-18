while True:
    print("who are you")
    name = input()
    if name != 'joe':
        continue
    print('hello, joe. what is the password? (it is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1