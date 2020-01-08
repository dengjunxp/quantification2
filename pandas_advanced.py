# encoding=utf-8

import pandas as pd
import os

pd.set_option('expand_frame_repr', False)   # 列太多时，不换行

# 导入EOSUSD每一天的一分钟数据
# df = pd.read_csv(
#     'data/EOSUSD/BITFINEX_EOSUSD_20170701_1T.csv',
#     skiprows=1,
#     parse_dates=['candle_begin_time'],
# )
# print(df)


# 批量读取文件名 #
#################
# 获取根目录
root_path = os.getcwd()
# root_path = os.path.abspath(os.path.dirname(__file__))
coin_path = '%s%sdata%sEOSUSD' % (root_path, os.path.sep, os.path.sep)

file_list = []
# root 根目录
# dirs 目录列表
# files 文件列表
for root, dirs, files in os.walk(coin_path):
    # 当files不为空的时候
    if files:
        for f in files:
            # 判断是以.csv结尾的文件
            if f.endswith('.csv'):
                file_list.append(f)

# 遍历文件名，批量导入数据
all_data = pd.DataFrame()
for file in sorted(file_list):
    # print(file)
    # exit(1)
    # 导入数据
    file_abs = '%s%s%s' % (coin_path, os.path.sep, file)
    df = pd.read_csv(file_abs, skiprows=1, parse_dates=['candle_begin_time'])

    # 合并数据
    # 可能会造成内存溢出
    all_data = all_data.append(df, ignore_index=True)

# 对数据进行排序
all_data.sort_values(by=['candle_begin_time'], inplace=True)
# print(all_data)

# 保存完整的csv文件
# csv格式
# all_data.to_csv(path_or_buf='eos_1min_data.csv')


# 将数据存入hdf文件中  #
# pip install tables #
######################
# all_data.to_hdf(
#     'eos_1min_data.h5',
#     key='all_data',     # 库中表的名字
#     mode='w'            # 写模式
# )


# 从hdf中读取文件
# all_data = pd.read_hdf(path_or_buf='eos_1min_data.h5', key='all_data')
# print(all_data)



