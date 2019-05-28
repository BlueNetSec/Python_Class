#example 1(solution 1) split into name,somewhere,com in tuple
s = 'name@somewhere.com'
first = s.split('@')
second = first[1]
third = second.split('.')
result = (first[0],third[0],third[1])
print(result)
