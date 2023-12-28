import random
string = 'string'
r = random.choice(string)
k = '$'
print("Original string:", string)
res = string.replace(r, k)
print("Modified string:", res)
