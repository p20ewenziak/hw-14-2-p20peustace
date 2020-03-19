#Author:PJE 3/18/20

dictionary = {}
string = input('Enter a string: ')
string = string.lower()

for x in string:
    dictionary[x] = 0

for x in string:
    for k, v in dictionary.items():
        if x == k:
            dictionary[k] += 1

for k, v in sorted(dictionary.items()):
    print(k,v)
