from random import randint

randNums = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

numsOrg = sorted(randNums)

print(f'Os números gerados foram: {randNums}')
print(f'O menor valor foi: {numsOrg[0]}')
print(f'O maior valor foi: {numsOrg[-1]}')
