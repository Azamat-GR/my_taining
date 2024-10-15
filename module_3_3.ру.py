def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params(b=25)
print_params(c=[1,2,3])

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list_ = [42, 'строка', True]
values_dict_ = {'a': 39, 'b':'строка', 'c': True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_)
print_params(**values_dict_)
print_params(*values_list_2, 42)