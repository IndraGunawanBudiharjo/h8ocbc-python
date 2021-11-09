def get_personal_info(name, age):
    return f'nama saya {name}, umur {age} tahun.'

print(get_personal_info('ani', 22))
# print(get_personal_info(age = 30, name = 'adi')) # keyword arguments


def makan(apa = 'mie'):
    return f'makan {apa}.'

print(makan())


def print_boolean(answer):
    print('The answer is', answer)

print_boolean(True)

def calculate_rect(length, width):
    print('Area: ', length * width)

length = 100
width = 20

calculate_rect(length, width)

# variable length
def penjualan(customer, *items): # tuple
    print(customer)
    print(items)
    pass

penjualan('roy', 'coklat')
penjualan('tia', 'telur', 'tepung', 'gula')

# lambda function
calculate_rect_area = lambda length, width: length * width
print(calculate_rect_area(4, 2))