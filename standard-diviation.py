import numpy as np

number = '12  30 45   57   70'
values = number.split()
data = [int(value) for value in values]

sort = sorted(data)


def cv(std, mean):
    return round(((std/mean)*100), 1)


print(cv(np.std(sort), np.mean(sort)))
