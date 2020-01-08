# encoding=utf-8
# 缺失值处理
# 排序函数

import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='data/BITFINEX-1H-data-20180124.csv',
    skiprows=1,
    # nrows=15,
)

df['symbol'] == 'BTCUSD'

# print(df[df['symbol'] == 'BTCUSD'])     # 筛选出BTCUSD的记录
# print(df[df['symbol'] == 'BTCUSD'].index)     # 显示筛选记录的index
# print(df[df['symbol'].isin(['BTCUSD', 'LTCUSD', 'ETHUSD'])])   # 判断列是否存在以下的值
# print(df[df['close'] < 10.0 | (df['symbol'] == 'AIDUSD')])      # 条件查询


# 缺失值的处理 #
###############
# 创建缺失值 #
#############
index = df[df['candle_begin_time'].isin(['2018-01-24 00:00:00', '2018-01-24 12:00:00'])].index
df.loc[index, '12小时'] = df['candle_begin_time']
# print(df)

# 删除缺失值 #
#############
# print(df.dropna(how='any'))     # 将带空值的行删除
# 将subset 中指定的列中，有空值的行删除；how='all' 都为空时，才删除
# print(df.dropna(subset=['12小时', 'close'], how='any'))


# 补全空值 #
###########
# print(df.fillna(value=0))   # 将缺失值赋值为固定值
# df['12小时'].fillna(value=df['close'], inplace=True)      # 从其他的列赋值缺失值
# print(df)

# print(df.fillna(method='ffill'))        # 向上查找非空值替换空值
# print(df.fillna(method='bfill'))        # 向下查找非空值替换空值


# 找出缺失值 #
#############
# print(df.notnull())     # 判断是否为空值，返向函数为isnull()
# print(df[df['12小时'].notnull()])     # 将'12小时'列为非空的行输出


# 排序函数 #
###########
# print(df.sort_values(by=['candle_begin_time'], ascending=1))    # by 指定哪一列， ascending=1 从小到大排序
# print(df.sort_values(by=['symbol', 'candle_begin_time'], ascending=[1, 1]))     # 多列排序


# 两个DataFrame上下合并的操作，append操作 #
########################################
# df1 = df.iloc[0:10][['candle_begin_time', 'symbol', 'close', 'volume']]
# print(df1)
# df2 = df.iloc[5:15][['candle_begin_time', 'symbol', 'close', 'volume']]
# print(df2)
# df3 = df1.append(df2, ignore_index=True)    # 指定ignore_index，用户重新确定index
# print(df3)


# 对数据进行去重 #
################
# df3.drop_duplicates(
#     subset=['candle_begin_time', 'symbol'],     # subset 参与判断重复的列，都相同才会去重
#     keep='first',   # 保留哪一行数据 first 保留第一行，last 保留最后一行
#     inplace=True,
# )


# 其他常用重要函数 #
##################
# 重置索引
# df.reset_index(inplace=True, drop=True)        # 重置index，drop=False 原有的索引取名为index保留下来, drop=True则不会保留
# print(df)


# 列重命名
# print(df.rename(columns={'close': '收盘价', 'open': '开盘价'}))   # 重命名close和open


# 判断空DataFrame
# print(df.empty)
# print(pd.DataFrame().empty)


# 转置
# print(df.T)

# 字符串处理
# print(df['symbol'].str[:3])
# print(df['symbol'].str.upper())
# print(df['symbol'].str.lower())
# print(df['symbol'].str.len())
# print(df['symbol'].str.contains('AID'))     # 判断字符串中是否包含某些特定字符
# print(df['symbol'].str.replace('USD', 'EUR'))   # 替换，将USD替换为EUR
# 参见地址：http://pandas.pydata.org/pandas-docs/stable/text.html#method-summary


# 时间处理
# print(df['candle_begin_time'])
# print(df.at[0, 'candle_begin_time'])
# print(type(df.at[0, 'candle_begin_time']))
# 日期类型转换（不支持：1999年1月1日）
# df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'])
# print(type(df.at[0, 'candle_begin_time']))
# 日期信息提取
# df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'])
# print(df['candle_begin_time'].dt.year)              # 年份
# print(df['candle_begin_time'].dt.month)             # 月份
# print(df['candle_begin_time'].dt.day)               # 日
# print(df['candle_begin_time'].dt.hour)              # 小时
# print(df['candle_begin_time'].dt.minute)            # 分钟
# print(df['candle_begin_time'].dt.second)            # 秒
# print(df['candle_begin_time'].dt.week)              # 一年中的第几周
# print(df['candle_begin_time'].dt.dayofyear)         # 一年中的第几天
# print(df['candle_begin_time'].dt.dayofweek)         # 一周中的星期几
# print(df['candle_begin_time'].dt.weekday)           # 一周中的星期几
# print(df['candle_begin_time'].dt.weekday_name)      # 一周中的星期几（英文全名）
# print(df['candle_begin_time'].dt.days_in_month)     # 这一天所在的月份共有多少天
# print(df['candle_begin_time'].dt.is_month_start)    # 这一天是否是该月的开头
# # [weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]
# print(df['candle_begin_time'] + pd.Timedelta(days=1))   # 增加一天，Timedelta用于表示时间差数据
# print((df['candle_begin_time'] + pd.Timedelta(days=1)) - df['candle_begin_time'])   # 返回 1 days


# rolling、expanding操作 #
#########################
# print(df['close'].mean())       # 计算close这一列的均值
# # 得到每一天的最近3天close的均值？（如何计算移动平均线）
# # 使用rolling函数
# df['收盘价_3天均值'] = df['close'].rolling(3).mean()
# print(df[['close', '收盘价_3天均值']])
# # roling(n) 为取最近n行数据，只计算这n行数据。后面可以接各类计算函数，例如max、min、std等
# print(df['close'].rolling(3).max())
# print(df['close'].rolling(3).min())
# print(df['close'].rolling(3).std())


# rolling可以计算每天的最近3天的均值，如果想计算每天的从开始至今的均值，应该如何计算？
# 使用expanding操作
# df['收盘价_至今均值'] = df['close'].expanding().mean()
# print(df[['close', '收盘价_至今均值']])


# expanding 为取从头至今的数据，后面可以接各类计算函数
# print(df['close'].expanding().max())
# print(df['close'].expanding().min())
# print(df['close'].expanding().std())


# 输出到本地文件 #
################
# print(df)
# df.to_csv('output.csv', encoding='gbk', index=False)

# 全部的函数：http://pandas.pydata.org/pandas-docs/stable/api.html
