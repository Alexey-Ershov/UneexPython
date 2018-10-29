import look_say

for index, elem in enumerate(look_say.LookSay()):
    print(f"{index}: {elem}")
    if index > 10:
        break
