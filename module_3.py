data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    n = 0
    for i in data_structure:
        if isinstance(i, int):
            n += i
        if isinstance(i, str):
            n += len(i)
        if isinstance(i, list):
            n += calculate_structure_sum(i)
        if isinstance(i, tuple):
            n += calculate_structure_sum(i)
        if isinstance(i, dict):
            n += calculate_structure_sum(i.items())
        if isinstance(i, set):
            n += calculate_structure_sum(i)
    return n
result = calculate_structure_sum(data_structure)
print(result)









