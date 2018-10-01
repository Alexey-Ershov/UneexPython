import more_views

gen = more_views.generator(int(input()))

for it in gen:
    print(type(it), ':', it)