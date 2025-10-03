""" #list
l1 = ['1', 33, 'Dsd', 7.045]
print(l1[::-1])

#Sets
s1 = {1,23,5,4,23}
print(s1)

#Dictionary

d = {"index1": 1, "index2": "BAG", "index3": 7.09}
print(d['index3'])

if d['index3']:
    print(True)

for i in range(10):
    print(i) """

""" numbers = [1, 2, 12, 130, 12, 3, -1, 2, 41]

max_number = numbers[0]

for current in numbers:
    if current > max_number:
        max_number = current

print(f"max number - {max_number} and method - {max(numbers)}")
 """
debt = 0
while debt < 1000:
    print(f'current debt - {debt}')
    debt += 10
