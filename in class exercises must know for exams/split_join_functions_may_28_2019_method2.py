#example 1(solution 1) split into name,somewhere,com in tuple
s = 'name@somewhere.com'
s = '.'.join(s.split('@'))
print(tuple(s.split('.')))

