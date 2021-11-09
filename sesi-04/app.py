# print('File')

#1
# file = open('sample.txt')
# file.close()

# try:
#     with open('sample.txt', 'w', encoding = 'utf-8') as f: # write mode
#         print('opening the file..')
#         f.write('my first file\n')
#         f.write('this file\n\n')
#         f.write('contains three lines\n')
# finally:
#     print('closing the file..')
#     f.close()


# f = open('sample.txt', 'a', encoding='utf-8') # append mode
# f.write('halo')

# f = open('sample.txt', 'r', encoding='utf-8') # read mode
# result = f.read(4)
# print(result)
# result = f.read(4)
# print(result)
# result = f.read()
# print(result)

# print(f.tell())
# f.seek(15)
# print(f.read(3))

# result = f.read(4)
# print(result)

# f.seek(0)                     # baca file dengan for 
# for line in f:
#     print(line, end = '')

# f.seek(0)
# print(f.readline()) # akses per baris


# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# import sys
# assert ('win32' in sys.platform), "This code runs on Windows only." 
# assert ('linux' in sys.platform), "This code runs on Linux only." 

# coins = 10
# def check_coin(coins):
#     assert(coins == 10), "some coins fells on the way"

# check_coin(coins)

# coins = 8
# try:
#     check_coin(coins)
# except: 
#     raise Exception('Some message coins fell here..')

import sys

def os_interacion():
    assert ('linux' in sys.platform), "Function can only run on Linux system"
    assert ('win32' in sys.platform), "Function can only run on Windows system"
    print('Doing something')

# try:
#     os_interacion()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')
    
# try: 
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

# try: 
#     with open('sample.txt') as file:
#         read_data = file.read()
# except FileNotFoundError as error:
#     print(error)
# else: 
#     print('Executing the else clause')

try: 
   os_interacion()
except AssertionError as error:
    print(error)
else: 
    print('Executing the else clause')
    try:
        with open('file.log') as file:
            read_date = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')