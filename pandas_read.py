# encoding=utf-8

import pandas as pd

df = pd.read_csv(filepath_or_buffer='data/BITFINEX_BTCUSD_20180124_1T.csv',
                 sep=',',
                 # 跳过n行开始读取
                 skiprows=1,
                 # 读入前n行
                 # nrows=15,
                 # 将指定字段解析为日期类型
                 # parse_dates=['candle_begin_time'],
                 # 将指定列设置为index，若不指定，index默认为0,1,2,3,4...
                 index_col=['candle_begin_time'],
                 # 读取指定的几列数据
                 # usecols=[],
                 # 当某行数据有问题时，报错。设定为False时为不报错
                 # error_bad_lines=False,
                 # 将数据中的null识别为空值
                 # na_values='NULL',
                 )

# 查看数据 #
###########
# print(df.shape)           # 输出dataframe有多少行，多少列
# print(df.shape[0])        # 取行数量，df.shape[1] 取列数量
# print(df.columns)         # 顺序输出每一列的名字
# print(df.index)           # 顺序输出一行的名字
# print(df.dtypes)          # 数据每一列的类型
# print(df.head(3))         # 查看前3行的数据，默认为5
# print(df.tail(3))         # 查看最后3行的数据，默认为5
# print(df.sample(n=3))     # 随机抽取3行，想要去固定比例的话，可以用frac参数 frac=0.5：取出50%的行。
# print(df.describe())      # 对每一列数据有直观感受，只会对数字类型的列有效
                            # count 有多少行数据，会将空值排除在外
                            # mean  平均值
                            # std   标准差
                            # min   最小值
                            # 25%   25%分位数
                            # 50%   50%分位数，中位数
                            # 75%   75%分位数
                            # max   最大值

# (print)打印格式的修正 #
#######################
# pd.set_option('expand_frame_repr', False)     # 当列太多时不换行
# pd.set_option('max_colwidth', 8)              # 设定每一列的最大宽度
# pd.set_option('display.max_rows', 101)        # 设定显示最大的行数
# pd.set_option('display.max_rows', None)       # 显示所有行
# pd.set_option('display.max_columns', None)    # 显示所有列
# pd.setpd.set_option('precision', 7)           # 浮点数的精度，默认为6
# 更多设置参见 http://pandas.pydata.org/pandas-docs/stable/options.html


# 选取指定的行、列 #
##################
# print(df['open'])               # 选取指定列
# print(df['open', 'close'])      # 同时选取多列


# loc操作：通过label（columns和index的名字）来读取数据 #
####################################################
# print(df.loc['2018-01-24 00:01:00'])    # 选取指定某一行，读取的数据类型是Series类型
# print(df.loc[['2018-01-24 00:01:00', '2018-01-24 00:05:00']])   # 选取指定的两行
# print(df.loc['2018-01-24 00:01:00':'2018-01-24 00:05:00'])      # 选取范围内的多行
# print(df.loc['2018-01-24 00:01:00':'2018-01-24 00:05:00', 'open':'close'])    # 选取指定范围的矩阵
# print(df.at['2018-01-24 00:01:00', 'open'])     # 读取指定行列的一个数据

# iloc操作：通过position来读取数据 #
##################################
# print(df.iloc[0])
# print(df.iloc[1:3])
# print(df.iloc[:, 1:3])
# print(df.iloc[1:3, 1:3])
# print(df.iloc[:, :])
# print(df.iat[1, 1])


# 列操作，行列的加减乘除 #
#######################
# print('2018年1月24日' + df['北京时间'])    # 字符串列可以直接加上字符串，对整列进行操作
# print(df['close'] * 100)
# print(df['close'] * df['volume'])
# df['北京时间2'] = '2018年1月24日' + df['北京时间']


# 统计函数 #
###########
# print(df['close'].mean())   # 求一整列的均值，返回一个数，会自动排除空值
# print(df[['close', 'open']].mean())   # 求两列的均值，返回Series
# print(df[['close', 'open']].mean(axis=1))     # 求两列均值，返回DataFrame

# print(df['high'].max())     # 一整天中的最高价
# print(df['low'].min())     # 一整天中的最低价
# print(df['close'].std())     # 标准差
# print(df['high'].count())     # 有多少条非空的个数
# print(df['high'].median())     # 中位数
# print(df['high'].quantile(0.25))     # 分位数


# shift 类函数、删除列的方式 #
############################
# df['上周期close'] = df['close'].shift(1)      # 读取上一行的数据，若参数设定为3，就是读取上三行的数据
# df['下周期close'] = df['close'].shift(-1)
# del df['上周期close']      # 删除某一列的方法

# df['涨跌'] = df['close'].diff(-1)     # 求本行数据和上一行数据相减得到的值
# print(df[['close', '涨跌']])
# df.drop(['涨跌'], axis=1, inplace=True)   # 删除涨跌数据，axis=1删除一整列

# df['涨跌幅'] = df['close'].pct_change(1)   # 和上一根K线相比的涨幅
# df['涨跌幅'] = df['close'].pct_change(-1)  # 和下一根K线相比的涨幅
# print(df[['close', '涨跌幅']])


# cum(cumulative)类函数 #
#########################
# df['volume_cum'] = df['volume'].cumsum()    # 累加，每一行的值加上上面所有行的值，结果保存到volume_cum列中
# print(df[['volume', 'volume_cum']])
# print((df['涨跌幅'] + 1.0).cumprod())          # 累成，每一次投资后的资金曲线


# 其他的列函数 #
###############
# df['close_排名'] = df['close'].rank(ascending=True, pct=False)    # 返回每一列close的排名，ascending=True从小到大  pct=True输出排名的百分比
# print(df[['close', 'close_排名']])
# print(df['close'].value_counts())   # 统计每个元素出现的次数




