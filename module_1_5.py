immutable_var = 1,2,'a','b'
print(immutable_var)
print(type(immutable_var))
#immutable_var[0] = 5
#print(immutable_var) ошибка т.к. нельзя менять элементы кортежа
mutable_var = [1, 2, 'a', 'b', 'Modified']
print(mutable_var)
mutable_var[4] = 'Unmodified'
print(mutable_var)