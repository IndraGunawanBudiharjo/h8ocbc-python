# int & float
# print(type(123))
# print(type(4.2))

# string
# print(type('Halo'))
# message = 'haha'
# print(f'halo {message}') 

# print("halo \"hehe\"")
# 

# s = 'foo'
# b = 'BAR'
# print(s.capitalize())
# print(b.lower())
# print(s.swapcase())

# boolean
# print(int(True))

# list

# primary_colors = ['Merah', 'Jingga', 'Biru']
# print(primary_colors[0])
# print(primary_colors[-2])


# event_a = ['Malang', 1200]
# event_b = ['Jogja', 1000]
# events = [event_a, event_b]

# events[0][0] = 'Surabaya'
# print(event_a[0])
# print(events[0][0])

# list slicing
hewan = ['kucing', 'ayam', 'kupu-kupu', 'anjing']
# hewan[x:y] 
#   x -> inclusive
#   y -> exclusive
# hewan[1:2] = ['tikus', 'kelinci']
# print(hewan)

# tuple
t = ('foo', 'bar', 'baz', 'qux')
# print(t[0])
# print(t[-1])
# (a, b, *c) = t
# print(a)
# print(b)
# print(c)

# dictionary
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
}

MLB_team['Boston'] = 'Red Fox'
print(MLB_team['Minnesota'])
print(MLB_team['Boston'])

