import re
import random


def roll(dices):
    pattern = re.compile(r'^(\d*)?d(3|4|6|8|10|12|20|100)((\+|-)\b(\d*))?$', re.I)

    number_of_rolls = 1
    mod = 0
    result = 0

    if re.match(pattern, dices):
        res = pattern.search(dices)
        if res.group(1) != '':
            number_of_rolls = int(res.group(1))

        dice = int(res.group(2))
        if res.group(5) is not None:
            mod = int(res.group(5))

        for i in range(0, number_of_rolls):
            result += random.randint(1, dice + 1)

        return result + mod


print(roll('d10-20'))
print(roll('3D20+10'))
print(roll('3d20-10'))
print(roll('d6+'))
print(roll('2d20'))
print(roll('3d333'))
print(roll('d200'))
print(roll('d205'))

