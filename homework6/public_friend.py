acqs = {}
all_people = set()


def getAcq(first_person, second_person):
    global acqs

    if acqs.get(first_person) is None:
        acqs[first_person] = {second_person}

    else:
        acqs[first_person].add(second_person)


first_person, second_person = tuple(int(i) for i in input().split(','))
while not(first_person == second_person == 0):
    getAcq(first_person, second_person)
    getAcq(second_person, first_person)
    
    all_people.add(first_person)
    all_people.add(second_person)

    first_person, second_person = tuple(int(i) for i in input().split(','))

for key, value in acqs.items():
    if all_people - {key} == value:
        print(key, end=' ')

print()
