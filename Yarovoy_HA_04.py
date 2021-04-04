def numbers_range(n):
    yield from n

def _filter(cond, gen_list):
    filtered = []
    for i in gen_list:
        if cond(i):  # Check condition
            filtered.append(i)
    return filtered


number_list = range(-5, 5)
a = numbers_range(number_list)

list_filtered_my_filter = _filter(lambda x: x > -4 and x < 0, a)
print(list_filtered_my_filter)

list_filtered_embed_filter = list(filter(lambda x: x > -4 and x < 0, number_list))
print(list_filtered_embed_filter)           # Output: [-5, -4, -3, -2, -1]
