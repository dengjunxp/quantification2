# encoding=utf-8

import pandas as pd

df = pd.DataFrame({'name': ['bob', 'sos', 'bob', 'sos', 'bob', 'sos', 'bob', 'bob'],
                   'root': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'close': [3, 1, 4, 1, 5, 9, 8, 6],
                   'position': [1, 2, 3, 4, 5, 6, 7, 8]})


temp = df.groupby('name').apply(lambda x: x['close'] + x['position'])
print(temp)
temp = temp.reset_index(level=[0])
print(temp[0])
exit()

# for name, group in grouped:
#     print(name)
#     print(group)


# def fill_none(one_group):
#     return one_group.fillna(one_group.mean())
#
#
# d = grouped.apply(fill_none)
# print(d)
