# encoding=utf-8
# 布林线择时策略
import pandas as pd
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.min_rows', 1000)

df = pd.read_hdf('data/eth/eth_1min_data.h5', key='all_data')

# 转换15分钟数据
rule_type = '15T'
period_df = df.resample(rule=rule_type, on='candle_begin_time', label='left', closed='left').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum',
})
period_df.dropna(subset=['open'], inplace=True)
period_df = period_df[period_df['volume'] > 0]
period_df.reset_index(inplace=True)
df = period_df[['candle_begin_time', 'open', 'high', 'low', 'close', 'volume']]
# # 筛选时间
# df = df[df['candle_begin_time'] >= pd.to_datetime('2017-01-01')]
# # 去掉index列
# df.reset_index(inplace=True, drop=True)
# print(df)
# exit()

# ======产生交易信号：布林线策略
# ====布林线策略
# 布林线中轨：n天收盘价的移动平均线
# 布林线上轨：n天收盘价的移动平均线 + m * n天收盘价的标准差
# 布林线上轨：n天收盘价的移动平均线 - m * n天收盘价的标准差
# 当收盘价由下向上穿过上轨的时候，做多；然后由上向下穿过下轨的时候，平仓。
# 当收盘价由上向下穿过下轨的时候，做空；然后由下向上穿过上轨的时候，平仓。

# 计算指标
n = 100     # 中轨n根K线的移动平均线
m = 2       # 系数

# 计算中轨
df['median'] = df['close'].rolling(n, min_periods=1).mean()
# print(df.iloc[156: 180])
# exit()
# 计算标准差
df['std'] = df['close'].rolling(n, min_periods=1).std(ddof=0)  # ddof 标准差自由度
# 计算上轨
df['upper'] = df['median'] + m * df['std']
# 计算下轨
df['lower'] = df['median'] - m * df['std']

# ====找出做多的信号（K线上穿上轨的条件）
# 当前K线的收盘价 > 上轨
condition1 = df['close'] > df['upper']
# 之前的K线的收盘价 <= 上轨
condition2 = df['close'].shift(1) <= df['upper'].shift(1)
# 将产生做多信号的那根K线的signal设置为1
df.loc[condition1 & condition2, 'signal_long'] = 1
# print(df.iloc[41607: 41636])
# exit()

# ====找出做多平仓的信号（K线下穿中轨的条件）
# 当前K线的收盘价 < 中轨
condition1 = df['close'] < df['median']
# 之前的K线的收盘价 >= 中轨
condition2 = df['close'].shift(1) >= df['median'].shift(1)
# 将产生平仓的信号当天的signal设置为0
df.loc[condition1 & condition2, 'signal_long'] = 0

# ====找出做空的信号（K线下穿下轨的条件）
# 当前K线的收盘价 < 下轨
condition1 = df['close'] < df['lower']
# 之前的K线的收盘价 >= 下轨
condition2 = df['close'].shift(1) >= df['lower'].shift(1)
# 将产生做空信号的那根K线的signal设置为-1
df.loc[condition1 & condition2, 'signal_short'] = -1

# ====找出做空平仓的信号（K线上穿中轨的条件）
condition1 = df['close'] > df['median']
condition2 = df['close'].shift(1) <= df['median'].shift(1)
df.loc[condition1 & condition2, 'signal_short'] = 0
# print(df.iloc[0: 42])
# exit()

########################################
# 去除信号组合的重复的情况（多少种组合）
# df.drop_duplicates(subset=['signal_long', 'signal_short'], inplace=True)
# print(df)
# exit()
########################################

# ====合并做多做空信号，去除重复信号
# df['signal'] = df[['signal_long', 'signal_short']].sum(axis=1)
# 如果pandas版本最新，使用下面代码和视频保持一致。
# min_count的意思是指定 NaN 个最少个数为1 超过1个NaN 就不计算 所以不会出现0.0
df['signal'] = df[['signal_long', 'signal_short']].sum(axis=1, min_count=1, skipna=True)

# print(df[['signal_long', 'signal_short', 'signal']].iloc[0:10])
# print(df.iloc[0: 40])
# exit()

temp = df[df['signal'].notnull()][['signal']]
# print(temp.iloc[0: 10])

temp = temp[temp['signal'] != temp['signal'].shift(1)]
# print(temp.iloc[0: 10])
# exit()
df['signal'] = temp['signal']
# print(df[['candle_begin_time', 'signal']])
# exit()

# 删除中间列
df.drop(['median', 'std', 'upper', 'lower', 'signal_long', 'signal_short'], axis=1, inplace=True)

# ====由signal计算出实际每天持有的仓位
# signal的计算运用了收盘价，是每根K线收盘之后产生的信号，到第二根开盘的时候才买入，仓位才会改变。
df['pos'] = df['signal'].shift()
df['pos'].fillna(method='ffill', inplace=True)
df['pos'].fillna(value=0, inplace=True)     # 将初始行数的position补全为0

# print(df)

# ====将数据存入hdf文件中
df.to_hdf('output/eth_bolling_signal.h5',
          key='all_data', mode='w')
