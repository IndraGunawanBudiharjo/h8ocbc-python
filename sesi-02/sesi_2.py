# conditional expressions
# x = 0
# y = 5

# if x < y:               # -> 0 < 5 : True
#     print('yes')

# if y < x:               # -> 5 < 0 : False
#     print('falsy')

# if x:                   # x == 0 : False
#     print('x')

# if y:                   # y == 5 : True
#     print('y')

# if 'ault' in 'grault':   # True
#     print('ault')

# weather = 'rain'

# if weather == 'nice':
#     print('Mow the lawn')
#     print('Weed the garden')
#     print('Take the dog for a walk')
# elif weather == 'rain':
#     print('sleep')

# if 'foo' in ['foo', 'bar', 'baz', 'qux']:      # literal list
#     print('Expression was true')
#     print('Done')

    # if 20 > 10:
    #     print('20 > 10')


# num = 120

# if num < 50:
#     print('first suite')
#     print('num is small')
# else: 
#     print('second suite')
#     print('num is large')

# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000

# if uang > hargaBuku:
#     print('beli buku')
# elif uang > hargaMajalah:
#     print('beli majalah')
# else:
#     print('uang tidak cukup')

# i = 10


# ternary if
# print("yes") if i > 0 else print("no")

# control flow

# looping
a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))


# loop in list

books = ['Book1', 'Book2', 'Book3']

for book in books:
    print(book)

x = range(2,8)
for n in x:
    print(n)
