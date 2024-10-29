my_dict = {'Ivan': 1998, 
           'Nikita': 2007,
           'Dmitry': 2005}
print(my_dict)
print(my_dict.get('Nikita'))
print(my_dict.get('Alex'))
my_dict.update({'Max':2010,
                'Vladimir': 1995})
a = my_dict.pop('Dmitry')
print(a)
print(my_dict)


my_set = {1, 1, 'Urban', 'Urban', 4.11, 3, 3}
print(my_set)
my_set.add(9)
my_set.add('orange')
my_set.remove(4.11)
print(my_set)