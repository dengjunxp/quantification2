# encoding=utf-8

import pandas as pd
import os


# 导入hdf文件 #
##############
# all_data = pd.read_hdf(path_or_buf='eos_1min_data.h5', key='all_data')
# print(all_data)


# 将数据存入hdf文件
# 批量读取文件
# 获取根目录
# root_path = os.getcwd()
# # root_path = os.path.abspath(os.path.dirname(__file__))
# coin_path = '%s%sdata%sEOSUSD' % (root_path, os.path.sep, os.path.sep)
# file_list = []
# for root, dirs, files in os.walk(coin_path):
#     if files:
#         for f in files:
#             if f.endswith('.csv'):
#                 file_list.append(f)
#
# # 创建hdf文件
# h5_store_file = 'eos_data.h5'
# # if not os.path.isfile(h5_store_file):
# #     h5_store = pd.HDFStore(h5_store_file, mode='w')
# h5_store = pd.HDFStore(h5_store_file, mode='w')
#
# # 批量导入并且存储数据
# for file in sorted(file_list):
#     date = file.split('_')[2]
#     print(date)
#     # print('%s%s%s' % (coin_path, os.path.sep, file))
#     # exit(1)
#     # 导入数据
#     df = pd.read_csv('%s%s%s' % (coin_path, os.path.sep, file),
#                      skiprows=1,
#                      parse_dates=['candle_begin_time'])
#     # 存储数据到hdf
#     # 下标字符串为表名
#     h5_store['eos_' + date] = df
#
# # 关闭hdf文件
# h5_store.close()


# 读取hdf数据 #
##############
# 创建hdf文件
# h5_store = pd.HDFStore('eos_data.h5', mode='r')
# h5_store中的key
# print(h5_store.keys())
# 读取某个key指向的数据
# print(type(h5_store.get('eos_20170701')))
# print(h5_store['eos_20180301'])
# 关闭hdf文件
# h5_store.close()





