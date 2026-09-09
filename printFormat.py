'''
    here we are using a width of 6 beacuase
    our largest number has six digits
'''
print(format(7.265, '6.2f'))
print(format(53.832, '6.2f'))
print(format(782.861, '6.2f'))

# formatting a decimal as a percentage
print('--- ---')
print(format(0.265, '.2%'))
print(format(.55, '.0%'))
# formatting integers with width
print('--- ---')
print(format(5, '6d'))
print(format(123456, '6d')) # the largest in has six digits
print(format(853443, '6d'))
print(format(963, '6d'))
# formatting integers with separators
print('--- ---')
print(format(963, ',d'))
print(format(7853613, ',d'))
print(format(49632623, ',d'))
# formatting integers with separators and width
print('--- ---')
print(format(963, '10,d'))
print(format(7853613, '10,d'))
print(format(49632623, '10,d')) # 10 = 8 digits + 2 commas
# Formatted String Literals¶
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
animals = 'eels'
print(f'My pool is full of {animals}.')

bugs = 'bees'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# FORMAT
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
sport1='soccer'
sport2='football'
print('We like to play {} and "{}!"'.format(sport1, sport2))
