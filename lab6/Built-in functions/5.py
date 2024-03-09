def check_in_tuples(colors, c):
    result = any(c in tu for tu in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
c1 = 'White'
print(check_in_tuples(colors, c1))
c1 = 'White'
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print(check_in_tuples(colors, c1))